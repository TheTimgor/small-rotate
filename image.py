from time import process_time
from PIL import Image
from rotate import *

size = 1000

im = Image.open('test.jpg')
width, height = im.size
width, height = int(size/height*width), size
im = im.resize((width, height))
im.show()
data = list(im.getdata())
start = process_time()
rdata = fast_rot(width, height, data)
print('rotate time: ', process_time()-start)
rim = Image.new('RGB', (height, width))
rim.putdata(rdata)
rim.show()

