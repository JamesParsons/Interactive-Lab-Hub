#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import sys
import os
import wave
import json
import pyttsx3

engine = pyttsx3.init()

if not os.path.exists("model"):
    print ("Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
    exit (1)

wf = wave.open(sys.argv[1], "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit (1)

model = Model("model")
# You can also specify the possible word list
rec = KaldiRecognizer(model, wf.getframerate(),'["hello howdy mom tonight dinner sad quiz test sad dinner", "[unk]"]')

# RATE
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)   # slower is lower number

# VOICE
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english_rp+f4')


while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        resulter = json.loads(rec.Result())
        #print("!!!!!this! ", rec.Result())
   

print("from test_words2 ", rec.FinalResult())

engine.say("Howdy partner")
engine.runAndWait()  

resp = ""

try:
    if resulter: 
        print("resulter = ", resulter)
        
        for item in resulter:
            print("resulter[item]", resulter[item])
        if "dinner" in resulter[item]:
            print("Found Dinner!!!!!")
            resp = "What would you like for dinner?"            
        if "mom" in resulter[item]:
            print("!!!!!!!!!!!!!mom!!!!!!!")
            resp = "Hi honey" + resp
        engine.say(resp)
        engine.runAndWait()         
    else:
        print("no resulter")
except:
    print("no resulter")
#print("maybe = ", resulter[1])