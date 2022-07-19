#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 16:27:45 2022

@author: pcunha
"""

import numpy as np
import matplotlib
import sep
from skimage.io import imread
import skimage 
import os

'''
https://sep.readthedocs.io/en/v1.1.x/api/sep.extract.html#sep.extract 
https://sep.readthedocs.io/en/v1.1.x/api/sep.mask_ellipse.html#sep.mask_ellipse
'''

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

# Path with the original data. Change it accordingly
path ='./test_mask_images/data/'

# Path to save final masked images. Change it accordingly
path2 = './test_mask_images/data_mask/'

image_list = os.listdir(path)
count=0
image_len=len(image_list)

for i in range(image_len):
    count +=1
    im = imread(path+image_list[i])
    im = im.T[:,106:106*3,106:106*3] #crop 424x424 -> 212x212
    data = im.T
    #print(im.shape, data.shape)


    data_gray = rgb2gray(data)

    # measure a spatially varying background on the image
    bkg = sep.Background(data_gray)

    # subtract the background
    data_sub = data_gray - bkg

    #extracting all the objects from the image with sigma higher than 4
    objects, mapp = sep.extract(data_sub, 4, err=bkg.globalrms, segmentation_map = True, minarea=10)
    
    # Computes the vertical and horizontal length of the mask 
    N,M = mapp.shape
    # Get the labels given in the mask. It changes on the number of sources detected
    regions = skimage.measure.label(mapp)
    # Extract the label that is detected in the center of the image
    object_label = regions[N//2, M//2]
    # Create a zero array with size of the mask
    object_mask = np.zeros_like(mapp)
    # Selects the center region with wanted label and sets it to 1
    object_mask[regions == object_label] = 1
    # Performs binary dilation in the mask, transforms into boolean format
    object_mask =skimage.morphology.binary_dilation(object_mask, footprint=skimage.morphology.disk(25))
    # Sets the center region to 0 and the rest to 1
    object_mask = 1- object_mask

    corr_img = data.copy()
    # Applies the mask to the image
    corr_img[object_mask == 1] = 0 
    
    #Saves the image to be used for classification
    matplotlib.image.imsave(path2+'mask_'+str(image_list[i]), corr_img)
    print('Done! '+str(image_len-count)+' to go.')

    
