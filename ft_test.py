#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

def rect(t):
    return np.where(abs(t)<=0.5,1,0)

ts=np.linspace(-20,20,10000)
samples=rect(ts)
N=len(samples)
freq=np.fft.fftfreq(N)
ft=np.fft.fft(samples)/N

plt.figure("Fourier transform example")
ax=plt.subplot(211)
ax.set_title("Time domain")
ax.plot(ts,samples)
ax2=plt.subplot(212)
ax2.set_title("Frequency domain")
ax2.plot(freq,ft.real)
plt.legend()
plt.show()
