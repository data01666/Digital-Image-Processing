#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family']='SimHei'

#读取RGB图像并转换为灰度图像
image = cv2.imread('Lena.bmp', 0)

#对数变换
c = 1.0  #对数变换常数
log_transformed = c * np.log(1 + image)
# 转换为整数类型（0-255）
log_transformed = np.uint8(log_transformed)

fig, axes = plt.subplots(1, 2)
axes[0].imshow(image, cmap='gray')
axes[0].set_title('原图')
axes[1].imshow(log_transformed, cmap='gray')
axes[1].set_title('对数变换')
plt.show()

