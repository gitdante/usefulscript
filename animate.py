"""
========================================
An animated image using a list of images
========================================

This examples demonstrates how to animate an image from a list of images (or
Artists).

after modified can be used to plot d/m tif
imagemagick required
"""
from osgeo import gdal
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
plt.axis('off')
name=[i for i in os.listdir('.') if '.tif' in i]


def readdata(path):
    fid = gdal.Open(path, gdal.GA_ReadOnly)
    data = fid.GetRasterBand(1).ReadAsArray()
    return data

# ims is a list of lists, each row is a list of artists to draw in the
# current frame; here we are just animating one artist, the image, in
# each frame
ims = []
for i in name:
    im = plt.imshow(readdata(i),vmax=10,vmin=0,cmap='Spectral',animated=True)
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=1000, blit=True,
                                repeat_delay=500)

#ani.save('dynamic_images.mp4')

plt.show()
