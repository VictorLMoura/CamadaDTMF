import wave
import random
import struct
import datetime

def main():

    SAMPLE_LEN = 44100 * 2 # 2   seconds of noise, 5 minutes

    noise_output = wave.open('noise.wav', 'w')
    noise_output.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

    d1 = datetime.datetime.now()

    for i in range(0, SAMPLE_LEN):
        value = random.randint(-32767, 32767)
        packed_value = struct.pack('h', value)
        noise_output.writeframes(packed_value)
        noise_output.writeframes(packed_value)

    d2 = datetime.datetime.now()
    print (d2 - d1), "(time for writing frames)"

    noise_output.close()

    d3 = datetime.datetime.now()
    print (d3 - d2), "(time for closing the file)"
    
if __name__ == "__main__":
    main()