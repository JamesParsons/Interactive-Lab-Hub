
from __future__ import print_function
import qwiic_joystick
import time
import sys
import qwiic

################ fun with distance ###############################

def distance_fun(distance):
    
    if distance >= 0 and distance <= 100:
        print("between zero and 100")
    


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

        distance_fun(distanceInches)

        print("Distance(mm): %s Distance(ft): %s" % (distance, distanceFeet))        

        print("X: %d, Y: %d, Button: %d" % ( \
            myJoystick.horizontal, \
                    myJoystick.vertical, \
                                        myJoystick.button))

        time.sleep(.5)

########################################################################

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




