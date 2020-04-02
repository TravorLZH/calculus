#!/usr/bin/env python3
import numpy as np
import cv2
import sys

maxiter=30

argc=len(sys.argv)
if argc<2:
    print("Usage: %s c [maxiter]" % sys.argv[0])
    sys.exit(-1)

c=float(sys.argv[1])

if argc>=3:
    maxiter=int(sys.argv[2])

r=(1+np.sqrt(1+4*abs(c)))/2

def f(z):
    return z**2+c

def check_f(z):
    for i in range(maxiter):
        if abs(z)>r:
            return (1-i/maxiter)*0xFF
        z=f(z)
    return 0

dz=0.01

re=np.arange(-3,3,dz)
im=np.flip(np.arange(-3,3,dz))

height=im.shape[0]
width=re.shape[0]

image=np.zeros((height,width),np.uint8)

for i in range(height):
    for j in range(width):
        image[i][j]=check_f(re[j]+im[i]*1j)

#cv2.imshow("Julia set (c=%.2f, maxiter=%d)" % (c,maxiter),image)
#cv2.waitKey(0)
cv2.imwrite("julia.png",image)
