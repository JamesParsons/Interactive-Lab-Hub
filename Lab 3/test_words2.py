#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import sys
import os
import wave
import json

if not os.path.exists("model"):
    print ("Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
    exit (1)

wf = wave.open(sys.argv[1], "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit (1)

model = Model("model")
# You can also specify the possible word list
rec = KaldiRecognizer(model, wf.getframerate(),'["hello howdy mom dinner", "[unk]"]')


while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        resulter = json.loads(rec.Result())
        print("!!!!!this! ", rec.Result())
   

print("from test_words2 ", rec.FinalResult())


if resulter: 
    print("resulter = ", resulter)
    
    for item in resulter:
        #for thing in item:
        print("item = ", item)
    #print(resulter[item])
else:
    print("no resulter")
    
print("maybe = ", resulter[1])


