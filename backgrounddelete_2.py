import cv2
from skimage import io
import numpy as np

#fname = r"C:\Users\14599\Desktop\数据处理\final CLSM\去除背景\kidney-ecadherin.png"
fname = r"C:\Users\14599\Desktop\1p3-epcam2.png"
img = cv2.imread(fname)

rows, cols, ch = img.shape
SIZE = 3  # 卷积核大小
P = int(SIZE / 2)
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
BEGIN = False
BP = []

for row in range(P, rows - P, 1):
    for col in range(P, cols - P, 1):
        #print(img[row,col])
        if (img[row, col] != BLACK).all():
            kernal = []
            for i in range(row - P, row + P + 1, 1):
                for j in range(col - P, col + P + 1, 1):
                    kernal.append(img[i, j])
                    if (img[i, j] == BLACK).all():
                        BP.append([i, j])


uniqueBP = np.array(list(set([tuple(c) for c in BP])))


for x, y in uniqueBP:
    img[x, y] = WHITE
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#img = cv2.imread(r"C:\Users\14599\Desktop\bird.png")
#img2 = cv2.imread(r"C:\Users\14599\Desktop\second_bird.png")
'''print(img2.shape)
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

mask = cv2.bitwise_and(img, img, mask=img2gray)
cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()'''