import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'

def gaussian_filter(image, size, sigma):
    kernel = gaussian_kernel(size, sigma)  #生成高斯核
    filtered_image = cv2.filter2D(image, -1, kernel)  #应用高斯滤波器
    return filtered_image

def gaussian_kernel(size, sigma):
    kernel = np.fromfunction(
        lambda x, y: (1/(2*np.pi*sigma**2)) * np.exp(-((x - size//2)**2 + (y - size//2)**2)/(2*sigma**2)),
        (size, size)
    )
    return kernel / np.sum(kernel)

image = cv2.imread('Lena.bmp', 0)
size = 3  #自定义滤波器大小
sigma = 0.8  #标准差
filtered_image = gaussian_filter(image, size, sigma)

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(image, cmap='gray')
axs[0].set_title('原图')
axs[1].imshow(filtered_image, cmap='gray')
axs[1].set_title('高斯滤波器')
plt.show()
