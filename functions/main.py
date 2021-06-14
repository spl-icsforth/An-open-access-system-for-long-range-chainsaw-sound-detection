import argparse
import os
import numpy as np
import librosa
import glob
import multiprocessing
from extract_pcen_feature import extract_pcen_feature as extract_features
from classify_features_new import classify_features

def main(pathIN, VADthresh, probThresh, nopREQ, del_temp=True, model = 'pcen_rnn4_cl2_RMED_allARUs_run0.hdf5', recursive=False):                    
    #%% Parameters
    maxDur=400 #in seconds
    nop=multiprocessing.cpu_count()
    print(str(int(nop)) + 'cpus found')
    nopREC=np.max([1,nop])
    if nopREQ<nopREC:
        nopUSE=nopREQ
    else:
        nopUSE=nopREC
    print(str(nopUSE) + 'cpus will be used')   
    
    inputWavPath=pathIN 
    outputDataPath=pathIN
    durations=[]        
    wavFileNames=[]
    
#%% Specify classicication model and number of classes   
    # modelfileName ='pcen_rnn4_cl2_RMED_allARUs_run0.hdf5';
    modelfileName = model

    Nclasses=2 
     
# %%
    if os.path.exists(inputWavPath + '/' + 'features') == False:
        os.mkdir((inputWavPath + '/' + 'features'))      
    
    if os.path.exists(inputWavPath + '/' + 'extracted_segments') == False:
        os.mkdir((inputWavPath + '/' + 'extracted_segments'))    

#%% do the job  
    folder_with_recordings=(inputWavPath + '/*.wav')
    if recursive: wavs = glob.glob(folder_with_recordings.replace('*', '**/*'), recursive = recursive)
    else: wavs = glob.glob(folder_with_recordings)
    
    for wavName in wavs:
        pool=multiprocessing.Pool(nopUSE)
        fileDuration=librosa.get_duration(filename=wavName)
        sr=librosa.get_samplerate(wavName)
        durations.append(fileDuration)       

        if sr==8000:
            wavFileNames.append(wavName)                     
            if fileDuration<maxDur:
                timeBorders=np.array((0,fileDuration))   
            else:
                timeBorders=np.arange(0,fileDuration,maxDur)
                timeBorders=np.delete(timeBorders,-1,axis=None)
                timeBorders=np.append(timeBorders,fileDuration)
                
            Nsegm=timeBorders.size    
            
            for segmIdx in range(Nsegm-1): #range(0,Nsegm-1):       
                # pool.apply_async(extract_features, args=(wavName,outputDataPath,timeBorders,segmIdx,VADthresh))
                pool.apply_async(extract_features, \
                    args=(wavName,outputDataPath,durations, timeBorders,segmIdx,VADthresh))

            pool.close()
            pool.join() 

        else:
            print(wavName.split(os.sep)[-1] + ' has a sampling rate different than 8000  Hz, will not process this audio file ')
 #%% Run classifier and extract positive .wav segments       
    classify_features(outputDataPath,f"models/{modelfileName}",Nclasses,probThresh)

    if del_temp:
        import shutil
        ftrs =  inputWavPath + '/' + 'features'
        if os.path.exists(ftrs):
            try:
                shutil.rmtree(ftrs)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
