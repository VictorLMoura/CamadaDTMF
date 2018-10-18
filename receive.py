from signalTeste import *
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import time
import signalTeste
import click
import pickle
import peakutils

class receiver:
    def __init__(self):
        self.init = 0

        self.sm = signalMeu()
        self.frequencia = 44100
        self.recorded = None

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

        self.matrix_frequencias =  {"1":(697,1209), "2":(697,1336), "3":(697,1209), "4":(770,1209), "5":(770,1336), "6":(770,1477), "7":(852,1209), "8":(852,1336), "9":(852,1477), "*":(941,1209), "0":(941,1336), "#":(941,1477)}
        self.time = 0


    def record(self):
        duration = 2
        recording = sd.rec(int(duration * self.frequencia), samplerate = self.frequencia, channels=1)
        sd.wait()
        self.recorded = recording[:,0]
        return recording[:,0]

    def findPeaks(self):
        recording_fft = self.sm.calcFFT(self.record(), self.frequencia)
        indexes = peakutils.indexes(recording_fft[1], thres=0.5, min_dist=10)
        return indexes

    def plotFFT2(self):
        recording_fft = self.sm.calcFFT(self.record, self.frequencia)
        #recording_fft = self.sig.calcFFT(self.record(), self.frequencia)
        plt.figure()
        plt.plot(recording_fft[0], np.abs(recording_fft[1]))
        plt.title("Fourier")
        plt.show()

    def findKeys(self):
        peaks = self.findPeaks()
        possible_frequency = [697, 1209, 1336, 770, 852, 1477, 941]

        received_frequency = []
        for peak in peaks:
            for frequency in possible_frequency:
                if abs(peak - frequency) < 50:
                    received_frequency.append(frequency)

            #for key in self.matrix_frequencias.keys():
            #    if

    def plotHarmonics(self):
        frequencies = self.findPeaks()
        for frequency in frequencies:
            senoid = self.sm.generateSin(frequency, 1, 2, self.frequencia)
            plt.figure()
            plt.title("Gráfico para o harmonico de {} Hz".format(frequency))
            plt.plot(senoid[0][:2000], senoid[1][:2000])
        plt.show()

    def main(self):
        self.plotFFT2()
        self.plotHarmonics()

if __name__ == "__main__":
    rs = receiver()
    rs.main()
