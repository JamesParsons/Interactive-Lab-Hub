
from __future__ import print_function
import qwiic_joystick
import time
import sys
import qwiic
from adafruit_servokit import ServoKit
import board
import busio
import adafruit_ssd1306

# Set channels to the number of servo channels on your kit.
# There are 16 channels on the PCA9685 chip.
kit = ServoKit(channels=16)

# Name and set up the servo according to the channel you are using.
servo = kit.servo[2]

# Set the pulse width range of your servo for PWM control of rotating 0-180 degree (min_pulse, max_pulse)
# Each servo might be different, you can normally find this information in the servo datasheet
servo.set_pulse_width_range(500, 2500)

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)


############# open and close #############

def open_and_close():
    
    # Set the servo to 90 degree position
    servo.angle = 90
    time.sleep(1)
    
    servo.angle = 0
    time.sleep(2) 
    
#################  arrow arriving ##########################
    
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
    
######################  arrow leaving  ##############################
    
def arrow_leaving(xpos):
    
    oled.fill(0)
    
    # wall
    for y in range(32):
        oled.pixel(1,y,255)

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

################ fun with distance ###############################

def distance_fun(distance):
    
    if distance >= 0 and distance <= .3:
        print("within 4 inches")
        
        open_and_close()
        
        
################# come or go ####################################
        
def come_or_go(distances):
    
    if distances[0] < distances[1] and distances[1] < distances[2] and distances[2] < distances[3]:
        print("Leaving")
        for x in range(11,126,5):
            arrow_leaving(x)
            oled.show()
    elif distances[0] > distances[1] and distances[1] > distances[2] and distances[2] > distances[3]:
        print("Approaching")
        for x in range(100,1,-5):
            arrow_arriving(x)
            oled.show()

######################## joystick #############################

def runExample():

    while True:

        ToF.start_ranging()
        distance = ToF.get_distance()	 # Get the result of the measurement from the sensor
        ToF.stop_ranging()

        distanceInches = distance / 25.4
        distanceFeet = distanceInches / 12.0
        
        distances.append(distanceFeet)
        distances.remove(distances[0])

        come_or_go(distances)
        
        distance_fun(distanceFeet)

        time.sleep(.1)

########################################################################

print("VL53L1X Qwiic Test\n")
ToF = qwiic.QwiicVL53L1X()
if (ToF.sensor_init() == None):					 # Begin returns 0 on a good init
    print("Sensor online!\n")


if __name__ == '__main__':
    
    distances = [6,6,6,6,6]
    
    oled.fill(0)
    oled.show()
    
    try:
        runExample()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)




