# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import busio
import adafruit_ssd1306
import time


# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)



def arrow_arriving(xpos):
    
    oled.fill(0)
    
    # wall
    for y in range(32):
        oled.pixel(1,y,255)

    # arrow flange up
    oled.pixel(xpos+4, 11, 255)
    oled.pixel(xpos+3, 12, 255)
    oled.pixel(xpos+2, 13, 255)
    oled.pixel(xpos+1, 14, 255)
    oled.pixel(xpos, 15, 255)
    
    # arrow flange down
    oled.pixel(xpos+1, 16, 255)
    oled.pixel(xpos+2, 17, 255)
    oled.pixel(xpos+3, 18, 255)
    oled.pixel(xpos+4, 19, 255)
    
    # arrow shaft
    oled.pixel(xpos+1, 15, 255)
    oled.pixel(xpos+2, 15, 255)
    oled.pixel(xpos+3, 15, 255)
    oled.pixel(xpos+4, 15, 255)
    oled.pixel(xpos+5, 15, 255)
    oled.pixel(xpos+6, 15, 255)
    oled.pixel(xpos+7, 15, 255)
    oled.pixel(xpos+8, 15, 255)
    oled.pixel(xpos+9, 15, 255)
    oled.pixel(xpos+10, 15, 255)
    
    oled.show()
    
def arrow_leaving(xpos):
    
    oled.fill(0)
    
    # wall
    for y in range(32):
        oled.pixel(127,y,255)

    # arrow flange up
    oled.pixel(xpos-4, 11, 255)
    oled.pixel(xpos-3, 12, 255)
    oled.pixel(xpos-2, 13, 255)
    oled.pixel(xpos-1, 14, 255)
    oled.pixel(xpos, 15, 255)
    
    # arrow flange down
    oled.pixel(xpos-1, 16, 255)
    oled.pixel(xpos-2, 17, 255)
    oled.pixel(xpos-3, 18, 255)
    oled.pixel(xpos-4, 19, 255)
    
    # arrow shaft
    oled.pixel(xpos-1, 15, 255)
    oled.pixel(xpos-2, 15, 255)
    oled.pixel(xpos-3, 15, 255)
    oled.pixel(xpos-4, 15, 255)
    oled.pixel(xpos-5, 15, 255)
    oled.pixel(xpos-6, 15, 255)
    oled.pixel(xpos-7, 15, 255)
    oled.pixel(xpos-8, 15, 255)
    oled.pixel(xpos-9, 15, 255)
    oled.pixel(xpos-10, 15, 255)
    
    oled.show()
    
# start with a blank screen
oled.fill(0)
# we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
oled.show()
while True:
    
    #oled.pixel(10,10,255)
    
    #for x in range(100,1,-5):
        #arrow_arriving(x)
        #oled.show()
  
    
    for x in range(0,126,5):
        arrow_leaving(11)
        oled.show()
    
    
    oled.show()