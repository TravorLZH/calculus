#!/usr/bin/env python3
import numpy as np
from matplotlib import pyplot as plt
import sys

depth=5
argc=len(sys.argv)
if argc>=2:
    depth=int(sys.argv[1])
    print("Depth: %d" % depth)
else:
    print("Insufficient arguments, setting depth to 5")

def p(x):
    y=np.zeros_like(x)
    for i in range(0,depth):
        np.add(y,(-1)**i*x**(2*i+1)/np.math.factorial(2*i+1),out=y,
                casting="unsafe")
    return y

xs=np.linspace(-10,10,200)
ys=np.sin(xs)
y2s=p(xs)

plt.figure("Taylor Expansion of function")
plt.title("Taylor Expansion of $sin(x)$ at $x=0$")
plt.xlim(-10,10)
plt.ylim(-10,10)

plt.plot(xs,ys,"r--",label="$sin(x)$")
plt.plot(xs,y2s,"b-",
        label="$\\sum_{n=1}^{%d}\\frac{(-1)^nx^{(2n+1)}}{(2n+1)!}$" % depth)

plt.legend()
plt.show()
