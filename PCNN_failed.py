from PIL import Image
mg = Image.open(r"C:\Users\14599\Desktop\数据处理\IMG_0292.tif")
r, g, b = mg.split()
mg2 = Image.merge('RGB', (r, g, b))
mg = mg.convert('hsv')
mg.show()

"""import numpy as np
import numpy.linalg as lg
M = np.random.ranf((3,3))
print(M)
Mi = lg.inv(M)
print(Mi)
print(np.dot(M,Mi))
#levelset.py
from scipy.signal import cspline2d
def LevelSet(A):
    Aofftarg = A <= 0
    Aontarg = A > 0
    M = cspline2d(Anotarg.astype('d'),70)
    Mofftarg = M * Aofftarg.astype('d')
    Aadd = (Mofftarg.astype('d'>0.5)).astype('d')
    A = A + Aadd
    Aontarg =A > 0
    Aofftarg = 1- Aontarg
    M = cspline2d (Aontarg.astype('d'),70)
    Montarg = M * Aontarg.astype('d') + Aofftarg.astype('d')
    Akill = (Montarg < 0.5).astype('d')
    A = A - Akill
    return A
#icm.py
from numpy import ones, zeros
class ICM:
    f, t1, t2 = 0.9, 0.8, 20.0
    def _init_(self,dim):
        self.F = zeros(dim,float)
        self.Y = zeros(dim,float)
        self.T = ones(dim,float)
    def Interate (self,stim):
        if self.Y.sum() > 0 :
            work = Smooth(self.Y.astype(float),3)
        else:
            work = zeros(self,Y.shape,float)
        self.F = self.f * self.F + stim +8 * work
        self.Y = self.F > self.T
        self.T = self.t1 * self.T + selt.T + self.t2 * self.Y +0.1
    def InterateLS(self,stim):
        if sum(sum(self.Y)) > 10 :
            work = LevelSet(self.Y)
            work = LevelSet(work)
        else:
            work = zeros(self.Y.shape,float)
        self.F = self.f * self.F + stim + work
        self.Y = self.F > self.T
        self.T = self.t1 * self.T +self.t2 * self.Y + 0.1


def AverageFilter(src, dst, k=3, method = "replicate"):
    imarray = np.array(Image.open(src))
    height, width, path = imarray.shape
    new_arr = np.zeros((height, width), dtype="uint8")

    filter = np.ones((k, k))

    for i in range(height):
        for j in range(width):
            total = 0
            for n in range(pow(k, 2)):
                '''
                k = 3, n = 0, 1, 2 ..., 8, a = -1, 0, 1, b = -1, 0, 1
                k = 5, n = 0, 1, 2, 3 ..., 24, a = -2, -1, 0, 1, 2
                '''
                a, b = int(n // k - (k - 1) / 2), int(n % k - 1)
                # filter_value
                aa, bb = int(n // k), int(n % k)
                f_value = filter[aa, bb]
                if i + a <= 0:
                    if j + b <= 0:
                        total += imarray[0, 0] * f_value
                    elif j + b >= width - 1:
                        total += imarray[0, -1] * f_value
                    else:
                        total += imarray[0, j + b] * f_value
                elif i + a >= height - 1:
                    if j + b <= 0:
                        total += imarray[-1, 0] * f_value
                    elif j + b >= width - 1:
                        total += imarray[-1, -1] * f_value
                    else:
                        total += imarray[-1, j + b] * f_value
                else:
                    if j + b <= 0:
                        total += imarray[i + a, 0] * f_value
                    elif j + b >= width - 1:
                        total += imarray[i + a, -1] * f_value
                    else:
                        total += imarray[i + a, j + b] * f_value
            total /= pow(k, 2)
            new_arr[i, j] = int(total)
    new_im = Image.fromarray(new_arr)
    new_im.save(dst)
    new.im.show()

gray_girl = "C:/Users/14599/Desktop/tbsi/数据处理/IMG_0292.tif"
tar = "C:/Users/14599/Desktop/tbsi/数据处理/IMG_0292_fs.tif"
AverageFilter(gray_girl, tar)
data = Image.open("C:/Users/14599/Desktop/tbsi/数据处理/IMG_0292_fs.tif")
Y = []
net = icm.ICM(data,shape)
for i in range(20):
    net.IterateLS(data)
    Y.append(net.Y+0)
mg = Image.fromarray( Y[9] )
"""