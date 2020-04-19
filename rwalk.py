#!/usr/bin/env python3
import random
from math import pi,sin,cos,exp,log
import matplotlib.pyplot as plt
from matplotlib import animation

xpos=[5]
ypos=[0]
xpos2=[-5]
ypos2=[0]

f=plt.figure()

ax=plt.gca()
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)

def alpha_exp(t,n):
    r=log(4)/n
    return exp(r*(t-n))

def alpha_lin(t,n):
    return t/n

def next_loc(x0,y0):
    theta=random.random()*2*pi
    r=random.random()
    x=x0+r*cos(theta)
    y=y0+r*sin(theta)
    if x>10: x=10
    elif x<-10: x=-10
    if y>10: y=10
    elif y<-10: y=-10
    return (x,y)

def walk(i):
    n=len(xpos)
    k=20
    ax.cla()
    ax.set_title("Random walk: %d steps" % i)
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)
    if i!=0:
        x,y=next_loc(xpos[-1],ypos[-1])
        xpos.append(x)
        ypos.append(y)
        x,y=next_loc(xpos2[-1],ypos2[-1])
        xpos2.append(x)
        ypos2.append(y)
        for t in range(n-k,n):
            ax.plot(xpos[t:t+2],ypos[t:t+2],c="blue",alpha=alpha_lin(t+k-n,k),
                    zorder=t)
            ax.plot(xpos2[t:t+2],ypos2[t:t+2],c="red",alpha=alpha_lin(t+k-n,k),
                    zorder=t)
    ax.scatter(xpos[-1],ypos[-1],c="k",zorder=n)
    ax.scatter(xpos2[-1],ypos2[-1],c="green",zorder=n)

anim=animation.FuncAnimation(fig=f,func=walk,frames=400,interval=100)

anim.save("rwalk.mp4")
