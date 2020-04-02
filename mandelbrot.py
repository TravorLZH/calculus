#!/usr/bin/env python3
import numpy as np
import cv2

dz=0.0025
maxiter=20

def check(c):
    z=0
    for i in range(maxiter):
        if abs(z)>2:
            return 0xFF*(i/maxiter)
        z=z**2+c
    return 0xFF

re=np.arange(-2.75,1.5,dz)
im=np.flip(np.arange(-1.5,1.5,dz))

height=im.shape[0]
width=re.shape[0]

image=np.zeros((height,width),np.uint8)

for i in range(height):
    for j in range(width):
        image[i][j]=check(re[j]+im[i]*1j)

#cv2.imshow("Mandelbrot set",image)
#cv2.waitKey(0)

cv2.imwrite("mandelbrot.png",image)
