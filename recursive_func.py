#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

def func(x):
    return abs(2*x-100)

c=0

n=int(input("# of recursions: "))

x0=int(input("x0="))

plt.figure("Recursive function result")

plt.title("%d of recursions $a_n+1=|2a_n-100|$ with $a_0=%d$" % (n,x0))

ax=plt.gca()
ax.set_xlim(0,n)
ax.set_ylim(0,100)

xs=range(0,n+1)
ys=[x0]

for i in range(1,n+1):
    ys.append(func(ys[i-1]))

ax.plot(xs,ys,"r*-",label="$a_n$")
plt.legend()
plt.show()
