import pyaudio
import array
import math
import time
import signalTeste
import matplotlib.pyplot as plt

def main():
    user_freq = [697.0, 770.0, 852.0, 941.0,
                1209.0, 1336.0, 1477.0, 1633.0]
    user_tones = {
        '1': (user_freq[0], user_freq[4]),
        '2': (user_freq[0], user_freq[5]),
        '3': (user_freq[0], user_freq[6]),
        'A': (user_freq[0], user_freq[7]),
        '4': (user_freq[1], user_freq[4]),
        '5': (user_freq[1], user_freq[5]),
        '6': (user_freq[1], user_freq[6]),
        'B': (user_freq[1], user_freq[7]),
        '7': (user_freq[2], user_freq[4]),
        '8': (user_freq[2], user_freq[5]),
        '9': (user_freq[2], user_freq[6]),
        'C': (user_freq[2], user_freq[7]),
        '*': (user_freq[3], user_freq[4]),
        '0': (user_freq[3], user_freq[5]),
        '#': (user_freq[3], user_freq[6]),
        'D': (user_freq[3], user_freq[7]),
    }

    sr = 44100
    length = .25
    volume = .25

    p = pyaudio.PyAudio()
    stream = p.open(rate=sr, channels=1, format=pyaudio.paFloat32, output=True)

    tone_set = user_tones
    while True:
        commands = input('>>>').upper()
        for command in commands:
            try:
                tone = tone_set[command]
            except KeyError:
                print('Invalid sequence: \'{}\'. Ignoring'.format(command))
                continue

            a = stream.write(array.array('f',
                                    ((volume * math.sin(i / (tone[0] / 100.)) + volume * math.sin(i / (tone[1] / 100.)))
                                    for i in range(int(sr*length)))).tostring())


    stream.close()
    p.terminate()

if __name__ == "__main__":
    main()
