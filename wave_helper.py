import wave

# wave_helper is a wrapper around built-in wave module developed for project CT sensor
# Performance of this module is not tested and guaranteed for any other purposes

class Struct(object):
    pass

def readSound(in_path):
    f = wave.open(in_path, 'rb')
    n = f.getnframes()
    data = Struct()
    data.bytes = f.readframes(n)
    data.prms = f.getparams()
    return data

def writeSound(out_path, bytes, prms):
    with wave.open(out_path,'w') as outfile:
        outfile.setparams(prms)
        outfile.writeframes(bytes)
    outfile.close()
    return

if __name__ == '__main__':
    # Testing goes into here
    data = readSound("test.wav")
    writeSound("test_out.wav", data.bytes, data.prms)
