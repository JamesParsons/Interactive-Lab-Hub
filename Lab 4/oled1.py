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


 

#oled.setFontType(1)
#oled.setCursor(0,0)
#oled.println("Hello oled")

text = "Hello oled"
oled.draw_text2(0,0,text,2)


oled.show()