#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

interval=0.5
nsamples=20
samples=[]

def signal(t):
    return np.sin(t)+np.sin(2*t)

for i in range(nsamples):
    samples.append(signal(interval*i))

def restored(t):
    y=0
    for i in range(nsamples):
        y+=samples[i]*np.sinc(t/interval-i)
    return y

x=np.linspace(0,19*interval,1000)

plt.figure("Restored vs. original")
ax=plt.subplot(121)
ax.set_xlabel("t")
plt.plot(x,signal(x),label=r"original signal: $\sin(t)+\sin(2t)$")
plt.scatter(np.arange(0,20*interval,interval),samples,color='red',
    label="samples",zorder=3)
plt.legend()
ax=plt.subplot(122)
ax.set_xlabel("t")
plt.plot(x,restored(x),color='orange',label="restored signal")
plt.scatter(np.arange(0,20*interval,interval),samples,color='red',
    label="samples",zorder=3)
plt.legend()
plt.show()
