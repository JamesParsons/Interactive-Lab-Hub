# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import busio
import adafruit_ssd1306


# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)


# Helper function to draw a circle from a given position with a given radius
# This is an implementation of the midpoint circle algorithm,
# see https://en.wikipedia.org/wiki/Midpoint_circle_algorithm#C_example for details
def arr(xpos):
    
    oled.pixel(11,11,255)
    
    oled.pixel(xpos-4, 11, 255)
    oled.pixel(xpos-3, 12, 255)
    oled.pixel(xpos-2, 13, 255)
    oled.pixel(xpos-1, 14, 255)
    oled.pixel(xpos, 15, 255)
    
    oled.pixel(xpos+1, 16, 255)
    oled.pixel(xpos+2, 17, 255)
    oled.pixel(xpos+3, 18, 255)
    oled.pixel(xpos+4, 19, 255)
    
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
    
    
    
    
    
# start with a blank screen
oled.fill(0)
# we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
oled.show()
while True:
    
    oled.pixel(10,10,255)
    
    for x in range(10, 0, 1):
        arr(x)
        sleep(.1)
        oled.show()
    
    oled.show()