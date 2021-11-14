
from __future__ import print_function
import qwiic_joystick
import time
import sys
import time
import board
import busio
import adafruit_mpr121
from tkinter import *

import paho.mqtt.client as mqtt
import uuid





topic = 'IDD/JSP'

def on_connect(client, userdata, flags, rc):
    print(f"connected with result code {rc}")
    client.subscribe(topic)

def on_message(cleint, userdata, msg):
    # function to receive the message
    if msg.topic == topic:
        #print("You pressed the button, fantastic")
        print(msg.payload.decode())

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

# make the window
root = Tk()
root.geometry("600x600")
root['bg'] = ['blue']
root.title("Choose Data")

canvas = Canvas(root, width=1024, height=1024)
canvas.pack() 

xval = 0
yval = 0
width = 64

for x in range(15):
    canvas.create_rectangle((xval*x), (yval*x), (xval*x)+width, (yval*x)+width)

# our main loop To send messages
while True:
    
    strval = ("X: %d, Y: %d, Button: %d" % ( \
                myJoystick.horizontal, \
                                    myJoystick.vertical, \
                                    myJoystick.button))
    
       
    
    
    #client.publish(topic, strval)

    if myJoystick.button == 0:
        client.publish(topic, "Button pressed!")
        #client.publish(topic, strval)
    
    time.sleep(.25)

















