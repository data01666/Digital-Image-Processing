import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'

def mean_filter(image, kernel_size):
    # 使用均值滤波器进行滤波
    filtered_image = cv2.blur(image, (kernel_size, kernel_size))
    return filtered_image

image = cv2.imread('Lena.bmp', 0)
kernel_size = 5  # 自定义均值滤波器大小
filtered_image = mean_filter(image, kernel_size)

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(image, cmap='gray')
axs[0].set_title('原图')
axs[1].imshow(filtered_image, cmap='gray')
axs[1].set_title('均值滤波器')
plt.show()
