# James Parsons
# jsp285@cornell.edu

from time import strftime, sleep, time
import time
from PIL import Image, ImageDraw

import numpy as np


if time.time()%10 == 1:
    print("one")


print(time.time())

#if strftime %10 == 1:
    #print("one second!")

img = Image.open("mario.jpg")

background = Image.open("green.jpg")
background.show()

#background.paste(img, (0, 0), img)
#background.save('how_to_superimpose_two_images_01.png',"PNG")


# shows the clock
while True:
    print (strftime("%m/%d/%Y %H:%M:%S"), end="", flush=True)
    print("\r", end="", flush=True)
    sleep(1)
    intime = int(time.time()%10)
    if intime == 1:
        print("One!", time.time())
    
    



















