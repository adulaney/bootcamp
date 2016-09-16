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


def hot_pixel_fix(image, pixel_shape=3):
    """
    Corrects for hot pixels.
    """

    selem = skimage.morphology.square(pixel_shape)
    im_med_filt = skimage.filters.median(image, selem)
    return im_med_filt


def illumination_fix(image, blur_radius=50):
    """
    Corrects uneven illumination.
    """

    im_blur = skimage.filters.gaussian(image, blur_radius)
    im_float = skimage.img_as_float(image)
    im_sub = im_float - im_blur
    return im_sub


def image_thresholding(image, microscopy='phase'):
    thresh = skimage.filters.threshold_otsu(image)
    if microscopy == 'phase':
        seg = image < thresh
    else:
        seg = image > thresh
    seg_lab, num_cells = skimage.measure.label(seg, return_num=True,
                                                    background=0)

    return seg_lab, num_cells


def object_size_slicing(image, cutoff=300, interpixel_dist=.063):
    """
    Removes objects too large or too small to be things of interest.
    """
    # Compute region properties and extract object areas.
    ip_dist = interpixel_dist # micron per pixel
    props = skimage.measure.regionprops(image)

    # Get the areas as an array.
    areas = np.array([prop.area for prop in props])
    im_cells = np.copy(image) > 0
    for i,_ in enumerate(areas):
        if areas[i] < cutoff:
            im_cells[image==props[i].label] = 0
    area_filt_lab = skimage.measure.label(im_cells)
    return area_filt_lab


def image_segmentation(image, hot_pixel=True, illumination=True,
                       microscopy='phase', thresholding=True,
                       size=True, pixel_shape=3, blur_radius=50,
                       interpixel_dist=0.063, cutoff=300):
    """
    Perform image segmentation.
    """

    if hot_pixel == True:
        # Correct for hot pixels
        im_med_filt = hot_pixel_fix(image, pixel_shape)
    else:
        im_med_filt = image

    if illumination == True:
        # Correct uneven illumination
        im_sub = illumination_fix(im_med_filt, blur_radius)
    else:
        im_sub = im_med_filt

    if thresholding == True:
        # Perform otsu thresholding
        seg_lab, num_cells = image_thresholding(im_sub, microscopy)
    else:
        seg_lab == im_sub

    if size == True:
        # Compute region properties and extract object areas.
        # Get the areas as an array
        im_cells = object_size_slicing(seg_lab, cutoff, interpixel_dist)
    else:
        im_cells = seg_lab

    # Show the image
    plt.imshow(im_cells, cmap=plt.cm.viridis)
    return im_cells
