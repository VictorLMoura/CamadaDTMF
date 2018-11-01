from signalTeste import *
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import time
import pickle
import peakutils
import keyboard

sm = signalMeu()
fs = 44100

user_freq = [697.0, 770.0, 852.0, 941.0,
            1209.0, 1336.0, 1477.0, 1633.0]
user_tones = {
    '1': (user_freq[0] + user_freq[4]),
    '2': (user_freq[0] + user_freq[5]),
    '3': (user_freq[0] + user_freq[6]),
    'A': (user_freq[0] + user_freq[7]),
    '4': (user_freq[1] + user_freq[4]),
    '5': (user_freq[1] + user_freq[5]),
    '6': (user_freq[1] + user_freq[6]),
    'B': (user_freq[1] + user_freq[7]),
    '7': (user_freq[2] + user_freq[4]),
    '8': (user_freq[2] + user_freq[5]),
    '9': (user_freq[2] + user_freq[6]),
    'C': (user_freq[2] + user_freq[7]),
    '*': (user_freq[3] + user_freq[4]),
    '0': (user_freq[3] + user_freq[5]),
    '#': (user_freq[3] + user_freq[6]),
    'D': (user_freq[3] + user_freq[7]),
}

def main():

    duration = 2
    myrecording = sd.rec(int(duration * fs), samplerate = fs, channels=1)
    sd.wait()
    myrecord = myrecording[:,0]

    recording_fft = sm.calcFFT(myrecord, fs)
    indexes = peakutils.indexes(recording_fft[1], thres=100, min_dist=100, thres_abs=True)
    return recording_fft[0][indexes], recording_fft[1][indexes], myrecord

def plotFFT2(peaks, record):
    recording_fft = sm.calcFFT(record, fs)
    plt.figure()
    plt.plot(recording_fft[0], np.abs(recording_fft[1]))
    plt.title("Fourier")
    plt.show()

def findKeys(peaks):
    possible_frequency = [697.0, 770.0, 852.0, 941.0, 1209.0, 1336.0, 1477.0, 1633.0]

    received_frequency = []
    for peak in peaks:
        if peak > 650 and peak < 1700 and len(received_frequency) <= 1:
            for frequency in possible_frequency:
                if abs(peak - frequency) < 5:
                    received_frequency.append(frequency)

    total = sum(received_frequency)
    if total == 1906:
        return "Tecla 1"
    if total == 2033:
        return "Tecla 2"
    if total == 2174:
        return "Tecla 3"
    if total == 0:
        return "Tecla A"
    if total == 1979:
        return "Tecla 4"
    if total == 2106:
        return "Tecla 5"
    if total == 2247:
        return "Tecla 6"
    if total == 0:
        return "Tecla B"
    if total == 2061:
        return "Tecla 7"
    if total == 2188:
        return "Tecla 8"
    if total == 2329:
        return "Tecla 9"
    if total == 0:
        return "Tecla C"
    if total == 0:
        return "Tecla *"
    if total == 2277:
        return "Tecla 0"
    if total == 0:
        return "Tecla #"
    if total == 0:
        return "Tecla D"
    else:
        return total

def plotHarmonics(peaks):
    plt.figure()
    plt.plot(np.arange(0,2,1/44100)[:5000], peaks[:5000])
    plt.show()

freqs, amps, myrecord = main()
plotFFT2(freqs,myrecord)
print(findKeys(freqs))
plotHarmonics(myrecord)
plt.plot(np.arange(0,2,1/44100)[:1000], myrecord[:1000])
plt.show()

tempo, sinal1 = sm.generateSin(14000, 1, 1, 2*fs)
sinal2 = np.multiply(sinal1,myrecord)
sinalRes_filter = sm.low_pass_filter(sinal2)
plotFFT2(freqs,myrecord)

sm.am_demodulation(sinalRes_filter[:2*fs], myrecord)
