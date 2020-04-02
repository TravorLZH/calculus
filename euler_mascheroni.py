#!/usr/bin/env python3
from math import log

n=1000
s=0

for i in range(1,n+1):
    s+=1/i

print(s-log(n))
