# from tasks.takePosition import *

from ppadb.client import Client
from PIL import Image
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize) 


adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

def image(name):
    image = device.screencap()
    with open(name+'.png', 'wb') as f:
        f.write(image)


def npImage(name):
    image = Image.open(name+'.png')
    image = np.array(image, dtype=np.uint8)
    return image

def npyCreate(name,data):
    with open(name+'.npy','wb') as f:
        np.save(f,data)

def npyOpen(name):
    with open(name+'.npy','rb') as f:
        d = np.load(f)
    return d