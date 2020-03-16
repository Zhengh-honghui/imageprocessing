from PIL import Image

empire = Image.open('C:/Users/14599/Desktop/bird.png')
empire_1 = empire.convert('P')
empire_1.show()
empire_4 = empire.convert('RGBA')
empire_4.show()
empire_5 = empire.convert('CMYK')
empire_5.show()
empire_6 = empire.convert('YCbCr')
empire_6.show()

empire_0 = empire.convert('F')
empire_0.show()
empire_2 = empire.convert('1')
empire_2.show()
empire_3 = empire.convert('L')
empire_3.show()
empire_7 = empire.convert('I')
empire_7.show()
'''for i in range(7)
    empire_i.show()'''