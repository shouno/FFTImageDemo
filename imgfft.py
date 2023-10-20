import numpy as np
import scipy as sp
from scipy.fft import fft2, fftshift
from PIL import Image  # 現代風に Pillow を使おう
from matplotlib import cm
import matplotlib.pylab as plt


#
IMG_SIZE = 128
src_img = Image.open("../test_images/boat.png")
img = src_img.resize((IMG_SIZE, IMG_SIZE))

fig = plt.figure(figsize=(12, 4))
axs = fig.subplots(1, 3)

org_img = axs[0].imshow(img, cmap="gray")
axs[0].set_title("Original")
axs[0].set_xticks([])
axs[0].set_yticks([])
cbar0 = plt.colorbar(org_img, shrink=0.6, aspect=10)
# fig.colorbar(axsub1, shrink=0.4, aspect=10)


FFT_IMG = fft2(img)
fft_img_orig = axs[1].imshow(fftshift(np.abs(FFT_IMG)), cmap="jet")
axs[1].set_title("Fourier Power")
axs[1].set_xticks([])
axs[1].set_yticks([])
cbar1 = plt.colorbar(fft_img_orig, shrink=0.6, aspect=10)

fft_img_log = axs[2].imshow(np.log(fftshift(np.abs(FFT_IMG))), cmap="jet")
axs[2].set_title("Fourier Power(Log)")
axs[2].set_xticks([])
axs[2].set_yticks([])
cbar2 = plt.colorbar(fft_img_log, shrink=0.6, aspect=10)

plt.tight_layout()

plt.show()
