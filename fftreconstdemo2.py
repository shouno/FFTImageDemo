# -*- coding: utf-8 -*-
#

import numpy as np
import scipy as sp
from scipy import misc
from matplotlib import cm
import matplotlib.pylab as plt


def scnline( n ):
    ret = []
    for i in range(n+1):
        ret.append( (i,n-i) )
    for i in range(n+1):
        ret.append( (-i,n-i) )
            
    return ret

def scnseq( n ):
    ret = []
    for i in range(n+1):
        ret += scnline( i )
    return ret

l = misc.lena()
N = 64
slena = misc.imresize( l, (N, N), interp='bilinear' ) / 255.

SLENA = np.fft.fft2( slena )

flt = np.zeros( (N, N) )


RecRange = 20
RecSeq = scnseq( RecRange )

for p in (RecSeq):

    plt.clf()
    plt.subplot( 2, 2, 1 )
    plt.imshow( slena, interpolation='nearest' )
    plt.title( 'Original' )
    plt.xticks(())
    plt.yticks(())
    
    ppx, ppy = p[0], p[1]

    cur = np.zeros((N,N))
    cur[ppy,ppx] = 1
    cur[-ppy,-ppx] = 1

    plt.subplot( 2, 2, 2 )
    baseimg = np.fft.ifft2( SLENA * cur ).real
    plt.imshow( baseimg, cmap=cm.coolwarm )
    plt.xticks( () )
    plt.yticks( () )
    plt.title( 'Base Component' )

    plt.subplot( 2, 2, 3 )    
    recimg = np.fft.ifft2( SLENA * flt ).real
    plt.imshow( recimg )
    plt.xticks( () )
    plt.yticks( () )
    plt.title( 'Reconstruct' )

    plt.subplot( 2, 2, 4 )
    flt[ppy, ppx] = 1
    flt[-ppy, -ppx] = 1
    plt.imshow( np.fft.fftshift(flt), interpolation='nearest' )
    plt.title( 'Recon. Pos.' )

    plt.pause(0.001)
