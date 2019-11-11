# DS-SFFNet
Deep supervision spatial Feature Fusion convolutional network (DS-SFFNet) is an end-to-end liver and liver tumor segmentation neural network, which based on deep supervision mechnaism and residual attention mechnaism. 

### This work used [miriambellver's work](https://github.com/imatge-upc/liverseg-2017-nipsws) and modified it to achieve our purpose.


## 1 The overall pipeline:

In the training phase, we first train liver segmentation network to get the coarse liver segmentation results. The liver ROI of CT images are located according to the liver segmentation results. Secondly, we use liver ROI to train liver tumor segmentation network to get the coarse liver tumor segmentation results. 

In the testing phase, we first get the accurate liver segmentation results. Then the DS-SFFNet can generate the coarse liver tumor segmentation results. To avoid over-segmentation in the liver tumor region, we remove the area out of liver by using the liver mask. In the end, a 3D fully connected conditional random fields[22] (CRFs) is utilized to refine the final liver tumor segmentation results. 

![the over pipeline](https://github.com/LTYUnique/DS-SFFNet/blob/master/images/figure%202.png)


