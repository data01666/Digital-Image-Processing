import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'

def butterworth_highpass_filter(image, cutoff_freq, n):
    #傅里叶变换
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)
    #创建巴特沃斯高通滤波器的掩膜
    rows, cols = image.shape
    center_row, center_col = rows // 2, cols // 2
    mask = np.ones((rows, cols), np.float32)
    for i in range(rows):
        for j in range(cols):
            dist = np.sqrt((i - center_row) ** 2 + (j - center_col) ** 2)
            #添加1e-8常数可以确保避免零除错误，并且不会显著影响滤波器结果
            mask[i, j] = 1 / (1 + (cutoff_freq / (dist + 1e-8)) ** (2 * n)) 
    #将掩膜应用于傅里叶变换后的图像
    fshift_filtered = fshift * mask
    #逆傅里叶变换
    f_inverse = np.fft.ifftshift(fshift_filtered)
    filtered_image = np.fft.ifft2(f_inverse)
    filtered_image = np.abs(filtered_image)
    return filtered_image

image = cv2.imread('Lena.bmp', 0)

#自定义巴特沃斯高通滤波器的截止频率和阶数
cutoff_freq = 30
n = 1
filtered_image = butterworth_highpass_filter(image, cutoff_freq, n)

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(image, cmap='gray')
axs[0].set_title('原图')
axs[1].imshow(filtered_image, cmap='gray')
axs[1].set_title('巴特沃斯高通滤波器')
plt.show()
