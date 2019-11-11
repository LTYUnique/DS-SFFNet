#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:14:04 2019

@author: lty
"""

import SimpleITK as sitk
import os
#import numpy as np
import natsort 
import time

start = time.time()
nii_path = '/home/lty/Desktop/seg_lesion_crf_new_results/crf_opening_k_1_results'
save_path = '/home/lty/Desktop/seg_lesion_crf_new_results/crf_opening_k_1_results_change_shreshold'

nii_files = natsort.natsorted(os.listdir(nii_path))
for i in range(len(nii_files)):
    nii_files_path = os.path.join(nii_path, nii_files[i])
    img = sitk.ReadImage(nii_files_path)
    img_array = sitk.GetArrayFromImage(img)
    img_array[img_array < 1] = 0
    img_array[img_array >= 1] = 2
    binary_img = sitk.GetImageFromArray(img_array)
    sitk.WriteImage(binary_img,os.path.join(save_path,'test-segmentation-'+str(i))+'.nii')
    end = time.time()
    print(end-start)
    

