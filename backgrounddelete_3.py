import cv2
import matplotlib.pyplot as plt
from skimage import io,color
fname = r"C:\Users\14599\Desktop\p2-ecadherin.png"
fname1 = r"C:\Users\14599\Desktop\p2-ecadherin_second.png"

img = cv2.imread(fname)
b, g, r = cv2.split(img)
img = cv2.merge([r, g, b])
img2 = cv2.imread(fname1)


img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

mask = cv2.bitwise_and(img, img, mask=img2gray)
plt.imshow(mask)
plt.show()
io.imsave(r"C:\Users\14599\Desktop\p2-ecadherin_final.png", mask)