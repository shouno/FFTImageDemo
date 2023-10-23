# -*- coding: utf-8 -*-
#

import numpy as np
import scipy as sp
from scipy import misc
from matplotlib import cm
import matplotlib.pylab as plt


def scnline(n):
    ret = []
    for i in range(n + 1):
        ret.append((i, n - i))
    for i in range(n + 1):
        ret.append((-i, n - i))

    return ret


def scnseq(n):
    ret = []
    for i in range(n + 1):
        ret += scnline(i)
    return ret


def decompImgCoord(img, blksz=16):
    startPnt = []
    nblks = 0
    Nh = img.shape[0]
    Nw = img.shape[1]
    for i in range(Nh // blksz):
        for j in range(Nw // blksz):
            startPnt.append((i * blksz, j * blksz))
            nblks += 1
    return startPnt


def blkiFFT(blkFFTimg, startPnts, blksz):
    blkifftimg = np.zeros(blkFFTimg.shape, dtype=complex)
    for b in startPnts:
        py, px = b[0], b[1]
        blkifftimg[py : py + blksz, px : px + blksz] = np.fft.ifft2(
            blkFFTimg[py : py + blksz, px : px + blksz]
        )
    return blkifftimg


def blkFFT(img, startPnts, blksz):
    blkfftimg = np.zeros(img.shape, dtype=complex)
    for b in startPnts:
        py, px = b[0], b[1]
        blkfftimg[py : py + blksz, px : px + blksz] = np.fft.fft2(
            img[py : py + blksz, px : px + blksz]
        )
    return blkfftimg


def blkFilter(blkFFTimg, flt, startPnts, blksz):
    filterimg = np.zeros(blkFFTimg.shape, dtype=complex)
    for b in startPnts:
        py, px = b[0], b[1]
        filterimg[py : py + blksz, px : px + blksz] = (
            blkFFTimg[py : py + blksz, px : px + blksz] * flt
        )
    return filterimg


slena = plt.imread("../test_images/lena.png")

# blksz = 32
blksz = 16
# blksz = 8
blkinput = []
nblks = 0

blkPnts = decompImgCoord(slena, blksz=blksz)
blkFFTimg = blkFFT(slena, blkPnts, blksz)

flt = np.zeros((blksz, blksz))

RecRange = 6
RecSeq = scnseq(RecRange)

print("Total CoverRate", len(RecSeq) / (blksz**2))

for p in RecSeq:
    plt.clf()
    plt.subplot(2, 3, 1)
    plt.imshow(slena, interpolation="nearest")
    plt.title("Original")
    plt.gray()
    plt.xticks(())
    plt.yticks(())

    ppx, ppy = p[0], p[1]

    cur = np.zeros((blksz, blksz))
    cur[ppy, ppx] = 1
    cur[-ppy, -ppx] = 1

    plt.subplot(2, 3, 2)
    baseimg = np.fft.ifft2(cur).real
    plt.imshow(baseimg, cmap=cm.seismic, interpolation="nearest")
    plt.xticks(())
    plt.yticks(())
    plt.title("Base Component (Cosine)")

    #    nblk = 4
    nblk = 3
    #    xoff, yoff = 7, 7
    xoff, yoff = 15, 15
    plt.subplot(2, 3, 3)
    rrr = (yoff * blksz, (yoff + nblk) * blksz, xoff * blksz, (xoff + nblk) * blksz)
    plt.imshow(
        slena[rrr[0] : rrr[1], rrr[2] : rrr[3]], cmap=cm.gray, interpolation="nearest"
    ),
    plt.xticks(())
    plt.yticks(())
    plt.title("Magnified(Orig.)")

    plt.subplot(2, 3, 4)
    flt[ppy, ppx] = 1
    flt[-ppy, -ppx] = 1

    fblkFFTimg = blkFilter(blkFFTimg, flt, blkPnts, blksz)
    recimg = blkiFFT(fblkFFTimg, blkPnts, blksz).real

    plt.imshow(recimg, interpolation="nearest")
    plt.gray()
    plt.xticks(())
    plt.yticks(())
    plt.title("Reconstruct")

    plt.subplot(2, 3, 5)
    plt.imshow(np.fft.fftshift(flt), interpolation="nearest")
    plt.title("Recon. Pos.")
    plt.jet()

    plt.subplot(2, 3, 6)
    plt.imshow(
        recimg[rrr[0] : rrr[1], rrr[2] : rrr[3]], cmap=cm.gray, interpolation="nearest"
    ),
    plt.xticks(())
    plt.yticks(())
    plt.title("Magnified(Recon.)")

    plt.pause(0.5)


input()
