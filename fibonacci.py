#!/usr/bin/env python3
import numpy as np

m=np.array([[1,1],[1,0]])

v=np.array([1,1])

for i in range(10):
    print(v[1])
    v=np.dot(m,v)
