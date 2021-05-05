import argparse
import os
import numpy as np
import librosa
import glob
import multiprocessing
from extract_pcen_feature import extract_pcen_feature as extract_features
#from classify_features import classify_features 
from classify_features_exp2raven import classify_features  

def main(pathIN, VADthresh, probThresh, nopREQ, del_temp=True, model = 'pcen_rnn4_cl2_RMED_allARUs_run0.hdf5'):                    
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
        # if args.VADthresh>=0.0779:
        #     VADthresh=args.VADthresh
        #     print('Setting VAD threshold value to the requested value')        
        # else:
        #     VADthresh=0.078   
        #     print('VAD threshold value is too small, setting it to 0.078')   
            
        # if args.probThresh>1:
        #     print('Probability threshold should be lower than one, a value greater than one will not admit any positive decisions') 
        # probThresh=args.probThresh
        
        inputWavPath=pathIN 
        outputDataPath=pathIN
        wavFileNames=[]
        
    #%% Specify classicication model and number of classes   
        # modelfileName ='pcen_rnn4_cl2_RMED_allARUs_run0.hdf5';
        modelfileName = model

        Nclasses=2 
         
    # %%
        if os.path.exists(inputWavPath + '/' + 'Features') == False:
            os.mkdir((inputWavPath + '/' + 'Features'))      
        
        if os.path.exists(inputWavPath + '/' + 'Extracted_segments') == False:
            os.mkdir((inputWavPath + '/' + 'Extracted_segments'))    

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
        classify_features(outputDataPath,f"models/{modelfileName}",Nclasses,probThresh)
        # if del_temp:
        #     ftrs =  inputWavPath + '/' + 'Features'
        #     if os.path.exists(ftrs):
        #         files = glob.glob(ftrs+'/*')
        #         for f in files:
        #             os.remove(f)

        if del_temp:
            import shutil
            ftrs =  inputWavPath + '/' + 'Features'
            if os.path.exists(ftrs):
                for filename in os.listdir(ftrs):
                    file_path = os.path.join(ftrs, filename)
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                    except Exception as e:
                        print('Failed to delete %s. Reason: %s' % (file_path, e))

                