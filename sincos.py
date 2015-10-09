#
# -*- coding: utf-8 -*-
#

import numpy as np
import matplotlib.pylab as plt

N = 256

#x = ( range( N ) / np.double(N) * 2 - 1 ) * np.pi 
x = ( range( N ) / np.double(N) * 2 ) * np.pi 
#y = np.sin(x)
#y = np.cos(x)
#y = np.sin( 2 * x )
#y = np.cos( 2 * x )
#y = np.sin( 10 * x )
y = np.cos( 10 * x )

plt.clf()

plt.plot( x, y, linewidth=2 )
plt.grid()
#plt.title( 'sine wave: sin(x)' )
#plt.title( 'cosine wave: cos(x)' )
#plt.title( 'sine wave: sin(2x)' )
#plt.title( 'cosine wave: cos(2x)' )
#plt.title( 'sine wave: sin(10x)' )
plt.title( 'cosine wave: cos(10x)' )
#plt.xlim( -np.pi, np.pi )
plt.xlim( 0, 2 * np.pi )


plt.show()


