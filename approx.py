#!/usr/bin/env python3
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

mpl.rcParams["text.usetex"]=True
mpl.rcParams["text.latex.preamble"]=[r"\usepackage{amsmath}"]

stepsize=0.5

# All first-order ODE problem can be turned in to the following:
# y'=f(x,y) and y(a)=c
#
# Suppose we turn this into a discrete problem:
# [y(x+h)-y(x)]/h=f(x,y)
# So that:
# y(x+h)=y(x)+h*f(x,y)
# Since we have the initial condition y(a)=c, we can approximate anything

# In this example, let's consider the following equation:
# y'=2*y and y(0)=2
# Obviously the solution to this problem is y=2*exp(x)

def diffeqn(x,y):
    return 2*y

# The analytical solution to the differential equation
def analytical_f(x):
    return 2*np.exp(2*x)

# The two-degree Taylor expansion of the function
def taylor_f(x):
    return 2*(1+2*x+2*x**2)

# The numberical approximation by the computer using Euler's method
def numerical_f(x):
    y=2
    a=0
    s=1
    if x<0: s=-1
    while s*a<s*x:
        a+=s*stepsize
        y+=s*stepsize*diffeqn(a,y)
    return y

lowb=-1
upb=1

x=np.arange(lowb,upb+0.001,0.001)
xa=np.arange(lowb,upb+stepsize,stepsize)

diffeqn_tex=r"\begin{cases}{dy\over dx}=2y \\ y(0)=2\end{cases}"


plt.figure("Euler's method")
plt.title("Solve the differential equation $%s$" % diffeqn_tex)
plt.plot(x,[analytical_f(n) for n in x],"k-",
    label="Analytical solution: $y=2e^{2x}$")
plt.plot(x,[taylor_f(n) for n in x],"b-",label="Two-degree Taylor polynomial")
plt.plot(xa,[numerical_f(n) for n in xa],"r-",label="Numerical approximation")
plt.legend()
plt.show()
