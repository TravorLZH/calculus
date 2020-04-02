#!/usr/bin/env python3
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams["text.usetex"]=True
mpl.rcParams["text.latex.preamble"]=[r"\usepackage{amsmath}"]

def get_next(x):
    if x%2:
        return 3*x+1
    else:
        return x/2

n=int(input("# of recursions="))

x0=int(input("x0="))

x=[x0]

for i in range(n):
    x.append(get_next(x[-1]))

plt.figure("Collatz Conjecture")
plt.title("Collatz Conjecture with %d recursions" % n)
plt.xlabel("$n$")
plt.ylabel("$a_n$")
plt.plot(range(n+1),x,"m*-",label=r"$a_{n+1}=\begin{cases}3a_n+1 &" \
        r"a_n\text{ is odd}\\a_n\div2 & a_n\text{ is even}\end{cases}$")
plt.legend()
plt.show()
