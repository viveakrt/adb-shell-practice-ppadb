from config import device

# move left
def moveToCroping(i):
    for _ in range(int(i)):
        device.shell('input touchscreen swipe 1000 200 1000 600 800') 
        device.shell('input touchscreen swipe 200 500 1000 500 800')
    device.shell('input touchscreen swipe 1000 500 1000 200 800')