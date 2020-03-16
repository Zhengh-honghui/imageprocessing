import cv2
from skimage import io
import numpy as np
import matplotlib.pyplot as plt

#fname = r"C:\Users\14599\Desktop\数据处理\final CLSM\去除背景\kidney-ecadherin.png"
fname = r"C:\Users\14599\Desktop\p3-epcam2.png"
img = cv2.imread(fname)
#b, g, r = cv2.split(img)
#img = cv2.merge([r, g, b])
img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
c_canny_img = cv2.Canny(img2gray, 50, 150)
cv2.imshow("img", c_canny_img)
cv2.waitKey(0)
#print(c_canny_img.shape)
'''cv2.imshow('mask', c_canny_img)
k = cv2.waitKey(500) & 0xFF
if k == 27:
   cv2.destroyAllWindows()'''
'''img = c_canny_img
rows, cols = img.shape
SIZE = 3  # 卷积核大小
P = int(SIZE / 2)
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
BEGIN = False
BP = []

for row in range(P, rows - P, 1):
    for col in range(P, cols - P, 1):
        # print(img[row,col])
        if (img[row, col] == WHITE).all():
            kernal = []
            for i in range(row - P, row + P + 1, 1):
                for j in range(col - P, col + P + 1, 1):
                    kernal.append(img[i, j])
                    if (img[i, j] == BLACK).all():
                        # print(i,j)
                        BP.append([i, j])

uniqueBP = np.array(list(set([tuple(c) for c in BP])))
for x, y in uniqueBP:
    img[x, y] = [255, 255, 255]
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

