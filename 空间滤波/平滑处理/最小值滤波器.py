#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'

def min_filter(image, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    filtered_image = cv2.erode(image, kernel)
    return filtered_image

image = cv2.imread('Lena.bmp', 0)
kernel_size = 3  #最小值滤波器的模板大小
filtered_image = min_filter(image, kernel_size)

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(image, cmap='gray')
axs[0].set_title('原图')
axs[1].imshow(filtered_image, cmap='gray')
axs[1].set_title('最小值滤波器')
plt.show()

