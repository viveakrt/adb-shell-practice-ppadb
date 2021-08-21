#!/usr/bin/env python3

from ppadb.client import Client
from PIL import Image
import numpy
import time


adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

def image(i):
    image = device.screencap()
    with open(str(i)+'.png', 'wb') as f:
        f.write(image)
def getImage(i):
    image = Image.open(str(i)+'.png')
    image = numpy.array(image, dtype=numpy.uint8)
    return image

print(getImage(1)[638][1141])

# imag = Image.open('news.png')
# imag = numpy.array(imag, dtype=numpy.uint8)
# print(imag)

# device.shell('input touchscreen tap 1000 465')
# device.shell('input touchscreen swipe 858 330 1462 688 2000')
# # device.shell('input touchscreen swipe 1000 465 1462 688 2000')
# time.sleep(121)
# device.shell('input touchscreen swipe 758 330 1462 688 2000')