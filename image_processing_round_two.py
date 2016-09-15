import numpy as np

# Our image processing tools
import skimage.filters
import skimage.io
import skimage.measure
import skimage.morphology
import skimage.segmentation

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)
sns.set_style('dark')

# Load an example phase image.
phase_im = skimage.io.imread('data/HG105_images/noLac_phase_0004.tif')

# Show the image.
plt.imshow(phase_im, cmap=plt.cm.viridis)
plt.show()
plt.close()

# Apply a gaussian blur to the image.
im_blur = skimage.filters.gaussian(phase_im, 50)

# Convert our phase image to a float.
phase_float = skimage.img_as_float(phase_im)
phase_sub = phase_float - im_blur

# Show both
plt.figure()
plt.imshow(phase_float, cmap=plt.cm.viridis)
plt.title('original')
plt.figure()
plt.imshow(phase_sub, cmap=plt.cm.viridis)
plt.title('subtracted')

# Apply otsu thresholding
thresh = skimage.filters.threshold_otsu(phase_sub)
seg = phase_sub < thresh

# Plot segmentation
plt.close('all')
plt.imshow(seg, cmap=plt.cm.Greys_r)


# Label 'em
seg_lab, num_cells = skimage.measure.label(seg, return_num=True, background=0)
plt.close()
plt.imshow(seg_lab, cmap=plt.cm.Spectral_r)

# Compute the region properties and extract area of each object
ip_dist = 0.063 # micron per pixel
props = skimage.measure.regionprops(seg_lab)

# Get the areas as an array
areas = np.array([prop.area for prop in props])
cutoff = 300
im_cells = np.copy(seg_lab) > 0
for i,_ in enumerate(areas):
    if areas[i] < cutoff:
        im_cells[seg_lab==props[i].label] = 0

area_filt_lab = skimage.measure.label(im_cells)

plt.figure()
plt.imshow(area_filt_lab, cmap=plt.cm.Spectral_r)







im_fl = skimage.io.imread('data/HG105_images/noLac_FITC_0004.tif')
