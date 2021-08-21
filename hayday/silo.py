from config import *
from PIL import ImageChops
import time

def wheat():  # sourcery skip: extract-method
    image('silo_shop')
    data = npImage('silo_shop')
    wheat = data[250:300,700:750]

    wheatCrop = npyOpen('sugarcane_crop')

    if not np.count_nonzero(wheat-wheatCrop):
        device.shell('input touchscreen tap 750 250')
        device.shell('input touchscreen tap 1700 525')
        if not (data[875,1400,2]):
            device.shell('input touchscreen tap 1450 725')
        device.shell('input touchscreen tap 1600 1000')
        

def swipeLeftShop():
    device.shell('input touchscreen swipe 1338 850 612 850 5000')
    device.shell('input touchscreen swipe 1338 850 612 850 5000')

def isZeroNp(size,data):
    return size-np.count_nonzero(data)

def sellWheat():  # sourcery skip: extract-duplicate-method
    image('roadside_shop')
    roadsideShope=npImage('roadside_shop')
    p1=roadsideShope[690,350:670,:3]
    p2=roadsideShope[690,710:1030,:3]
    p3=roadsideShope[690,1080:1400,:3]
    p4=roadsideShope[690,1435:1755,:3]

    for _ in range(10):
        if isZeroNp(1280,p1) < 10:
            device.shell('input touchscreen tap 515 505')
        device.shell('input touchscreen tap 515 505')
        wheat()
        if isZeroNp(1280,p2) < 10:
            device.shell('input touchscreen tap 865 505')
        device.shell('input touchscreen tap 865 505')
        wheat()
        if isZeroNp(1280,p3) < 10:
            device.shell('input touchscreen tap 1240 505')
        device.shell('input touchscreen tap 1240 505')
        wheat()
        if isZeroNp(1280,p4) < 10:
            device.shell('input touchscreen tap 1600 505')
        device.shell('input touchscreen tap 1600 505')
        wheat()
        swipeLeftShop()
sellWheat()

# money = data[690]

# print(data[875,1400,2])
# print(wheat)
# print(np.count_nonzero(wheat-wheatCrop))


# image('hayday')
# m1 = Image.open('hayday.png')
# # m2=m1.crop((700,250,750,300))
# d = npImage('hayday')
# m2.save('wheat_crop.png')
# firstcroplocation.crop((700,250,750,350)).show()
#secondcroplocation.crop((1018,250,1068,300))
# data = npImage()

# p1=d[690,350:670,:3]
# p2=d[690,710:1030,:3]
# p3=d[690,1080:1400,:3]
# p4=d[690,1435:1755,:3]
# # print(p1)
# # print(len(p1))
# zero_els = len(p1)*3 - np.count_nonzero(p1)
# print(zero_els)
# zer = len(p2)*3 - np.count_nonzero(p2)
# print(zer)

# z = len(p3)*3 - np.count_nonzero(p3)
# print(z)

# ze = len(p4)*3 - np.count_nonzero(p4)
# print(ze)