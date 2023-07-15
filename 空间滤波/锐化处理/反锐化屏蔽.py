import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'

def mean_filter(image, kernel_size):
    #均值滤波器
    filtered_image = cv2.blur(image, (kernel_size, kernel_size))
    return filtered_image

def unsharp_masking(image, kernel_size):
    #反锐化屏蔽
    blurred = mean_filter(image, kernel_size)
    mask = cv2.subtract(image, blurred)
    sharpened = cv2.addWeighted(image, 1, mask, 1, 0)
    return mask, sharpened

image = cv2.imread('Cameraman.bmp', 0)
kernel_size = 5
mask, sharpened = unsharp_masking(image, kernel_size)

fig, axs = plt.subplots(1, 3, figsize=(12, 4))
axs[0].imshow(image, cmap='gray')
axs[0].set_title('原图')
axs[1].imshow(mask, cmap='gray')
axs[1].set_title('差值图像')
axs[2].imshow(sharpened, cmap='gray')
axs[2].set_title('反锐化屏蔽')
plt.show()
