#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 08:58:41 2019

@author: lty
"""

import SimpleITK as sitk
import scipy.io
import os
import natsort
import time

start = time.time()
nii_path = '/DataDisk/liutianyu/DenseInferenceWrapper-master/CRF_perpare/crf_liver_results_to_submit/crf_liver_submit_opening_results'
save_path = '/DataDisk/liutianyu/DenseInferenceWrapper-master/CRF_perpare/crf_liver_results_to_submit/crf_liver_submit_opening_results_slice'

folders = natsort.natsorted(os.listdir(nii_path))
for i in range(len(folders)):
    folders_path = os.path.join(nii_path, folders[i])
    img = sitk.ReadImage(folders_path)
    img_array = sitk.GetArrayFromImage(img)
    z = img_array.shape[0]
    for j in range(z):
        silce = img_array[j,:,:]
        scipy.misc.imsave(os.path.join(save_path, str(i))+'/'+str(j+1)+'.png', silce)
        end = time.time()
        print(end-start)

        
