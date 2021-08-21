from config import *
from PIL import ImageChops

def connectionLost():
    image('hayday')
    data = npImage('hayday')

    tryAgain = data[1000][700:1600]
    with open('try_again.npy','rb') as f:
        a = np.load(f)
    rs =a-tryAgain
    rsc=np.count_nonzero(rs)
    print(rsc)
    return (rsc < 300)


# with open('try_again.npy','wb') as f:
#     np.save(f,data[1000][700:1600])
# # m1 = Image.open('hayday.png')
# # m2=m1.crop((1000,950,1300,1050))
# # m2.save('compare.png')
# compare = Image.open('compare.png')
# try_again = Image.open('try_again.png')

# diff = ImageChops.difference(compare, try_again)
# # return not diff.getbbox()
# # diff.show()
# print(diff.getbbox())
# if diff.getbbox():
#     diff.show()