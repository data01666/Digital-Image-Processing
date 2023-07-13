import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'

#读取图像
image = cv2.imread('Lena.bmp', 0)

#分段线性变换参数
x_min = 50
x_max = 200
# 分段线性变换函数
def piecewise_linear_transform(pixel_value):
    if pixel_value < x_min:
        return 0
    elif pixel_value > x_max:
        return 255
    else:
        return 255 * (pixel_value - x_min) / (x_max - x_min)

#对图像进行分段线性变换
transformed_image = np.vectorize(piecewise_linear_transform)(image)

#计算原始图像的直方图
hist_original, _ = np.histogram(image.flatten(), bins=256, range=[0, 256])
#计算变换后图像的直方图
hist_transformed, _ = np.histogram(transformed_image.flatten(), bins=256, range=[0, 256])

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes[0, 0].imshow(image, cmap='gray')
axes[0, 0].set_title('原始图像')
axes[0, 1].imshow(transformed_image, cmap='gray')
axes[0, 1].set_title('分段线性变换')
axes[1, 0].bar(range(256), hist_original, color='gray', alpha=0.7)
axes[1, 0].set_title('原始图像直方图')
axes[1, 0].set_xlabel('灰度值')
axes[1, 0].set_ylabel('像素数量')
axes[1, 1].bar(range(256), hist_transformed, color='gray', alpha=0.7)
axes[1, 1].set_title('分段线性变换直方图')
axes[1, 1].set_xlabel('灰度值')
axes[1, 1].set_ylabel('像素数量')
plt.show()




