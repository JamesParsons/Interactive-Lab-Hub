
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





topic = 'IDD/JSP'

def on_connect(client, userdata, flags, rc):
    print(f"connected with result code {rc}")
    client.subscribe(topic)

def on_message(cleint, userdata, msg):
    # if a message is recieved on the colors topic, parse it and set the color
    if msg.topic == topic:
        print("You pressed the button, fantastic")

client = mqtt.Client(str(uuid.uuid1()))
client.tls_set()
client.username_pw_set('idd', 'device@theFarm')
client.on_connect = on_connect
client.on_message = on_message

client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

client.loop_start()

# this lets us exit gracefully (close the connection to the broker)
def handler(signum, frame):
    print('exit gracefully')
    client.loop_stop()
    exit (0)

# when sigint happens, do the handler callback function
#signal.signal(signal.SIGINT, handler)

myJoystick = qwiic_joystick.QwiicJoystick()
myJoystick.begin()

# our main loop
while True:
    
    strval = ("X: %d, Y: %d, Button: %d" % ( \
                myJoystick.horizontal, \
                                    myJoystick.vertical, \
                                    myJoystick.button))
    
    
    client.publish(topic, strval)

    if myJoystick.button == 0:
        client.publish(topic, "Button pressed!")
        #client.publish(topic, strval)
    
    time.sleep(.1)

















