import numpy as np
import pandas as pd
# Our image processing tools
import skimage.filters
import skimage.io
import skimage.measure
import skimage.morphology
import skimage.segmentation
import image_segmentation_function as sf
import matplotlib.pyplot as plt
import glob
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)
sns.set_style('dark')

image_names = glob.glob('data/bacterial_growth/*.tif')

images = []
for filename in image_names:
    im = skimage.io.imread(filename)
    images.append(im)

segmented_image = []
for im in images:
    segmented_image.append(sf.image_segmentation(im, interpixel_dist=0.0645, microscopy='fluorescent'))

plt.imshow(images[1])
plt.imshow(segmented_image[1], cmap=plt.cm.BuGn, alpha=0.5)
im_rgb = np.dstack(3 * [images[1] / images[1].max()])
# im_copy = np.copy(images[1] / images[1].max())
# im_copy[segmented_image[1] > 0] = 1.0
# merge = np.dstack((images[1] / images[1].max(), im_copy, images[1]/images[1].max()))
# plt.imshow(merge)
im_rgb[segmented_image[1] > 0] = 1.0
