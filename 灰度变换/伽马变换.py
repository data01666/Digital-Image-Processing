#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'

#读取灰度图像
image = cv2.imread('Lena.bmp', 0)

#伽马变换
gamma = 2  #伽马值
gamma_transformed = np.power(image / 255.0, gamma) * 255.0
# 转换为整数类型（0-255）
gamma_transformed = np.uint8(gamma_transformed)

fig, axes = plt.subplots(1, 2)
axes[0].imshow(image, cmap='gray')
axes[0].set_title('原图')
axes[1].imshow(gamma_transformed, cmap='gray')
axes[1].set_title('伽马变换')
plt.show()


# In[ ]:




