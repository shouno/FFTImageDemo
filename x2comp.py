# -*- coding: utf-8 -*-
#

import numpy as np
import scipy as sp
import matplotlib.pylab as plt

N = 256
x = range( N ) / np.double(N) * 2 - 1
#y = np.abs(x) + (x-0.5)**2
#y = x**2
#y = 8 * (x-0.4)**2 * (x+0.4)**2 
y = x
Y = np.fft.fft( y )

MaxCutoff = 32

ycomp = np.zeros( (MaxCutoff, N) )
ydash = np.zeros( N )

cbarx = range(MaxCutoff)
cbary = np.zeros( MaxCutoff )



for cidx in range(MaxCutoff):

    plt.clf()
    plt.subplot( 2, 2, 1 )
    plt.plot( x, y, linewidth=2 )
    plt.grid()
    plt.title( 'Original Signal' )
    plt.ylim( -0.2, 1.0 )


    flt = np.zeros(N)
    flt[cidx] = 1
    flt[-cidx] = 1
    ycomp[cidx,:] = np.fft.ifft( Y * flt ).real
    ydash += ycomp[cidx,:]
    plt.subplot( 2, 2, 2 )
    for i in range(cidx+1):
        plt.plot( x, ycomp[i] )
    plt.title( 'Component' )
    plt.grid()
    plt.ylim( -1.5, 1.5 )

    plt.subplot( 2, 2, 3 )
    plt.plot( x, ydash, 'r', linewidth=2 )
    plt.title( 'Sythesis' )
    plt.grid()
    plt.ylim( -0.2, 1.0 )

    plt.subplot( 2, 2, 4 )
    cbary[cidx] = np.abs( Y[cidx] )
    plt.bar( cbarx, cbary )
    plt.title( 'Component Strength' )
    



    plt.pause( 0.5 )

plt.show()
