import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'

def roberts_operator(image):
    kernel_x = np.array([[-1, 0], [0, 1]])
    kernel_y = np.array([[0, -1], [1, 0]])
    gradient_x = cv2.filter2D(image, -1, kernel_x)
    gradient_y = cv2.filter2D(image, -1, kernel_y)
    magnitude = np.sqrt(np.square(gradient_x) + np.square(gradient_y))
    magnitude = np.uint8(magnitude)
    return gradient_x, gradient_y, magnitude

image = cv2.imread('Cameraman.bmp', 0)
gradient_x, gradient_y, magnitude = roberts_operator(image)

fig, axs = plt.subplots(2, 2, figsize=(5, 5))
axs[0, 0].imshow(image, cmap='gray')
axs[0, 0].set_title('原图')
axs[0, 1].imshow(gradient_x, cmap='gray')
axs[0, 1].set_title('正对角线')
axs[1, 0].imshow(gradient_y, cmap='gray')
axs[1, 0].set_title('反对角线')
axs[1, 1].imshow(magnitude, cmap='gray')
axs[1, 1].set_title('梯度图像')
plt.show()
