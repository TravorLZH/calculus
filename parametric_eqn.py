#!/usr/bin/env python3
from matplotlib import pyplot as plt
import numpy as np
import math

ts=np.linspace(-10,10,100)

def f(t):
    # Parametric equations for X and Y
    x=-np.cos(t)
    y=np.sin(t)
    return (x,y)    # The vector

xs,ys=f(ts)

plt.figure("Vector-valued function")
plt.title("Vector-valued function")
plt.xlim(-3,3)
plt.ylim(-3,3)
ax=plt.gca()
ax.spines["top"].set_color("none")
ax.spines["right"].set_color("none")
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
ax.spines["left"].set_position(("data",0))
ax.spines["bottom"].set_position(("data",0))
ax.set_aspect("equal",adjustable="box")
plt.plot(xs,ys,
        label="$x=\\cos(\\theta)$ and $y=\\sin(\\theta)$")

plt.legend()
plt.show()
