#!/usr/bin/env python3
import numpy as np
from matplotlib import pyplot as plt

def plot_vector(vec,lbl):
    assert(len(vec)==2) # Must be 2 dimensional
    x=[0,vec[0]]
    y=[0,vec[1]]
    plt.plot(x,y,label=lbl)

fig=plt.figure("Put directional vectors wherever you want")

plt.xlim(-5,5)
plt.ylim(-5,5)
ax=plt.gca()
ax.spines["top"].set_color("none")
ax.spines["right"].set_color("none")
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
ax.spines["left"].set_position(("data",0))
ax.spines["bottom"].set_position(("data",0))
ax.set_aspect("equal",adjustable="box")

vec1=np.array([1,2])
vec2=np.array([-4,2])
vec3=vec1+vec2
vec4=vec1*vec2

plot_vector(vec1,"vec1")
plot_vector(vec2,"vec2")
plot_vector(vec3,"vec3")
plot_vector(vec4,"vec4")

plt.legend()
plt.show()
