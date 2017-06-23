import wave
from myStruct import *

# wave_helper is a wrapper around built-in wave module developed for project CT sensor
# Performance of this module is not tested and guaranteed for any other purposes

def read_sound(in_path):
    f = wave.open(in_path, 'rb')
    n = f.getnframes()
    data = myStruct()
    data.bytes = f.readframes(n)
    data.prmts = f.getparams()
    return data

def write_sound(out_path, data):
    bytes = data.bytes
    prmts  = data.prmts
    with wave.open(out_path,'w') as outfile:
        outfile.setparams(prmts)
        outfile.writeframes(bytes)
    outfile.close()
    return

if __name__ == '__main__':
    # Testing goes into here
    data = read_sound("test.wav")
    write_sound("test_out.wav", data.bytes, data.prmts)
    print ("Done")
