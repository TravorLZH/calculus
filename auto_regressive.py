#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import time

# Auto-regressive model example
#
# X[t]=a*X[t-1]+b*X[t-2]+c*X[t-3]+...+w[t]
#
# where `w' denotes white noise

# Example: AR(2)
#
# X[t]=a*X[t-1]+b*X[t-2]+w[t]

niter=400
X_range=range(0,niter)
X=[1]
w=[]
w.append(np.random.normal(scale=0.5))
a=0.85

np.random.seed(int(time.time()))

for i in range(1,niter):
    w.append(np.random.normal(scale=0.5))
    X.append(a*X[-1]+w[-1])

win_size=10
MA_range=range(0,niter,win_size)
MA=[]

for i in MA_range:
    MA.append(np.mean(X[i:i+win_size]))

# Linear interpolate moving average
MA_int=np.interp(X_range,MA_range,MA)

plt.figure("AR(1) model")
ax=plt.subplot(211)
ax.set_title("AR(1)'s result after %d iterations with a=%.2f" \
        % (niter,a))
ax.plot(X_range,X,".-",label=r"$X_t=a\cdot X_{t-1}+w_t$")
ax.plot(MA_range,MA,".-",
        label="Moving Average with window size %d" % win_size)
ax.legend()


ax2=plt.subplot(212)
ax2.set_title("Noise anaysis")
ax2.plot(X_range,w,"r.-",label="$w_t$")
ax2.legend()
plt.show()

print("Noise: mean=%.5f, std=%.5f" % (np.mean(w),np.std(w)))
