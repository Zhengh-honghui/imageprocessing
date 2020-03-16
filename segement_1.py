import numpy as np
from skimage import data,img_as_float
import matplotlib.pyplot as plt
import cv2

def calcGrayHist(image):
    '''
    统计像素值
    :param image:
    :return:
    '''
    # 灰度图像的高，宽
    rows, cols = image.shape
    # 存储灰度直方图
    grayHist = np.zeros([256], np.uint64)
    for r in range(rows):
        for c in range(cols):
            grayHist[image[r][c]] += 1
    return grayHist


def threshTwoPeaks(image, r, b):
    # 计算灰度直方图
    histogram = calcGrayHist(image)

    # 找到灰度直方图的最大峰值对应的灰度值
    maxLoc = np.where(histogram == np.max(histogram))
    firstPeak = maxLoc[0][0]

    # 寻找灰度直方图的第二个峰值对应的灰度值
    measureDists = np.zeros([256], np.float32)
    for k in range(256):
        measureDists[k] = pow(k - firstPeak, 2) * histogram[k]
    maxLoc2 = np.where(measureDists == np.max(measureDists))
    secondPeak = maxLoc2[0][0]

    # 找两个峰值之间的最小值对应的灰度值，作为阈值
    thresh = 0
    if firstPeak > secondPeak:
        temp = histogram[int(secondPeak): int(firstPeak)]
        minLoc = np.where(temp == np.min(temp))
        thresh = secondPeak + minLoc[0][0] + 1
    else:
        temp = histogram[int(firstPeak): int(secondPeak)]
        minLoc = np.where(temp == np.min(temp))
        thresh = firstPeak + minLoc[0][0] + 1

    # 找到阈值，我们进行处理
    img = image.copy()
    img[img > thresh] = 255
    img[img <= thresh] = 0
    img = cv2.merge([r, img, b])
    cv2.imshow('deal_image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    rgb = cv2.imread(r'C:\Users\14599\Desktop\3.png')
    b, g, r = cv2.split(rgb)
    rgb = cv2.merge([r, g, b])
    rgb1 = rgb
    g = cv2.GaussianBlur(g, (3, 3), 0)
    #g = cv2.blur(g, (3, 3))
    #gray_img = cv2.cvtColor(g, cv2.COLOR_RGB2GRAY)
    threshTwoPeaks(g, r, b)

#https: // blog.csdn.net / shawroad88 / article / details / 87965784
cv2.fastNlMeansDenoising()