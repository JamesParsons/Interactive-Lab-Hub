
#from __future__ import print_function
#import qwiic_joystick
#import time
#import sys
#import qwiic
from adafruit_servokit import ServoKit
import board
import busio
#import adafruit_ssd1306
from sshkeyboard import listen_keyboard




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
#oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)


############# open and close #############

def open_and_close():
    
    # Set the servo to 90 degree position
    servo.angle = 90
    time.sleep(1)
    
    servo.angle = 0
    #time.sleep(2) 
   
#################  get key presses  ######################   
    
def press(key):
    print(f"'{key}' pressed")
    if key == 'up':
        servo.angle = 50
    if key == 'down':
        servo.angle = 0
        
        

def release(key):
    print(f"'{key}' released")
    servo.angle = 25


servo.angle = 25
listen_keyboard(
    on_press=press,
    on_release=release,
)













