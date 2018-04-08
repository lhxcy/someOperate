import PIL
from PIL import Image,ImageGrab
import os

im = ImageGrab.grab()
# or call im.show() to view the image directly
im.save("e:/screenshot.png")#保存图片
#os.execvp( "mspaint",('mspaint','c:/screenshot.png'))#调用画图程序打开截屏图片
im1=Image.open("e:/screenshot.png")
print(im1.size)

rec=([400,400,800,800])
region=im1.crop(rec)
region.show()
region.save("e:/123.bmp")
