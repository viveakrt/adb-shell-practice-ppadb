from config import *

image('sugarcane_crop')
img=Image.open('sugarcane_crop.png')
m2=img.crop((700,250,750,300)).show()
m1=npImage('sugarcane_crop')
d=m1[250:300,700:750]
# npyCreate('sugarcane_crop',d)
