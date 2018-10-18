from signalTeste import *
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import sys
import pyaudio
import array
import math
import time
import signalTeste
import keyboard
import click
import matplotlib.pyplot as plt

sm = signalMeu()

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

    fs = 44100

    tone_set = user_tones
    while True:
        key = click.getchar()
        if key in user_tones:
            tone = tone_set[key]
            tempo1, sinal1 = sm.generateSin(tone[0], 1, 1, fs)
            tempo2, sinal2 = sm.generateSin(tone[1], 1, 1, fs)
            sinalRes = np.add(sinal1, sinal2)
            print(sinalRes)
            sd.play(sinalRes, fs)

        else:
            print('Invalid sequence: Ignoring')
            continue



    # stream.close()
    # p.terminate()

if __name__ == "__main__":
    main()
