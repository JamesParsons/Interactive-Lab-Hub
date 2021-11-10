from __future__ import print_function
import qwiic_joystick
import time
import sys
import time
import board
import busio
import adafruit_mpr121

import paho.mqtt.client as mqtt
import uuid

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

topic = 'IDD/your/topic/here'

i2c = busio.I2C(board.SCL, board.SDA)

#mpr121 = adafruit_mpr121.MPR121(i2c)

#while True:
    #for i in range(12):
        #if mpr121[i].value:
            #val = f"Twizzler {i} touched!"
            #print(val)
            #client.publish(topic, val)
    #time.sleep(0.25)
    
    
    
    
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

        print("X: %d, Y: %d, Button: %d" % ( \
                    myJoystick.horizontal, \
                                        myJoystick.vertical, \
                                        myJoystick.button))
        
        strval = ("X: %d, Y: %d, Button: %d" % ( \
                    myJoystick.horizontal, \
                                        myJoystick.vertical, \
                                        myJoystick.button))
        
        #for i in range(12):
            #if mpr121[i].value:
        #val = f"Twizzler {i} touched!"
        print(strval)
        client.publish(topic, strval)        

        time.sleep(.1)
    
if __name__ == '__main__':
    try:
        runExample()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)    
    
    
        #while True:
            #for i in range(12):
                #if mpr121[i].value:
                    #val = f"Twizzler {i} touched!"
                    #print(val)
                    #client.publish(topic, val)
            #time.sleep(0.25)
        
    
    
    
    
    