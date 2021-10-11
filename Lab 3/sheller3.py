import os
import subprocess
from time import sleep
from vosk import Model, KaldiRecognizer
import sys
import os
import wave
import json


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
    reply = "What would you  like for dinner?"
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