# -*- coding: utf-8 -*-
'''
Detects chainsaw activity in each .wav recording in a given folder

        Parameters:
                -u (int): Number of processing units employed
                -t (double): Treshold for VAD detection, default=0.078
                -p (double): Treshold for RNN classifier, default=0.75
                
        Output:
                None
                Fills "Extracted_segments" folder with the detected chainsaw segments, 
                and in "Features" folder are the corresponding features used by
                the classifier.

        Syntax examples: 
                python detect_chainsaw.py path/that/points/to/folder/with/wavs 
                python detect_chainsaw.py path/that/points/to/folder/with/wavs -t 0.079
                python detect_chainsaw.py path/that/points/to/folder/with/wavs -p 0.5
                python detect_chainsaw.py path/that/points/to/folder/with/wavs -t 0.079 -u 4 -p 0.6 

'''

import argparse
import os
import numpy as np
import librosa
import glob
import multiprocessing
import sys
sys.path.append("./functions")

from extract_pcen_feature import extract_pcen_feature as extract_features
from classify_features import classify_features 

def main():
        
    parser = argparse.ArgumentParser(description='batch_processor', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('pathIN', help='folder containing audio data')    
    parser.add_argument('-u', '--nopREQ', type=int, default=6, help='number of processing units employed')    
    parser.add_argument('-t', '--VADthresh', type=float, default=0.078, help='Treshold for VAD detection, default=0.078') 
    parser.add_argument('-p', '--probThresh', type=float, default=0.75, help='Treshold for RNN classifier, default=0.75')     
    args = parser.parse_args()

    #%% Parameters
    maxDur=400 #in seconds
    nop=multiprocessing.cpu_count()
    print(str(int(nop)) + 'cpus found')
    nopREC=np.max([1,nop-1])
    if args.nopREQ<nopREC:
        nopUSE=args.nopREQ
    else:
        nopUSE=nopREC
    print(str(nopUSE) + 'cpus will be used')   
    if args.VADthresh>=0.0779:
        VADthresh=args.VADthresh
        print('Setting VAD threshold value to the requested value')        
    else:
        VADthresh=0.078   
        print('VAD threshold value is too small, setting it to 0.078')   
        
    if args.probThresh>1:
        print('Probability threshold should be lower than one, a value greater than one will not admit any positive decisions') 
    probThresh=args.probThresh
    
    inputWavPath=args.pathIN 
    outputDataPath=args.pathIN
    wavFileNames=[]
    
#%% Specify classicication model and number of classes   
    modelfileName='pcen_rnn4_cl2_RMED_allARUs_run0.hdf5';
    Nclasses=2 
     
# %%
    if os.path.exists(inputWavPath + '/' + 'features') == False:
        os.mkdir((inputWavPath + '/' + 'features'))      
    
    if os.path.exists(inputWavPath + '/' + 'extracted_segments') == False:
        os.mkdir((inputWavPath + '/' + 'extracted_segments'))    

#%% do the job  
    folder_with_recordings=(inputWavPath + '/*.wav')
    for wavName in glob.glob(folder_with_recordings):
        pool=multiprocessing.Pool(nopUSE)
        fileDuration=librosa.get_duration(filename=wavName)
        sr=librosa.get_samplerate(wavName)
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
                pool.apply_async(extract_features, args=(wavName,outputDataPath,timeBorders,segmIdx,VADthresh))

            pool.close()
            pool.join() 
        else:
            print(wavName.split(os.sep)[-1] + ' has a sampling rate different than 8000  Hz, will not process this audio file ')
 #%% Run classifier and extract positive .wav segments       
    classify_features(outputDataPath,f"Models/{modelfileName}",Nclasses,probThresh)    

if __name__ == "__main__":
    main()