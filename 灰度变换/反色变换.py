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
