import numpy as np
from skimage import data,img_as_float,io
import matplotlib.pyplot as plt
import cv2
rgb = cv2.imread(r'C:\Users\14599\Desktop\p2-ecadherin.png')

b,g,r = cv2.split(rgb)
rgb = cv2.merge([r,g,b])
rgb1 = rgb

gray_img = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
#img_mean = cv2.blur(gray_img, (9,9))
img = cv2.cvtColor(rgb1, cv2.COLOR_RGB2GRAY)

# 应用5种不同的阈值方法
ret, th1 = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY)
ret, th2 = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY_INV)
ret, th3 = cv2.threshold(img, 70, 255, cv2.THRESH_TRUNC)
ret, th4 = cv2.threshold(img, 70, 255, cv2.THRESH_TOZERO)
ret, th5 = cv2.threshold(img, 70, 255, cv2.THRESH_TOZERO_INV)
#OSTU阀值分割 第二个参数应该设置为0
ret2, th6 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

th7 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 255, 0)
th8 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 255, 0)

titles = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV', 'OSTU', 'adaptive1', 'adaptive2']
images = [img, th1, th2, th3, th4, th5, th6, th7, th8]

# 使用Matplotlib显示
for i in range(9):
    plt.subplot(3, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i], fontsize=8)
    plt.xticks([]), plt.yticks([])  # 隐藏坐标轴

plt.show()


plt.imshow(images[1])
io.imsave(r'C:\Users\14599\Desktop\p2-ecadherin_first.png', images[1])
plt.show()

#
