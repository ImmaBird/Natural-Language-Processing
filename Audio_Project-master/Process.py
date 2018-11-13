import sys
import wave
from threading import Thread

import matplotlib.pyplot as plt
import numpy as np
import pyaudio

import Audio as audio

audio.record(5)

spf = wave.open('./clip.wav', 'r')

signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')
rate = spf.getframerate()

time = np.linspace(0, len(signal)/rate, num=len(signal))

thread = Thread(target=audio.play)
thread.start()

plt.figure(1)
plt.title('Signal Wave')
plt.ylabel('Frequency')
plt.xlabel('Time')
plt.plot(time, signal)
plt.show()
