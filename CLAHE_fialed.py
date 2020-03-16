from PIL import Image
from skimage import exposure, color, io, img_as_ubyte
import numpy as np
import matplotlib.pyplot as plt
img = Image.open(r'C:\Users\14599\Desktop\数据处理\IMG_0292.TIF')
img = np.array(img)
#直方图均衡
#img_eq = exposure.equalize_hist(img)
#限制对比度自适应直方图均衡
img_adapteq = exposure.equalize_adapthist(img, clip_limit=0.02)
#分成三个通道进行均值(失败了，可能是分通道是不行的？）
#r, g, b = img.split()
#hsv = color.convert_colorspace(img, 'RGB', 'HSV') #hsv空间
#hsv1 = np.array(hsv)
#img1 = exposure.equalize_adapthist(hsv1, clip_limit=0.03)
#img_eq = exposure.equalize_hist(hsv1)
''''#绘制直方图
imgg = np.array(img)
hist1 = exposure.histogram(imgg, nbins=2)
plt.figure("hist")
arr = imgg.flatten()
n, bins, patches = plt.hist(arr, bins=10)
plt.show()

hist2 = exposure.histogram(img1, nbins=2)
plt.figure("hist")
arr = img1.flatten()
n, bins, patches = plt.hist(arr, bins=10)
plt.show()
'''
io.imshow(img_adapteq)
io.show()
'''
io.imshow(img1)
io.show()
img1 = img_as_ubyte(img1)
img2 = img_as_ubyte(img_eq)
rgb = color.convert_colorspace(img1, 'HSV', 'RGB')
rgb1 = color.convert_colorspace(img_eq, 'HSV', 'RGB')
io.imshow(rgb1)
io.show()
io.imshow(rgb)
io.show()
''''''
r1 = np.array(r)
g1 = np.array(g)
b1 = np.array(b)
r_adapteq = exposure.equalize_adapthist(r1, clip_limit=0.03)
g_adapteq = exposure.equalize_adapthist(g1, clip_limit=0.03)
b_adapteq = exposure.equalize_adapthist(b1, clip_limit=0.03)
rmg = Image.fromarray(r_adapteq)
gmg = Image.fromarray(g_adapteq)
bmg = Image.fromarray(b_adapteq)
mg2 = Image.merge('RGB', (rmg, gmg, bmg))
mg2.show()'''
''''#绘制cdf图 累积分布函数(还未解决）
plt.figure("cdf")
img_cdf = exposure.cumulative_distribution(img_adapteq, nbins=256)
n, bins, patches = plt.hist(img_cdf, bins=10)
plt.show()'''

#绘制直方图
'''hist2=exposure.histogram(img, nbins=2)
print(hist2)
plt.figure("hist")
arr=img.flatten()
n, bins, patches = plt.hist(arr, bins=10)
plt.show()

plt.figure("hist")
arr=img_adapteq.flatten()
n, bins, patches = plt.hist(arr, bins=10)
plt.show()'''

'''plt.figure(0)
plt.imshow(img)
plt.title('Figure 0 low contrast image')
plt.show()
plt.figure(1)
plt.imshow(img_eq)
plt.title('Figure 1 high constrast image using normal histogram equalization')
plt.show()'''

'''#限制对比度自适应直方图均衡处理后图像
plt.figure(2)
plt.imshow(img_adapteq)
plt.title('Figure 2 high constract image using adaptive histogram euqalization')
plt.show()'''