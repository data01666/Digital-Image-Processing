#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import matplotlib.pyplot as plt
plt.rcParams['font.family']='SimHei'

#读取RGB图像并转换为灰度图像
image = cv2.cvtColor(cv2.imread('Lena.bmp'), cv2.COLOR_BGR2GRAY)

#对图像进行反色变换
inverted_image = 255 - image

# 显示原始图像和反色变换后的图像
fig, axes = plt.subplots(1, 2)
axes[0].imshow(image, cmap='gray')
axes[0].set_title('原图')
axes[1].imshow(inverted_image, cmap='gray')
axes[1].set_title('反色变换')
plt.show()


# In[2]:


import cv2
import matplotlib.pyplot as plt

#读取图像将BGR转为RGB
image = cv2.cvtColor(cv2.imread('Lena.bmp'), cv2.COLOR_BGR2RGB)

#将图像分割为蓝色、绿色和红色通道
blue_channel, green_channel, red_channel = cv2.split(image)
#对每个通道进行反色变换
inverted_blue_channel = 255 - blue_channel
inverted_green_channel = 255 - green_channel
inverted_red_channel = 255 - red_channel
# 合并通道得到反色变换后的图像
inverted_image = cv2.merge((inverted_blue_channel, inverted_green_channel, inverted_red_channel))

fig, axes = plt.subplots(1, 2)
axes[0].imshow(image)
axes[0].set_title('原图')
axes[1].imshow(inverted_image)
axes[1].set_title('反色变换')
plt.show()

