import speech_recognition as sr
import pyttsx3
import board
import digitalio
from adafruit_apds9960.apds9960 import APDS9960

# Speech to text stuff:
r = sr.Recognizer()
speech = sr.Microphone(device_index=2)


# Text to speech stuff:
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)   # slower is lower number
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english_rp+f4')

# proximity / gesture stuff
i2c = board.I2C()
int_pin = digitalio.DigitalInOut(board.D5)
apds = APDS9960(i2c, interrupt_pin=int_pin)

apds.enable_proximity = True
apds.proximity_interrupt_threshold = (0, 250)
apds.enable_proximity_interrupt = True
stopper = 0

apds.enable_color = True
apds.enable_gesture = True
gesture = apds.gesture()


#while gesture == 0:
    #gesture = apds.gesture()
#print('Saw gesture: {0}'.format(gesture))


def findResponse(spoken):
    
    if "goodbye" in spoken:
        print("Goodbye honey")
        engine.say("Goodbye Honey")
        engine.runAndWait()
        exit()    
    
    if "hello" in spoken:
        print("found hello")
        engine.say("Hello")
        engine.runAndWait()        
        
    if "mom" in spoken:
        print("Hi Dear")
        
    if apds.proximity <= 100 and stopper == 0:
        print("Aww let mommy hug you")
        engine.say("Do you need a hug?")
        engine.runAndWait()     
        stopper = 1
  
    

def getSpeech():

    with speech as source:
        print("say something!…")
        #audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        recog = r.recognize_google(audio, language = 'en-US')
    
        print("You said: " + recog)
        
        lower = recog.lower()
        findResponse(lower)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
while True:
    getSpeech()
    
    
 
 

## female voice found here https://stackoverflow.com/questions/57751564/pyttsx3-voice-gender-female
## gotten from https://pyttsx3.readthedocs.io/en/latest/engine.html#module-pyttsx3.voice
## basic funstionality for the speech to text part gotten from:
## https://maker.pro/raspberry-pi/projects/speech-recognition-using-google-speech-api-and-python