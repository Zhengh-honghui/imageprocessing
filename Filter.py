import numpy as np
import cv2
import matplotlib.pyplot as plt
########     四个不同的滤波器    #########
img = cv2.imread(r'C:\Users\14599\Desktop\1.png')
b,g,r = cv2.split(img)
img = cv2.merge([r,g,b])

# 均值滤波  cv2.blur(image, (ksize, ksize)) 可以作用于RGB图像
#Ksize越大，图像越平滑,也就是越模糊,是线性滤波器。
img_mean = cv2.blur(img, (3,3))

# 高斯滤波 cv2.GaussianBlur(image, (size, size), sigmaX, sigmaY)
#sigmaX和sigmaY代表了横轴与纵轴权重的标准差，若为0就是让opencv帮你自动推算方差大小。可作用于RGB图像
#虑到卷积核内像素的权重，是线性滤波器。是应用最多最多的平滑滤波器！
#一般的图像预处理操作都少不了它,一般，使用频率高斯卷积核越大，方差越大，图像就越模糊
img_Guassian = cv2.GaussianBlur(img,(3,3),0)

# 中值滤波cv2.medianBlur(image, Ksize)
# 注意这里的第二个参数不是tuple了，是一个整数，代表了(Ksize, Ksize)，所以意义是一样的。能够作用于RGB图像
#是一种非线性滤波器，能够很好的消除椒盐噪声
img_median = cv2.medianBlur(img, 7)

# 双边滤波cv2.bilaterFilter(image, Ksize, sigmaColor, sigmaSpace)
# Ksize是一个整数，代表了卷积核的大小，sigmaColor是灰度差值权重的标准差，sigmaSpace是位置权重的标准差
# 和前面的高斯滤波的权重是一致的，这两个标准差越大，滤波能力越强，同时还能较好的保留边缘信息。能够作用于RGB图像。
# ps的磨皮、人物卡通化都是通过双边滤波实现的。该算法复杂度高，耗时长
#参数选择 https://blog.csdn.net/jfuck/article/details/8932978
img_bilater = cv2.bilateralFilter(img, 7, 150, 150)

# 展示不同的图片
titles = ['srcImg','mean', 'Gaussian', 'median', 'bilateral']
imgs = [img, img_mean, img_Guassian, img_median, img_bilater]

for i in range(5):
    plt.subplot(2,3,i+1)
    #plt.subplot(nrows, ncols, index, **kwargs) 三个整数是行数、列数和索引值
    #注意，这和matlab中类似，没有0，数组下标从1开始
    plt.imshow(imgs[i])
    plt.title(titles[i])
plt.show()

#https://blog.csdn.net/qq_27261889/article/details/80822270

