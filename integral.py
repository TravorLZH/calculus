#!/usr/bin/env python3
import numpy as np

def integral(ifrom,ito,func,dx=1e-9):
    x=np.arange(ifrom,ito,dx)
    dy=func(x)*dx
    return np.sum(dy)

def f(x):
    return np.sin(x)

if __name__=="__main__":
    predict=integral(0,10,f)
