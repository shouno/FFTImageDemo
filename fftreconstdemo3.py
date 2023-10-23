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

def decompImgCoord( img, blksz=16 ):
    startPnt = []
    nblks = 0
    for i in range(N/blksz):
        for j in range(N/blksz):
            startPnt.append( (i*blksz, j*blksz) )
            nblks += 1
    return startPnt
    

def blkiFFT( blkFFTimg, startPnts, blksz ):
    blkifftimg = np.zeros( blkFFTimg.shape, dtype=complex)
    for b in startPnts:
        py, px = b[0], b[1]
        blkifftimg[py:py+blksz, px:px+blksz] = np.fft.ifft2( blkFFTimg[py:py+blksz, px:px+blksz] )
    return blkifftimg

def blkFFT( img, startPnts, blksz ):
    blkfftimg = np.zeros( img.shape, dtype=complex )
    for b in startPnts:
        py, px = b[0], b[1]
        blkfftimg[py:py+blksz, px:px+blksz] = np.fft.fft2( img[py:py+blksz, px:px+blksz] )
    return blkfftimg

def blkFilter( blkFFTimg, flt, startPnts, blksz ):
    filterimg = np.zeros( blkFFTimg.shape, dtype=complex )
    for b in startPnts:
        py, px = b[0], b[1]
        filterimg[py:py+blksz, px:px+blksz] = blkFFTimg[py:py+blksz, px:px+blksz] * flt
    return filterimg

l = misc.lena()
N = 512
slena = misc.imresize( l, (N, N), interp='bilinear' ) / 255.


blksz = 32
blkinput = []
nblks = 0

blkPnts = decompImgCoord( slena, blksz=blksz )
blkFFTimg = blkFFT( slena, blkPnts, blksz )

flt = np.zeros( (blksz, blksz) )

RecRange = 4
RecSeq = scnseq( RecRange )


for p in (RecSeq):

    plt.clf()
    plt.subplot( 2, 3, 1 )
    plt.imshow( slena, interpolation='nearest' )
    plt.title( 'Original' )
    plt.gray()
    plt.xticks(())
    plt.yticks(())
    
    ppx, ppy = p[0], p[1]

    cur = np.zeros((blksz,blksz))
    cur[ppy,ppx] = 1
    cur[-ppy,-ppx] = 1

    plt.subplot( 2, 3, 2 )
    baseimg = np.fft.ifft2( cur ).real
    plt.imshow( baseimg, cmap=cm.coolwarm, interpolation='nearest' )
    plt.xticks( () )
    plt.yticks( () )
    plt.title( 'Base Component (Cosine)' )
    



    plt.subplot( 2, 3, 4 )    
    flt[ppy, ppx] = 1
    flt[-ppy, -ppx] = 1
    
    fblkFFTimg = blkFilter( blkFFTimg, flt, blkPnts, blksz )
    recimg = blkiFFT( fblkFFTimg, blkPnts, blksz ).real
                      
    plt.imshow( recimg, interpolation='nearest' )
    plt.gray()
    plt.xticks( () )
    plt.yticks( () )
    plt.title( 'Reconstruct' )

    plt.subplot( 2, 3, 5 )
    plt.imshow( np.fft.fftshift(flt), interpolation='nearest' )
    plt.title( 'Recon. Pos.' )
    plt.jet()
    
    plt.pause(0.01)
