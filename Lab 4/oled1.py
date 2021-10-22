# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)


 

#oled.setFontType(1)
#oled.setCursor(0,0)
#oled.println("Hello oled")

im = Image.new('RGB', (20,20), (128, 128, 128))
draw = ImageDraw.Draw(im)

draw.line((0,0,10,10), fill=(255, 255, 0), width=5)

#text = "Hello oled"
#oled.draw_text2(0,0,text,2)


oled.show()