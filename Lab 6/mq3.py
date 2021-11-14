import os
import subprocess
from time import sleep
from vosk import Model, KaldiRecognizer
import sys
import os
import wave
import json
import board
import digitalio
#from adafruit_apds9960.apds9960 import APDS9960
from __future__ import print_function
import busio
import adafruit_mpr121

import paho.mqtt.client as mqtt
import uuid




topic = 'IDD/MVP'

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


#subprocess.run(['arecord', '-D', 'hw:3,0', '-f', 'cd', '-c1', '-r', '48000', '-d', '5', '-t', 'wav', 'recorded_mono.wav'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
audio = subprocess.run(['arecord', '-D', 'hw:3,0', '-f', 'cd', '-c1', '-r', '48000', '-d', '5', '-t', 'wav', 'recorded_mono.wav'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


client.publish(topic, audio)


