# -*- coding: utf-8 -*-
#

import numpy as np
import matplotlib as mpl
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

N = 256
x = ( range( N ) / np.double(N) * 2 ) * np.pi
y = ( range( N ) / np.double(N) * 2 ) * np.pi

X, Y = np.meshgrid( x, y )

kMax = 5

for i in range(kMax):
    for j in range(kMax):
        cnt = i*kMax + j + 1
        plt.subplot( kMax, kMax, cnt )
#        Z = np.cos( i * Y  + j * X )
        Z = np.sin( i * Y  + j * X )
        plt.imshow( Z, cmap=cm.coolwarm )
        plt.xticks(())
        plt.yticks(())

plt.show()
