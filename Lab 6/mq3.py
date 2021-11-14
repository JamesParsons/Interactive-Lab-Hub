from __future__ import print_function
import os
import subprocess
from time import sleep
import board
import numpy as np
#import cv2
import busio
import qwiic

import paho.mqtt.client as mqtt
import uuid




topic = 'IDD/MVP'
# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

def distances():       

    ToF.start_ranging()
    distance = ToF.get_distance()	 # Get the result of the measurement from the sensor
    ToF.stop_ranging()
    
    distanceFeet = distance / 304.8 
    
    print("distance to edge: ", distanceFeet)
    
    return distanceFeet


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


while True:

        ToF = qwiic.QwiicVL53L1X()
        if (ToF.sensor_init() == None):					 # Begin returns 0 on a good init
                print("Sensor online!\n") 

        distance = distances()
        
        client.publish(topic, distance)
        
        sleep(5)













