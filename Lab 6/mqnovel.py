
from __future__ import print_function
import time
import sys
import time
#import board
#import busio
#import adafruit_mpr121

import paho.mqtt.client as mqtt
import uuid


topic = 'IDD/MVP'

novel = ""

def on_connect(client, userdata, flags, rc):
    print(f"connected with result code {rc}")
    client.subscribe(topic)

def on_message(cleint, userdata, msg):
    
    global novel
    # function to receive the message
    if msg.topic == topic:
        #print(msg.payload.decode())
        novel = novel + " " + msg.payload.decode() + ". "
        print(novel)

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
    
i = 0

# our main loop To send messages
while True:
    
    if i == 0:
        player = "Mahir"
    elif i == 1:
        player = "Victoria"
    elif i == 2:
        player = "James"
    
    if i == 2:
        i = 0
    else:
        i = i + 1
        
    
    line = input(f"{player}: ")
    #print(line)
    
    client.publish(topic, line)
    
    time.sleep(5)
       
    
    
