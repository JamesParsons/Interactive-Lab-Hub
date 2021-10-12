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
from adafruit_apds9960.apds9960 import APDS9960

# for gestures and proximity
i2c = board.I2C()
int_pin = digitalio.DigitalInOut(board.D5)
apds = APDS9960(i2c, interrupt_pin=int_pin)

apds.enable_proximity = True
apds.proximity_interrupt_threshold = (0, 250)
apds.enable_proximity_interrupt = True

apds.enable_color = True
apds.enable_gesture = True
gesture = apds.gesture()

#while gesture == 0:
    #gesture = apds.gesture()
#print('Saw gesture: {0}'.format(gesture))


#while True:
subprocess.run(['arecord', '-D', 'hw:3,0', '-f', 'cd', '-c1', '-r', '48000', '-d', '5', '-t', 'wav', 'recorded_mono.wav'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
result = subprocess.run(['python3', 'test_words3.py', 'recorded_mono.wav'], capture_output=True)
    #sleep()

print("result =", result)
print("type result ", type(result))
print("sub ", subprocess.CompletedProcess)

print(" stdout = ", result.stdout.decode())
print("type stdout = ", type(result.stdout.decode()))
strout = result.stdout.decode()
print("strout =", strout)

reply = ""


if  "dinner" in strout:
    print("strout has dinner")
    reply = "Swipe up and down for pizza, side to side for hamburgers"
    subprocess.call(['espeak', reply, '-ven+f2', '-k5', '-s150'], stderr=subprocess.DEVNULL)
    while gesture == 0:
        gesture = apds.gesture()
    print('Saw gesture: {0}'.format(gesture))
    if gesture == 1 or gesture == 2:
        print("Pizza it is")
        reply = "Pizza it is"
    else:
        print("Ok ill make hamburgers")
        reply = "Ok I will make hamburgers"
if "mom" in strout:
    print("Hi honey")
    reply = "Hi honey"
if "quiz" in strout:
    print("I am sure you will do better next time if you study")
    reply = "HI am sure you will do better next time if you study"
if "test" in strout:
    print("I am sure you will do better next time if you study")
    reply = "I am sure you will do better next time if you study"
if "sad" in strout:
    print("I will get you some milk and cookies")
    reply = "I will get you some milk and cookies"   
if "party" in strout:
    print("That sounds fun")
    reply = "That sounds fun" 
if "class" in strout:
    print("Make sure to get some good sleep for tomorrow")
    reply = "Make sure to get some good sleep for tomorrow"
if "goodbye" in strout:
    print("Goodbye Dear")
    reply = "Goodbye Dear"
if "stop" in strout:
    print("See you later")
    reply = "See you later" 
    
    
subprocess.call(['espeak', reply, '-ven+f2', '-k5', '-s150'], stderr=subprocess.DEVNULL)
    
    
    
# converting the shell to python gotten from:
# https://codefather.tech/blog/shell-command-python/#:~:text=There%20are%20multiple%20ways%20to%20execute%20a%20shell,to%20standard%20output%2C%20standard%20error%20and%20command%20piping.
    
# espeak implementation from:
# https://stackoverflow.com/questions/11269575/how-to-hide-output-of-subprocess/11270665#11270665 