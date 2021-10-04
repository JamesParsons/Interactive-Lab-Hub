import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import webcolors


# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

#########################################################################

# these setup the code for our buttons and the backlight and tell the pi to treat the GPIO pins as digitalIO vs analogIO
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

####################################################################

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)

#################################################################################
def drawSheep(width, height, sectime):
    
    # format is xstart = start x position.   xend = start position + thickness
    thickness = width * .03
    offset1 = (width * .0125)
    
    if sectime == 4:
        height = height - (height*.1)
    if sectime == 5:
        height = height - (height*.2)
    if sectime == 6:
        height = height - (height*.3)
    if sectime == 7:
        height = height - (height*.2) 
    if sectime == 8:
        height = height - (height*.1)        
    
    # Sheep
    # y+ goes down, x+ goes right
    draw.rectangle(((width*.1125), (height*.63)+thickness, (width*.125), (height*.75)), outline=0, fill=(255,255,255)) #LLeg
    draw.rectangle(((width*.1375),(height*.63)+thickness,(width*.15),(height*.75)), outline=0, fill=(255,255,255)),  #RLeg
    draw.ellipse(((width * .1),(height * .65),(width * .1) + thickness,(height * .65) + thickness), outline=None,fill=(255,255,255)), # LL
    draw.ellipse(((width * .1125),(height * .64),(width * .1125) + thickness,(height * .64) + thickness), outline=None,fill=(255,255,255)), #LM
    draw.ellipse(((width * .125),(height * .65),(width * .125) + thickness,(height * .65) + thickness), outline=None,fill=(255,255,255)), #LR
    draw.ellipse(((width * .1),(height * .60),(width * .1) + thickness,(height * .60) + thickness), outline=None,fill=(255,255,255)), #UL
    draw.ellipse(((width * .1125),(height * .59),(width * .1125) + thickness,(height * .59) + thickness), outline=None,fill=(255,255,255)), #UM
    draw.ellipse(((width * .125),(height * .60),(width * .125) + thickness,(height * .60) + thickness), outline=None,fill=(255,255,255)), #UR
    draw.ellipse(((width * .14),(height * .57),(width * .14) + thickness,(height * .57) + thickness), outline=None,fill=(255,255,255))  # Head
##################################################################################

#############################################################################

def drawFence(width, height, sectime, mintime):
    
    start = (width*.9)
    thickness = width * .03
    offset1 = (width * .0125)    
    
    if sectime == 1:
        start = width - (width*.4)
    if sectime == 2:
        start = width - (width*.5)
    if sectime == 3:
        start = width - (width*.6)
    if sectime == 4:
        start = width - (width*.7) 
    if sectime == 5:
        start = width - (width*.8)
    if sectime == 6:
        start = width - (width*.9)
    if sectime == 7:
        start = width 
    if sectime == 8:
        start = width - (width*.1)
    if sectime == 9:
        start = width - (width*.2)
    if sectime == 0:
        start = width - (width*.3)

        
    if mintime >= 0 and mintime < 58:   
        draw.rectangle(((start), (height*.63), (start + 20), (height*.75)), outline=0, fill=(45,55,195))
   
    if mintime >= 58 and mintime < 60:
    # y+ goes down, x+ goes right
        # Wolf
        draw.rectangle(((width*.1125)+start, (height*.63)+thickness, (width*.125)+start, (height*.75)), outline=0, fill=(115,103,21))
        draw.rectangle(((width*.1375)+start,(height*.63)+thickness,(width*.15)+start,(height*.75)), outline=0, fill=(115,103,21)),
        draw.ellipse(((width * .1)+start,(height * .65),(width * .1)+start + thickness,(height * .65) + thickness), outline=None,fill=(115,103,21)), # LL
        draw.ellipse(((width * .1125)+start,(height * .64),(width * .1125)+start + thickness,(height * .64) + thickness), outline=None,fill=(115,103,21)), #LM
        draw.ellipse(((width * .125)+start,(height * .65),(width * .125)+start + thickness,(height * .65) + thickness), outline=None,fill=(115,103,21)), #LR
        draw.ellipse(((width * .1)+start,(height * .60),(width * .1)+start + thickness,(height * .60) + thickness), outline=None,fill=(115,103,21)), #UL
        draw.ellipse(((width * .1125)+start,(height * .59),(width * .1125)+start + thickness,(height * .59) + thickness), outline=None,fill=(115,103,21)), #UM
        draw.ellipse(((width * .125)+start,(height * .60),(width * .125)+start + thickness,(height * .60) + thickness), outline=None,fill=(115,103,21)), #UR
        draw.ellipse(((width * .09)+start,(height * .57),(width * .09)+start + thickness,(height * .57) + thickness), outline=None,fill=(115,103,21))  # Head       
        
##############################################################

def drawGround(width, height, mintime):
    
    minute = mintime
    ghue = 120
    #want the grass to get brighter green then darker again
    if minute >= 0 and minute < 30:
        ghue = 120 + (minute * 4)
    else:
        midstep = minute - 30
        ghue = 240 - (midstep * 4)
           
  
    #ground
    draw.rectangle((0,(height * .75),width, height),outline=None, fill=(0,ghue,0))
    #sky
    draw.rectangle((0,(0),width, (height*.75)),outline=None, fill=(90,180,225))

##############################################################################
def buttonPressed(width, height, secs, mins, hours, red, green, blue):
       
    wstart = (width * .05)
    hstart = (height * .1)
    wend = wstart + (width * .05)
    hend = hstart + (height * .1)
    
    secpos = (width / 60)  * secs
    minpos = (width / 60) * mins
    hrpos = (width / 24) * hours
            
    #secs, mins, hours blocks
    draw.rectangle((secpos+wstart,hstart,secpos+wend,hend),outline=None, fill=(255,0,0))
    draw.rectangle((minpos+wstart,hstart+(height*.3),minpos+wend,hend+(height*.3)),outline=None, fill=(0,255,0))  
    draw.rectangle((hrpos+wstart,hstart+(height*.8),hrpos+wend,hend+(height*.8)),outline=None, fill=(0,0,255))
    
##############################################################################
    
def drawSun(width, height, hrtime):
    
    # sun gets brighter towards noon, darker towards 6 pm
    if hrtime >= 6 and hrtime < 12:
        shue = 171 + (hrtime * 14)
        draw.ellipse((width*.85,height*-.25,width*1.15,height*.25), outline=None,fill=(shue,shue,0)) 
    if hrtime >= 12 and hrtime < 18:
        midstep = hrtime - 30
        shue = 171 - (midstep * 14)
        draw.ellipse((width*.85,height*-.25,width*1.15,height*.25), outline=None,fill=(shue,shue,0)) 
        
    # moon gets darker towards midnight and brighter towards 6 am
    if hrtime >= 0 and hrtime < 6:
        shue = 158 - (hrtime * 7)
        draw.ellipse((width*.85,height*-.25,width*1.15,height*.25), outline=None,fill=(shue,shue,shue))
        
    if hrtime >= 18 and hrtime < 24:
        hourmidstep = hrtime - 18
        shue = 158 + (hourmidstep * 7)
        draw.ellipse((width*.85,height*-.25,width*1.15,height*.25), outline=None,fill=(shue,shue,shue)) 
    
    #shue = (hrtime *7) + 171  # gets yellow value according to hrtime (it gets brighter)
    #draw.ellipse((width*.85,height*-.25,width*1.15,height*.25), outline=None,fill=(shue,shue,0)), #LR
    
##########################################################

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

####################################################


#####################################################

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=(0,0,0))

    
    # Display image.
    disp.image(image, rotation)
    
    
    
    
