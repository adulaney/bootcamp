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

def image_segmentation(image):
    """
    Perform image segmentation.
    """

    # Correct uneven illumination
    im_blur = skimage.filters.gaussian(image, 50)
    im_float = skimage.img_as_float(image)
    im_sub = im_float - im_blur

    # Correct for hot pixels
    selem = skimage.morphology.square(3)
    im_med_filt = skimage.filters.median(im_sub, selem)

    
