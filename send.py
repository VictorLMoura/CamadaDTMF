from signalTeste import *
import numpy as np
import sounddevice as sd
import time
import signalTeste
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
    inicio = 30000
    fim = 72000

    tone_set = user_tones
    while True:
        key = click.getchar()
        if key in user_tones:
            tone = tone_set[key]
            tempo, sinal1 = sm.generateSin(tone[0], 1, 1, fs)
            tempo, sinal2 = sm.generateSin(tone[1], 1, 1, fs)

            sinalRes = np.add(sinal1, sinal2)
            sinalmax = max(sinalRes)
            sinalmin = min(sinalRes)

            sinalNorm = []
            for i in range(len(sinalRes-1)):
                x = (sinalRes[i] - sinalmin)/(sinalmax - sinalmin)
                sinalNorm.append(x)

            sinalRes_filter = sm.low_pass_filter(sinalNorm)
            #sinalRes_filter2 = sm.low_pass_filter2(sinalNorm)
            plt.plot(tempo[:1000], sinalRes[:1000])
            plt.plot(tempo[:1000], sinalRes_filter[:1000])
            #plt.plot(tempo[:1000], sinalRes_filter2[:1000])
            plt.plot(tempo[:1000], sinalNorm[:1000])

            sm.plotFFT(sinalRes, fs)
            plt.show()
            
            sm.am_modulation(sinalRes_filter[:4000], sinalNorm[:4000])

        elif key == 'k':
            '''
            Arquivo wav
            '''
            duration = 2
            myrecording = sd.rec(int(duration * fs), samplerate = fs, channels=1)
            sd.wait()
            myrecord = myrecording[:,0]

            tempo, sinal1 = sm.generateSin(14000, 1, 1, 2*fs)
            sinal2 = np.multiply(sinal1,myrecord)
            
            sinalmax = max(sinal1)
            sinalmin = min(sinal1)

            sinalNorm = []
            for i in range(len(sinal2-1)):
                x = (sinal2[i] - sinalmin)/(sinalmax - sinalmin)
                sinalNorm.append(x)

            sinalRes_filter = sm.low_pass_filter(sinalNorm)
            
            sinalRes_filter = sm.low_pass_filter(sinalNorm)
            #sinalRes_filter2 = sm.low_pass_filter2(sinalNorm)
            plt.plot(tempo[inicio:fim], sinal2[inicio:fim])
            #plt.plot(tempo[inicio:fim], sinalRes_filter[inicio:fim])
            #plt.plot(tempo[inicio:fim], sinalRes_filter2[inicio:fim])
            plt.plot(tempo[inicio:fim], sinalNorm[inicio:fim])

            sm.plotFFT(sinalNorm, fs)
            plt.show()
            
            sm.am_modulation(sinalRes_filter[:2*fs], sinalNorm[:6*fs])



        else:
            print('Invalid sequence ', key, ': Ignoring')
            continue



    # stream.close()
    # p.terminate()

if __name__ == "__main__":
    main()
