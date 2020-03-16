from PIL import Image
from skimage import exposure, color, io
import numpy as np
import cv2
import matplotlib.pyplot as plt
img = io.imread(r'C:\Users\14599\Desktop\数据处理\IMG_0291.TIF')
'''#原图直方图显示
hist1 = exposure.histogram(img, nbins=256)
plt.figure("hist")
arr = img.flatten()
n, bins, patches = plt.hist(arr, bins=256)
plt.show()'''
#RGB转化到HSV空间中去 ,HSV,分别代表色调，饱和度，明度
img = color.convert_colorspace(img, 'RGB', 'HSV') #hsv空间
#HSV空间通道拆分
h = img[:, :, 0]
s = img[:, :, 1]
v = img[:, :, 2]
#io.imshow(v) v通道显示
#io.show()

#Histogram Equalization
img_eq = exposure.equalize_hist(v)
# Adaptive Equalization
img_adapteq = exposure.equalize_adapthist(v, clip_limit=0.05)

#灰度均值结果显示
'''merge = np.dstack([h, s, img_eq])#通道合并
img_eq1 = color.convert_colorspace(merge, 'HSV', 'RGB')
io.imshow(img_eq1)
io.show()'''

#直方图显示
hist1 = exposure.histogram(img_adapteq, nbins=256)
plt.figure("hist")
arr = img_adapteq.flatten()
n, bins, patches = plt.hist(arr, bins=256)
plt.show()

#限制阈值自适应灰度均值结果显示
merge = np.dstack([h, s, img_adapteq])
img_adapteq1 = color.convert_colorspace(merge, 'HSV', 'RGB')
io.imshow(img_adapteq1)
io.show()






'''#CLAHE后图像直方图显示
hist1 = exposure.histogram(img_adapteq1, nbins=256)
plt.figure("hist")
arr = img_adapteq1.flatten()
n, bins, patches = plt.hist(arr, bins=256)
plt.show()'''