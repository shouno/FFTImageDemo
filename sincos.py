import numpy as np
import matplotlib.pylab as plt

N = 256
k = 10

x = np.linspace(0, 2 * np.pi, N)
y = np.cos(k * x)

plt.figure()
plt.plot(x, y, linewidth=2)
plt.grid()
plt.title(f"cos({k:2}x)")
plt.xlim(0, 2 * np.pi)

plt.show()
