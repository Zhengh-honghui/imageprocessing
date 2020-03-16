import numpy as np
from skimage import data,img_as_float,io
import matplotlib.pyplot as plt
import cv2
rgb = cv2.imread(r'C:\Users\14599\Desktop\kidney-epcam (2)2.png')

b,g,r = cv2.split(rgb)
rgb = cv2.merge([r,g,b])
rgb1 = rgb

#gray_img = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
#img_mean = cv2.blur(gray_img, (9,9))
gray_img = cv2.cvtColor(rgb1, cv2.COLOR_RGB2GRAY)
img = r

#固定阀值分割 cv2.threshold()用来实现阈值分割，ret是return value缩写，代表当前的阈值，暂时不用理会。
#函数有4个参数：
#参数1：要处理的原图，一般是灰度图
#参数2：设定的阈值
#参数3：最大阈值，一般为255
#参数4：阈值的方式，主要有5种
'''ret, th = cv2.threshold(g, 147, 255, cv2.THRESH_BINARY)
cv2.adaptiveThreshold()
cv2.imshow('thresh', th)
cv2.waitKey(0)'''
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

'''#直方图绘制
hist = cv2.calcHist([gray_img], [0], None, [256], [0,256])
plt.subplot(2, 2, 1)
plt.hist(gray_img.ravel(), 255, [0,256])
plt.subplot(2, 2, 4)
plt.imshow(img_mean)

#直方图绘制
hist = cv2.calcHist([img_mean], [0], None, [256], [0,256])
plt.subplot(2, 2, 2)
plt.hist(gray_img.ravel(), 255, [0,256])'''
titles = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV', 'OSTU', 'adaptive1', 'adaptive2']
images = [img, th1, th2, th3, th4, th5, th6, th7, th8]

# 使用Matplotlib显示
for i in range(9):
    plt.subplot(3, 3, i + 1)
    images[i] = cv2.merge([images[i], g, b])
    plt.imshow(images[i])
    plt.title(titles[i], fontsize=8)
    plt.xticks([]), plt.yticks([])  # 隐藏坐标轴

plt.show()
plt.imshow(images[5])
io.imsave(r'C:\Users\14599\Desktop\kidney-epcam (2)2_first.png', images[5])
plt.show()
#plt.subplot(2, 2, 3)
#plt.imshow(rgb)
#plt.show()

#https://blog.csdn.net/qq_33414271/article/details/78765966
#https://www.jianshu.com/p/293e04f134c3
#自适应阀值分割
# 看得出来固定阈值是在整幅图片上应用一个阈值进行分割，它并不适用于明暗分布不均的图片。
# cv2.adaptiveThreshold()自适应阈值会每次取图片的一小部分计算阈值，这样图片不同区域的阈值就不尽相同。
'''参数1：要处理的原图
参数2：最大阈值，一般为255
参数3：小区域阈值的计算方式
ADAPTIVE_THRESH_MEAN_C：小区域内取均值
ADAPTIVE_THRESH_GAUSSIAN_C：小区域内加权求和，权重是个高斯核
参数4：阈值方式（跟前面讲的那5种相同）
参数5：小区域的面积，如11就是11*11的小块
参数6：最终阈值等于小区域计算出的阈值再减去此值'''
'''ret, th1 = cv2.threshold(img, 147, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 255, 0)
th3 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 255, 0)

titles = ['Original', 'Global(v = 147)', 'Adaptive Mean', 'Adaptive Gaussian']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i], fontsize=8)
    plt.xticks([]), plt.yticks([])
plt.show()

#OSTU阀值分割 第二个参数应该设置为0
ret2, th0 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('thresh', th0)
cv2.waitKey(0)
ostu = cv2.merge([r, th0, b])
cv2.imshow('ostu', ostu)
cv2.waitKey(0)'''