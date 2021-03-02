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
    '''
    Classifies features from the folder pathIN, 
    into a positive (chainsaw) or negative (not chainsaw) class.
    If segment is classified as chainsaw, the corresponding segment 
    of the .wav under analysis is saved in wavs/ folder.

	    Parameters:
	            pathIN (str): Path where function looks for extracted features
	            modelfileName (str): Filename of the pretrained DNN model for classification
				Nclasses (int): Number of classes used for the classification task
				probThresh (double): Probability threshold for the classifier
	    Returns:
	            totalDetectedDuration (double): The total duration of chainsaw segments detected. (s)
    '''
    from tensorflow.keras.models import Model
    from tensorflow.keras.models import load_model
    import tensorflow as tf
    
    Fs=8000
    featurePathIN=(pathIN + '/' + 'Features')
    pathOUT=(pathIN + '/' + 'Extracted_segments')
    model = load_model(modelfileName)
    filenamesIN = glob.glob(os.path.join(featurePathIN,'*.obj'))  
    positiveSegments=np.zeros((0,2))     
    totalDetectedDuration=0
    for filename in filenamesIN:
        with open(filename,'rb') as fid:
            dataIN = pickle.load(fid,encoding='latin1')            
        featMatrix=dataIN['X']  
        wavName=dataIN['Nw']
        recName=dataIN['Nr']
        ftrTimeBorders=dataIN['ftrTB']        
        Nsamples=np.shape(featMatrix)[0]   
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
                hours,minutes,seconds=create_timestamp(positiveSegments[u,0])   
                prob='%.2f' %np.mean(positiveSawPRs[finalList[u]])
                instanceName=('instance' + '_' + hours + 'h' + minutes + 'm' + seconds + 's' + '_prob' + prob + '.wav')
                # instanceName=('prob' + prob + '_instance' + '_' + hours + 'h' + minutes + 'm' + seconds + 's.wav')                
                sf.write(os.path.join(pathOUT,(recName + '_' + instanceName)),sIN,Fs)  
                print('Utterance classified as chainsaw with mean probability ' + str(np.mean(positiveSawPRs[finalList[u]])))
                totalDetectedDuration+=positiveSegments[u,1]-positiveSegments[u,0]  
        print('Total detected duration of chainsaw in seconds is ' + '%.2f' %totalDetectedDuration) 

    return totalDetectedDuration 
    # time.sleep(4)         
    
