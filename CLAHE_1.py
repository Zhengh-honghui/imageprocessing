from skimage import exposure, color, io, data
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
path = r"C:\Users\14599\Desktop\数据处理\final CLSM"
img_list = os.listdir(path)
ind = 0
for i in img_list:
  #RGB转化到HSV空中去 ,HSV,分别代表色调，饱和度，明度
  #print(i)
  img = io.imread(os.path.join(path, i))
  img = color.convert_colorspace(img, 'RGB', 'HSV') #hsv空间
  #HSV空间通道拆分
  h = img[:, :, 0]
  s = img[:, :, 1]
  v = img[:, :, 2]
  #io.imshow(v) #v通道显示
  #io.show()
  # Adaptive Equalization
  img_adapteq = exposure.equalize_adapthist(v, clip_limit=0.03)

  #限制阈值自适应灰度均值结果显示
  merge = np.dstack([h, s, img_adapteq])
  img_adapteq1 = color.convert_colorspace(merge, 'HSV', 'RGB')
  #img_adapteq1 = data.chelsea()
  #print(img_adapteq1.dtype.name)

  #img_adapteq1 = np.array(img_adapteq1, dtype = np.uint8)
  savename = i[:-3] + 'png'
  io.imsave(os.path.join(path, savename), img_adapteq1)


'''img_median = cv2.medianBlur(img_adapteq1, 3)
img_bilater = cv2.bilateralFilter(img_adapteq1, 3, 75, 75)

titles = ['ahist' 'median', 'bilateral']
imgs = [img_adapteq1, img_median, img_bilater]

for i in range(3):
    plt.subplot(1,3,i+1)
    #plt.subplot(nrows, ncols, index, **kwargs) 三个整数是行数、列数和索引值
    #注意，这和matlab中类似，没有0，数组下标从1开始
    plt.imshow(imgs[i])
    plt.title(titles[i])
plt.show()'''
#img_cv = cv2.imread(r'C:\Users\14599\Desktop\2.png')
'''img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

dst = cv2.fastNlMeansDenoisingColored(img_cv, None, 10, 10, 7, 21)
plt.imshow(dst)
plt.show()'''


#https://blog.csdn.net/jokertony/article/details/68077233