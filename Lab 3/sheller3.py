import os
import subprocess
from time import sleep
from vosk import Model, KaldiRecognizer
import sys
import os
import wave
import json
import pyttsx3

engine = pyttsx3.init()

# RATE
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)   # slower is lower number

# VOICE
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english_rp+f4')

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

if strout == "dinner":
    print("strout has dinner")
    reply = "What would you  like for dinner?"
    subprocess.call(['espeak', reply], stderr=subprocess.DEVNULL)
if strout == "mom":
    print("strout has mom")
    reply = "Hi honey"
    subprocess.call(['espeak', reply], stderr=subprocess.DEVNULL)