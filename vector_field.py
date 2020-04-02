#!/usr/bin/env python3
from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams["text.usetex"]=True
mpl.rcParams["text.latex.preamble"]=[r"\usepackage{amsmath}"]

def normalize(vec):
    magn=np.linalg.norm(vec,axis=0)
    return vec/np.array([magn,magn])

def f(x,y):
    vx=-y*np.sin(x)
    vy=x
    return np.array([vx,vy])

def get_vec(x,y):
    vec=f(x,y)
    print(vec.shape)
    return normalize(vec)

xs=np.linspace(-3,3,20)
ys=np.linspace(-3,3,20)

x,y=[elm.reshape(elm.size) for elm in np.meshgrid(xs,ys)]

vecs=get_vec(x,y)

plt.figure("Vector field")
plt.title(r"Vector field $\nabla=\begin{bmatrix}-y\sin(y)\\x\end{bmatrix}$")
ax=plt.gca()
ax.spines["top"].set_color("none")
ax.spines["right"].set_color("none")
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
ax.spines["left"].set_position(("data",0))
ax.spines["bottom"].set_position(("data",0))
ax.set_aspect("equal",adjustable="box")
plt.quiver(x,y,vecs[0],vecs[1],angles='xy')
plt.show()
