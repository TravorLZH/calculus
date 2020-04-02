#!/usr/bin/env python3
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x=np.linspace(-10,10,1000)
y=x[:]
x,y=np.meshgrid(x,y)
print(x.shape,y.shape)

fig=plt.figure("3D Surface demo")
ax=fig.gca(projection="3d")

fig.colorbar(ax.plot_surface(x,y,np.sin(x)+np.sin(y)),shrink=0.5,aspect=5)

plt.show()
