#思路1尝试用开运算消除g通道（目前在r通道里面的噪点）
import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage import io
img = io.imread(r"C:\Users\14599\Desktop\数据处理\final CLSM\去除背景\kidney-ecadherin.png")

b, g, r = cv2.split(img)
gray_res = r
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
closed1 = cv2.morphologyEx(gray_res, cv2.MORPH_CLOSE, kernel,iterations=1)    #闭运算1
closed2 = cv2.morphologyEx(gray_res, cv2.MORPH_CLOSE, kernel,iterations=3)    #闭运算2
opened1 = cv2.morphologyEx(gray_res, cv2.MORPH_OPEN, kernel,iterations=1)     #开运算1
opened2 = cv2.morphologyEx(gray_res, cv2.MORPH_OPEN, kernel,iterations=3)     #开运算2
gradient = cv2.morphologyEx(gray_res, cv2.MORPH_GRADIENT, kernel)             #梯度

plt.imshow(cv2.merge([closed2,g,b]))
plt.show()
#显示如下腐蚀后的图像
cv2.imshow("gray_res", r)
cv2.imshow("Close1", closed1)#cv2.merge(closed1,g,b)
cv2.imshow("Close2", closed2)#cv2.merge(closed2,g,b)
cv2.imshow("Open1", opened1)#cv2.merge(opened1,g,b)
cv2.imshow("Open2", opened2)#cv2.merge(opened2,g,b)
cv2.imshow("gradient", gradient)#cv2.merge(gradient,g,b)

cv2.waitKey(0)
cv2.destroyAllWindows()

#原文链接：https://blog.csdn.net/wsp_1138886114/article/details/82917661
