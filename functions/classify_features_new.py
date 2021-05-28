# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 16:25:35 2019
@author: FORTH-ICS
"""
import os
import numpy as np
import librosa
import pickle
import soundfile as sf 
import time
import glob
import pandas as pd

#%%
def create_timestamp(eventTime): 
    minutes,seconds=divmod(eventTime,60)  
    hours, minutes=divmod(minutes,60) 
    s=format(int(seconds), '02d')
    m=format(int(minutes), '02d')
    h=format(int(hours), '02d')
        
    return h,m,s   

#%% 
def classify_features(pathIN,modelfileName,Nclasses,probThresh):
    # from tensorflow.keras.models import Model
    from tensorflow.keras.models import load_model
    import tensorflow as tf
    
    Fs=8000
    featurePathIN=(pathIN + '/' + 'features')
    pathOUT=(pathIN + '/' + 'extracted_segments')
    model = load_model(modelfileName)
    filenamesIN = glob.glob(os.path.join(featurePathIN,'*.obj'))  
    cnt=0
    idxs=[]
    uDurs=[]
    instanceTimes=[]
    beginTime=[]
    endTime=[]
    fileOffsets=[]
    beginFiles=[]   
    probabilities=[]    
    positiveSegments=np.zeros((0,2))     
    totalDetectedDuration=0
    save_params = []
    
    for filename in filenamesIN:
        with open(filename,'rb') as fid:
            dataIN = pickle.load(fid,encoding='latin1')            
        featMatrix=dataIN['X']  
        wavName=dataIN['Nw']
        recName=dataIN['Nr']
        ftrTimeBorders=dataIN['ftrTB']    
        accumulativeDuration=dataIN['accumulativeDuration']        
        Nsamples=np.shape(featMatrix)[0]  
        
        try:
            recInitiationSeconds=int(recName[-6:-4])*3600+int(recName[-4:-2])*60+int(recName[-2:]) ##<------
        except:
            recInitiationSeconds=0         
        
        
        if Nsamples>0:
            try:
                probs = model.predict(featMatrix,batch_size=16)
            except:
                featMatrix=tf.expand_dims(featMatrix,axis = -1)
                probs = model.predict(featMatrix,batch_size=16)
            probs=np.reshape(probs,(Nsamples,Nclasses))
            sawPR=probs[:,0]  
            positiveArgs=np.argwhere(sawPR>probThresh)
            positiveArgs=positiveArgs.flatten()
            positiveSegments=ftrTimeBorders[positiveArgs,:]
            positiveSawPRs=sawPR[positiveArgs]
       
            finalList=[]
            tempList=[0,]
            q=0
            m=1             
            while m < np.shape(positiveSegments)[0]:
                q+=1
                if positiveSegments[m,0]<=positiveSegments[m-1,1]:
                    positiveSegments[m-1,1]=positiveSegments[m,1]
                    positiveSegments=np.delete(positiveSegments,m,axis=0)
                    tempList.append(q)                         
                else:
                    finalList.append(tempList)
                    tempList=[q,]
                    m+=1 
                    
            finalList.append(tempList)
            Nps=len(positiveSegments)
            for u in range(Nps):    

                sIN, sr = librosa.load(wavName, sr=Fs, offset=positiveSegments[u,0],duration=positiveSegments[u,1]-positiveSegments[u,0])   
                sIN=sIN-np.mean(sIN)
                
                cnt+=1
                idxs.append(cnt)
                hours,minutes,seconds=create_timestamp(positiveSegments[u,0]+recInitiationSeconds)   
                prob='%.2f' %np.mean(positiveSawPRs[finalList[u]])
                timeInterval=positiveSegments[u,:]
                uDur=timeInterval[1]-timeInterval[0]                  
                instanceTime=(format(int(hours),'02d') + ':' + format(int(minutes),'02d') + ':' + format(int(seconds),'02d'))                
                instanceTimes.append(instanceTime)
                beginTime.append('%.4f' %(timeInterval[0]+accumulativeDuration))
                endTime.append('%.4f' %(timeInterval[1]+accumulativeDuration))
                fileOffsets.append('%.4f' %timeInterval[0])
                beginFiles.append(recName)                
                probabilities.append(prob)
                uDurs.append('%.2f' %uDur)   

                instanceName=f'instance_{hours}h{minutes}m{seconds}s_prob{prob}.wav'
                sf.write(os.path.join(pathOUT,(recName + '_' + instanceName)),sIN,Fs)  
                
                print('Utterance classified as chainsaw with mean propability ' + str(np.mean(positiveSawPRs[finalList[u]])))
                totalDetectedDuration+=positiveSegments[u,1]-positiveSegments[u,0]  
                save_params.append(
                    dict(wavName = wavName, sr=Fs, 
                        offset=positiveSegments[u,0],
                        duration=positiveSegments[u,1]-positiveSegments[u,0],
                        instanceName=instanceName,
                        outName = os.path.join(pathOUT,(recName + '_' + instanceName))))

        print('Total detected duration of chainsaw in seconds is ' + '%.2f' %totalDetectedDuration) 

 #%%
    if cnt>0:
        textName=('results_chainsaw')               
        # textName=(recName[:-4] + '_' + 'chainsaw')               
        d = {'Selection': idxs, 'View': 'spectrogram', 'Channel': 1, 'Low Frequency (Hz)':20,'High Frequency (Hz)':2000, 'Pattern': 'chainsaw','Begin Time (s)': beginTime,
             'End Time (s)': endTime, 'Begin File': beginFiles, 'File Offset (s)': fileOffsets, 'TOD': instanceTimes, 'Probability':probabilities, 'dur':uDurs}
        columnsOrder=['Selection','View','Channel','Begin Time (s)','End Time (s)','Low Frequency (Hz)','High Frequency (Hz)','Begin File','File Offset (s)','Pattern','Probability','TOD','dur']
        df = pd.DataFrame(data=d)
        df.to_csv((pathIN + '/' + textName + '.txt'), index=False, header=True, sep='\t', columns=columnsOrder) #, mode='a')                

    
def save_audio(save_params, ind):

    sr = 8000  
    save_audio_file(
        wavName=save_params[ind]['wavName'], sr=save_params[ind]['sr'], 
        offset=save_params[ind][offset],duration=save_params[ind][duration],
        outName = save_params[ind][outName])

def save_audio_file(wavName, sr, offset,duration, outName):
    import librosa, soundfile as sf
    sIN, sr = librosa.load(wavName, sr=sr, offset=offset,duration=duration)   
    sIN = sIN-np.mean(sIN)
    sf.write(outName,sIN,Fs)  

