# -*- coding: utf-8 -*-


import numpy as np
import scipy as sp
from scipy import misc
from matplotlib import cm
import matplotlib.pylab as plt


#l = misc.lena()
l = misc.imread( '../test_images/boat.png' )
slena = misc.imresize( l, (64,64), interp='bilinear' ) / 255.
#slena = np.random.randn( 64, 64 )

fig = plt.figure()
ax = fig.gca()

plt.subplot( 1, 2, 1 )
axsub1 = plt.imshow( slena, interpolation='nearest' )
plt.xticks(())
plt.yticks(())
plt.title( 'Original' )
fig.colorbar( axsub1, shrink=0.4, aspect=10 )


SLENA = np.fft.fft2( slena )
plt.subplot( 1, 2, 2 )
axsub2 = plt.imshow( np.fft.fftshift( np.abs( SLENA ) ), interpolation='nearest', cmap=cm.coolwarm )
plt.title( 'Fourier Power' )
#axsub2 = plt.imshow( np.fft.fftshift( np.log( np.abs( SLENA ) ) ), interpolation='nearest', cmap=cm.coolwarm )
#plt.title( 'Fourier Power(Log)' )

plt.xticks(())
plt.yticks(())
fig.colorbar( axsub2, shrink=0.4, aspect=10 )


plt.show()
