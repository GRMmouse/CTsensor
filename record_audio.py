import pyaudio
import wave
import os
import time


#globals, settings for recording the audio
FORMAT=   pyaudio.paInt16 #sampling size and format
CHANNELS=  1 #number of channels
RATE=  44100   #sampling rate
SAMPLE_SIZE =  1024  #how many samples in a frame that stream will read
RECORD_TIME =  1  #time in seconds to record for


#sound_record function
def sound_record(FORMAT,CHANNELS,RATE,SAMPLE_SIZE,RECORD_TIME,WAVE_FILENAME):  #takes in settings as parameters and returns a 60sec .wav file
    audio= pyaudio.PyAudio() #instantiate PyAudio()
    stream = audio.open(format=FORMAT, channels= CHANNELS,
                    rate=RATE, input=True, frames_per_buffer= SAMPLE_SIZE) #opens a stream to record audio on

    frames = []  #creates an empty data frame

    for i in range(0, int(RATE / SAMPLE_SIZE * RECORD_TIME)):   #read the samples from the stream
        data = stream.read(SAMPLE_SIZE)
        frames.append(data)    #append the samples to data frames

    #close the stream and stop recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    #write the frames to a .wav file
# WAVE_FILENAME= str(counter)+'.wav'
    wavfile = wave.open(WAVE_FILENAME, 'wb')   #opens a write only .wav file
    wavfile.setnchannels(CHANNELS)
    wavfile.setsampwidth(audio.get_sample_size(FORMAT))
    wavfile.setframerate(RATE)
    wavfile.writeframes(b''.join(frames))
    wavfile.close()

    return wavfile


#check_buffer function
def check_buffer(pathName):  #takes a string as a parameter, the current folder is the pathname
    output_buffer= os.listdir(pathName) #buffer
    output_buffer=output_buffer[1:]
    totalCount=0
    file_list=[]
    for file in output_buffer:
        filename = (file[:-4])
        file_list.append(int(filename))
    #print(file_list)
    currentMax =  max(file_list)
    totalCount =  len(output_buffer) #size of list dir
    return (currentMax, totalCount)


#main function
def main():

    flag= True
    counter=1
    currentDirectory = '/Users/hannahhess/Desktop/WAVfiles' #name of current directory
    BUFFER_SIZE = 10
    

    while flag:
    
        checkbuff=check_buffer(currentDirectory)
        #print(checkbuff)
        totalCount=int(checkbuff[1])
    
        if (totalCount < BUFFER_SIZE):
            #print (totalCount)
            WAVE_FILENAME = 'WAVfiles/'+str(counter) + '.wav'  
            #print(WAVE_FILENAME)
            wavfile = sound_record(FORMAT,CHANNELS,RATE,SAMPLE_SIZE,RECORD_TIME,WAVE_FILENAME)
            #print("wav file recorded")
            #print("wave file saved to: " + currentDirectory)
            counter=counter+1 #update the counter for the file name
       
        else:  #if there is not space in the buffer
            #print("Not enough room in buffer.")
        


    #print("end")

main()













