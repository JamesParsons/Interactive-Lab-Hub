
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

################ fun with distance ###############################

def distance_fun(distance):
    
    if distance >= 0 and distance <= .3:
        print("within 4 inches")
        
        # Set the servo to 45 degree position
        servo.angle = 45
        time.sleep(2)
        
        servo.angle = 0
        time.sleep(2)        
        
################# come or go ####################################
        
def come_or_go(distances):
    
    if distances[0] < distances[1] and distances[1] < distances[2] and distances[2] < distances[3]:
        print("Leaving")
    elif distances[0] > distances[1] and distances[1] > distances[2] and distances[2] > distances[3]:
        print("Approaching")
    


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
        distance = ToF.get_distance()	 # Get the result of the measurement from the sensor
        ToF.stop_ranging()

        distanceInches = distance / 25.4
        distanceFeet = distanceInches / 12.0
        
        distances.append(distanceFeet)
        distances.remove(distances[0])
        
        #print("distances ", distances)

        come_or_go(distances)
        
        distance_fun(distanceFeet)

        #print("Distance(mm): %s Distance(ft): %s" % (distance, distanceFeet))        

        #print("X: %d, Y: %d, Button: %d" % ( \
            #myJoystick.horizontal, \
                    #myJoystick.vertical, \
                                        #myJoystick.button))

        time.sleep(.5)

########################################################################

print("VL53L1X Qwiic Test\n")
ToF = qwiic.QwiicVL53L1X()
if (ToF.sensor_init() == None):					 # Begin returns 0 on a good init
    print("Sensor online!\n")


if __name__ == '__main__':
    
    distances = [6,6,6,6,6]
    
    try:
        runExample()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)




