from skimage import exposure, color, io, data
import numpy as np
import cv2
import matplotlib.pyplot as plt
rgb = io.imread(r'C:\Users\14599\Desktop\去除背景\kidney-ecadherin.png')
b,g,r = cv2.split(rgb)
plt.imshow(rgb)
plt.show()

#rgb = io.imread(r'C:\Users\14599\Desktop\p2-ecadherin.tif')
'''img = color.convert_colorspace(rgb, 'RGB', 'HSV') #hsv空间
#HSV空间通道拆分
h = img[:, :, 0]
s = img[:, :, 1]
v = img[:, :, 2]
io.imshow(h) #v通道显示
io.show()
# Adaptive Equalization
img_adapteq = exposure.equalize_adapthist(v, clip_limit=0.03)
  #限制阈值自适应灰度均值结果显示
merge = np.dstack([h, s, img_adapteq])
img_adapteq1 = color.convert_colorspace(merge, 'HSV', 'RGB')'''
#rgb = cv2.merge([r+g,g,b])
#rgb[:,:,1] = 0
#io.imsave(r'C:\Users\14599\Desktop\p2-ecadherin1.png', rgb)
#io.imsave(r'C:\Users\14599\Desktop\p2-ecadherin.png', img_adapteq1)