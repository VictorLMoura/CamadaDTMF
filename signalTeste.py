
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window
from scipy import signal



class signalMeu:
    def __init__(self):
        self.init = 0

    def generateSin(self, freq, amplitude, time, fs):
        n = time*fs
        x = np.linspace(0.0, time, n)
        s = amplitude*np.sin(freq*x*2*np.pi)
        return (x, s)

    def calcFFT(self, signal, fs):
        # https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html
        N  = len(signal)
        W = window.hamming(N)
        T  = 1/fs
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
        yf = fft(signal*W)
        return(xf, np.abs(yf[0:N//2]))

    def plotFFT(self, signal, fs):
        x,y = self.calcFFT(signal, fs)
        plt.figure()
        plt.plot(x, np.abs(y))
        plt.title('Fourier')

    def low_pass_filter(self, data):
        fc = 0. #Cutoff frequencia, 0.1*44100
        b = 0.08
        N = int(np.ceil((4 / b))) #Deve ser um numero impar
        if not N % 2: N += 1
        n = np.arange(N)
        
        sinc_func = np.sinc(2 * fc * (n - (N - 1) / 2.))
        window = 0.42 - 0.5 * np.cos(2 * np.pi * n / (N - 1)) + 0.08 * np.cos(4 * np.pi * n / (N - 1))
        sinc_func = sinc_func * window
        sinc_func = sinc_func / np.sum(sinc_func)

        new_signal = np.convolve(data, sinc_func)
        return new_signal

    def low_pass_filter2(self,data):
        samplerate = 44100
        nyq_rate = samplerate/2
        width = 5.0/nyq_rate
        ripple_db = 60.0 #dB
        N , beta = signal.kaiserord(ripple_db, width)
        cutoff_hz = 4000.0
        taps = signal.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
        yFiltrado = signal.lfilter(taps, 1.0, data)
        return yFiltrado

    def am_modulation(self,portadora, sinalNorm):
        sinal = np.multiply(portadora,sinalNorm)
        sd.play(sinal, 44100)

    def am_demodulation(self, portadora, myrecord):
        sinal = np.multiply(portadora,myrecord)
        sd.play(sinal, 44100)
        return sinal
