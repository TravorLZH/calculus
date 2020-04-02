#!/usr/bin/env python3
from matplotlib import pyplot as plt
import numpy as np

x=np.linspace(-20,20,1000)

plt.figure("Fourier analysis")
f1=plt.subplot(311)
f1.plot(x,np.sin(x/2),"r-",label=r"$y_1=\sin(\frac{x}{2})$")
f1.legend()
f2=plt.subplot(312)
f2.plot(x,np.sin(2*x),label=r"$y_2=\sin(2x)$")
f2.legend()
f3=plt.subplot(313)
f3.plot(x,np.sin(x/2)+np.sin(2*x),"g-",label="$y=y_1+y_2$")
f3.legend()
plt.show()
