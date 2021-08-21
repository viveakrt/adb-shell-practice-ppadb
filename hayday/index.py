from takePosition import *
from config import device
from panel import *

# moveToCroping(2)

# device.shell('input touchscreen tap 1000 465')
# device.shell('input draganddrop 830 360 104 650 2000')

# if connectionLost():
#     print('Clicked')
#     device.shell('input touchscreen tap 1140 1000')
device.shell("sendevent /dev/input/event2 1 330 1")     # Puts down finger
device.shell("sendevent /dev/input/event2 3 57 10")     # Sets pressure
device.shell("sendevent /dev/input/event2 3 53 150")    # Sets X to 100
device.shell("sendevent /dev/input/event2 3 54 150")    # Sets Y to 230
device.shell("sendevent /dev/input/event2 0 0 0")       # "0 0 0" (its called a SYN_REPORT)
device.shell("sendevent /dev/input/event2 1 330 0")     # Lift up finger
device.shell("sendevent /dev/input/event2 0 0 0")  
device.shell("sendevent /dev/input/event2 1 330 1")
device.shell("sendevent /dev/input/event2 3 57 10")
device.shell("sendevent /dev/input/event2 3 53 200")
device.shell("sendevent /dev/input/event2 3 54 200")
device.shell("sendevent /dev/input/event2 0 0 0")
device.shell("sendevent /dev/input/event2 3 53 200")
device.shell("sendevent /dev/input/event2 3 54 300")
device.shell("sendevent /dev/input/event2 0 0 0")
device.shell("sendevent /dev/input/event2 3 53 300")
device.shell("sendevent /dev/input/event2 3 54 300")
device.shell("sendevent /dev/input/event2 0 0 0")
device.shell("sendevent /dev/input/event2 1 330 0")
device.shell("sendevent /dev/input/event2 0 0 0")