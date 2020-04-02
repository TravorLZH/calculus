#!/usr/bin/env python3
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

def my_func(z):
    return func1(z)+func2(z)

def func1(z):
    return np.exp(z*1j)

def func2(z):
    return np.exp(z*2j)

def plot_complex(ax,func,lbl,border=5):
    z=np.linspace(-border,border,1000)
    out=func(z)
    ax.plot(out.real,out.imag,z,label="$%s$" % lbl)
    ax.plot(out.real,-border*np.ones_like(z),z,"g-")
    ax.plot(border*np.ones_like(z),out.imag,z,"r-")
    ax.set_xlabel("real")
    ax.set_ylabel("imaginary")
    ax.set_zlabel("input")
    ax.set_xlim(-border,border)
    ax.set_ylim(-border,border)
    ax.set_zlim(-border,border)
    ax.grid(False)
    ax.legend()
    return ax


lbl1="e^{ix}"
lbl2="e^{2ix}"

fig=plt.figure("Complex functions",figsize=(3*4,4))

axes=[]
pairs=[]

axes.append(fig.add_subplot(1,3,1,projection="3d",proj_type="ortho"))
plot_complex(axes[0],my_func,"f(z)=%s+%s" % (lbl1,lbl2))

axes.append(fig.add_subplot(1,3,2,projection="3d",proj_type="ortho"))
plot_complex(axes[1],func1,lbl1)

axes.append(fig.add_subplot(1,3,3,projection="3d",proj_type="ortho"))
plot_complex(axes[2],func2,lbl2)

for ax in axes:
    pairs.append([ax.azim,ax.elev])

def mouse_move(event):
    for (azim,elev),ax in zip(pairs,axes):
        if azim!=ax.azim or elev!=ax.elev:
            azim=ax.azim
            elev=ax.elev
            break
    for i,ax in enumerate(axes):
        pairs[i]=[azim,elev]
        ax.azim,ax.elev=azim,elev

fig.canvas.mpl_connect("motion_notify_event",mouse_move)

plt.show()
