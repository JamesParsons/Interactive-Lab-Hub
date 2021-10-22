
from __future__ import print_function
import qwiic_joystick
import time
import sys
import qwiic
from adafruit_servokit import ServoKit
import board
import busio
import adafruit_ssd1306

############################## class feeder #############################

class Feeder:
    
    def __init__(self):
        
        self.d1 = 0
        self.d2 = 0
        self.d3 = 0
        self.within_range = False
        
        # if it is false it can be opened, then should be set to true
        self.valve = False
        
        # arriving = 1, leaving  = 2, neutral = 0
        self.state = 0
        
        self.xpos = 64
        #def open_and_close():
            
        
        
        
#############################################################################
        
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
    #time.sleep(2) 
    
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

        
################# display ####################################
        
def display():
    
    xpos = feeder.xpos
    
    if feeder.state == 1:
        arrow_arriving(xpos)
        feeder.xpos = xpos + 1
    if feeder.state == 2:
        arrow_leaving(xpos)
        feeder.xpos = xpos - 1

######################## distances #############################

def distances():

    ToF.start_ranging()
    distance = ToF.get_distance()	 # Get the result of the measurement from the sensor
    ToF.stop_ranging()
    
    distanceFeet = distance / 304.8
    
    d1 = feeder.d1
    d2 = feeder.d2
    
    feeder.d1 = d2
    feeder.d2 = distanceFeet
    
    d1 = feeder.d1
    d2 = feeder.d2

    if d1 < d2:
        feeder.state = 1    
    elif d1 > d2:
        feeder.state = 2
    else:
        feeder.state = 0
        
    
    if feeder.valve == False and distanceFeet <= .3:
        print("open valve")
        open_and_close()
        feeder.valve = True
    

########################################################################

print("VL53L1X Qwiic Test\n")
ToF = qwiic.QwiicVL53L1X()
if (ToF.sensor_init() == None):					 # Begin returns 0 on a good init
    print("Sensor online!\n")


if __name__ == '__main__':
    
    #distances = [6,6,6]
    
    oled.fill(0)
    oled.show()
    
    feeder = Feeder()
    
    while True:
        
        distances() 
        display()
   
        print(feeder.d1, feeder.d2, feeder.state)
        
        time.sleep(.1)
