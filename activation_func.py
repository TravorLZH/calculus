#!/usr/bin/env python3
import numpy as np
from matplotlib import pyplot as plt

def relu(x):
    return np.maximum(0,x)

def sigmoid(x):
    return 1/(1+np.exp(-x))

plt.figure("Activation functions")

x=np.linspace(-5,5,100)
ax=plt.subplot(411)
ax.plot(x[0:50],np.zeros(50),"y-",label=r"$step(x)$")
ax.plot(x[50:100],np.ones(50),"y-")
ax.legend()
ax2=plt.subplot(412)
ax2.plot(x,sigmoid(x),"g-",label=r"$sigmoid(x)=\frac{1}{1+e^{-x}}$")
ax2.legend()
ax3=plt.subplot(413)
ax3.plot(x,relu(x),"r-",label=r"$relu(x)=\max(0,x)$")
ax3.legend()
ax4=plt.subplot(414)
ax4.plot(x,np.tanh(x),"b-",label=r"$\tanh(x)$")
ax4.legend()
plt.show()
