#!/usr/bin/env python3
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

def func(t):
    return (t*np.cos(2*np.pi*t),t*np.sin(2*np.pi*t))

plt.figure("Plot parametric curve in 3D coordinates")

ax=plt.gca(projection="3d",proj_type="ortho")

t=np.linspace(-2,2,100)

ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
ax.set_zlim(-5,5)
ax.plot(t,func(t)[0],func(t)[1],label="$f(t)=(t\\cdot\\cos(2\\pi t),t\\cdot\\cos(2\\pi t))$")

plt.legend()
plt.show()
