import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib as mpl

from cellpose import plot, utils

path='./ImagesSegNpy/'
print("11")

for  (root,dirs,files) in os.walk(path):
    for filename in files:
        dat=np.load(path+filename,allow_pickle=True).item()
        #print(dat['filename'])
        #outline=dat['outlines']
        # plot image with masks overlaid
        #mask_RGB = plot.mask_overlay(dat['img'], dat['masks'],colors=np.array(dat['colors']))
        # plot image with outlines overlaid in red
        outlines = utils.outlines_list(dat['masks'])
        plt.imshow(dat['img'])
        plt.title(filename)
        for o in outlines:
           plt.plot(o[:,0], o[:,1], color='r')
        plt.show()
