from skimage import exposure, color, io, data
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
path = r"C:\Users\14599\Desktop\数据处理\final CLSM\bgr"
img_list = os.listdir(path)
for i in img_list:

  rgb = io.imread(os.path.join(path, i))
  r, g, b = cv2.split(rgb)
  rgb = cv2.merge([g,r,b])
  io.imshow(rgb)
  io.show()
  if i[-3:] == 'tif':
      savename = i[:-4] + '1'+'.png'
  else:
      savename = i[:-4] + '2'+'.png'
  io.imsave(os.path.join(path, savename), rgb)

'''from PIL import Image
i = 1
j = 1
img = Image.open("F:/myworkspace/image/1.jpg")#读取系统的内照片
print (img.size)#打印图片大小
width = img.size[0]#长度
height = img.size[1]#宽度
f = open('F:/myworkspace/image/log.txt','a+')#保存一下图片像素看一下
for i in range(0,width):#遍历所有长度的点
    for j in range(0,height):#遍历所有宽度的点
        data = (img.getpixel((i,j)))#打印该图片的所有点
        f.write(str(data)+"("+str(i)+","+str(j)+")\n")#看一下像素
        print (str(data))#打印每个像素点的颜色RGBA的值(r,g,b,alpha)
        if ((230<data[0]<250 and 170<data[1]<185 and 170<data[2]<190)or(180<data[0]<210 and 110<data[1]<130 and 120<data[2]<140)):#RGBA的r值大于170，并且g值大于170,并且b值大于170
            #判断条件就是一个像素范围范围
            # img.putpixel((i,j),(0,255,0))#则这些像素点的颜色改成绿色
            img.putpixel((i, j), (0, 128, 255))  # 则这些像素点的颜色改成蓝色
f.close()
img = img.convert("RGB")#把图片强制转成RGB
img.save("F:/myworkspace/image/5.jpg")#保存修改像素点后的图片'''
