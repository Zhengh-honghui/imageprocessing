import numpy as np
import cv2
import matplotlib.pyplot as plt
filePath = r'C:\Users\14599\Desktop\3.png'
img = cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)
dst = cv2.fastNlMeansDenoisingColored(img, None, 10,10,7,21)
img_bilater = cv2.bilateralFilter(img, 9, 30, 30)

plt.subplot(131), plt.imshow(img)
plt.subplot(132), plt.imshow(dst)
#lt.subplot(133), plt.imshow(img_bilater)
plt.show()

#https://blog.csdn.net/qq_38410428/article/details/93046099