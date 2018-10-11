import wave
import random
import struct
import datetime

def main():

    SAMPLE_LEN = 44100 * 2 # 300 seconds of noise, 5 minutes

    noise_output = wave.open('noise.wav', 'w')
    noise_output.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

    values = []

    for i in range(0, SAMPLE_LEN):
        value = random.randint(-32767, 32767)
        packed_value = struct.pack('h', value)
        values.append(packed_value)
        values.append(packed_value)

    value_str = ''.join(values)
    noise_output.writeframes(value_str)

    noise_output.close()
    
if __name__ == "__main__":
    main()