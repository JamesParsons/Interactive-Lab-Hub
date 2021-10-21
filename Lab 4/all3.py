# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import busio
import adafruit_ssd1306
from __future__ import print_function
import qwiic_joystick
import time
import sys
import qwiic


# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)




# start with a blank screen
oled.fill(0)
# we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
oled.show()

######################## joystick #############################

def runExample():

    print("\nSparkFun qwiic Joystick   Example 1\n")
    myJoystick = qwiic_joystick.QwiicJoystick()

    if myJoystick.connected == False:
        print("The Qwiic Joystick device isn't connected to the system. Please check your connection", \
              file=sys.stderr)
        return

    myJoystick.begin()

    print("Initialized. Firmware Version: %s" % myJoystick.version)

    while True:

        ToF.start_ranging()
        #myJoystick.begin()
        # Write configuration bytes to initiate measurement
        #time.sleep(.1)
        distance = ToF.get_distance()	 # Get the result of the measurement from the sensor
        #time.sleep(.1)
        ToF.stop_ranging()

        distanceInches = distance / 25.4
        distanceFeet = distanceInches / 12.0

        print("Distance(mm): %s Distance(ft): %s" % (distance, distanceFeet))        

        print("X: %d, Y: %d, Button: %d" % ( \
            myJoystick.horizontal, \
                    myJoystick.vertical, \
                                        myJoystick.button))
        
        
        if distances[0] < distances[1] and distances[1] < distances[2] and distances[2] < distances[3]:
            print("Leaving")
        elif distances[0] > distances[1] and distances[1] > distances[2] and distances[2] > distances[3]:
            print("Approaching")        

        oled.show()

        time.sleep(.5)

########################################################################

    #oled.show()
    
    
    
    


print("VL53L1X Qwiic Test\n")
ToF = qwiic.QwiicVL53L1X()
if (ToF.sensor_init() == None):					 # Begin returns 0 on a good init
    print("Sensor online!\n")
    
    
    
if __name__ == '__main__':
    try:
        runExample()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)
    
    
    
    
    
    
