#!/usr/bin/env python3
import numpy as np
from matplotlib import pyplot as plt

xs=np.arange(-2.5,2.5,1e-5)

plt.figure("Gaussian's integral")
plt.title(r"$\int_{-\infty}^\infty e^{-x^2}dx$")
plt.ylim(0,2)
plt.plot(xs,np.exp(-np.square(xs)),"r-",label="$y=e^{-x^2}$")
plt.legend()
plt.show()
