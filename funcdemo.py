# -*- coding: utf-8 -*-
#

import numpy as np
import scipy as sp
import matplotlib.pylab as plt

N = 256
x = range(N) / np.double(N) * 2 - 1
# y = 0.4 * np.abs(x-0.4) + 0.5 * (x+0.4)**2
# y = x**2
# y = 8 * (x-0.4)**2 * (x+0.4)**2
y = x
Y = np.fft.fft(y)


ytop, ybtm = 1.1, -1.1
# ytop, ybtm = 1.2, -1.2
ctop, cbtm = 1.5, -1.5
# ctop, cbtm  = 0.5, -0.5

MaxCutoff = 32

ycomp = np.zeros((MaxCutoff, N))
ydash = np.zeros(N)

cbarx = range(MaxCutoff)
cbary = np.zeros(MaxCutoff)


plt.pause(0.5)

plt.subplot(2, 2, 1)
plt.plot(x, y, linewidth=2)
plt.grid()
plt.title("Original Signal")
plt.ylim(ybtm, ytop)

plt.subplot(2, 2, 2)
plt.title("Component")

plt.subplot(2, 2, 3)
plt.title("Sythesis")

plt.subplot(2, 2, 4)
plt.title("Component Strength")

plt.pause(2)


for cidx in range(MaxCutoff):
    plt.clf()
    plt.subplot(2, 2, 1)
    plt.plot(x, y, linewidth=2)
    plt.grid()
    plt.title("Original Signal")
    plt.ylim(ybtm, ytop)

    flt = np.zeros(N)
    flt[cidx] = 1
    flt[-cidx] = 1
    ycomp[cidx, :] = np.fft.ifft(Y * flt).real
    ydash += ycomp[cidx, :]
    plt.subplot(2, 2, 2)
    for i in range(cidx + 1):
        plt.plot(x, ycomp[i])
    plt.title("Component")
    plt.grid()
    plt.ylim(cbtm, ctop)

    plt.subplot(2, 2, 3)
    plt.plot(x, ydash, "r", linewidth=2)
    plt.title("Sythesis")
    plt.grid()
    plt.ylim(ybtm, ytop)

    plt.subplot(2, 2, 4)
    cbary[cidx] = np.abs(Y[cidx])
    plt.bar(cbarx, cbary)

    plt.title("Component Strength")

    plt.pause(0.75)

plt.show()
input()
