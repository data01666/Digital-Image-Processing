#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'

#读取图像
image = cv2.imread('Lena.bmp', 0)

#进行直方图均衡化
equalized_image = cv2.equalizeHist(image)

#计算原始图像的直方图
hist_original, _ = np.histogram(image.flatten(), bins=256, range=[0, 256])
#计算均衡化后图像的直方图
hist_equalized, _ = np.histogram(equalized_image.flatten(), bins=256, range=[0, 256])

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes[0, 0].imshow(image, cmap='gray')
axes[0, 0].set_title('原始图像')
axes[0, 1].imshow(equalized_image, cmap='gray')
axes[0, 1].set_title('直方图均衡化')
axes[1, 0].bar(range(256), hist_original, color='gray', alpha=0.7)
axes[1, 0].set_title('原始图像直方图')
axes[1, 0].set_xlabel('灰度值')
axes[1, 0].set_ylabel('像素数量')
axes[1, 1].bar(range(256), hist_equalized, color='gray', alpha=0.7)
axes[1, 1].set_title('直方图均衡化直方图')
axes[1, 1].set_xlabel('灰度值')
axes[1, 1].set_ylabel('像素数量')
plt.show()


# In[ ]:




