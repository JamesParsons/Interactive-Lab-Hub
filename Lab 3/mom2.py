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


apds.enable_color = True
apds.enable_gesture = True
gesture = apds.gesture()



#while gesture == 0:
    #gesture = apds.gesture()
#print('Saw gesture: {0}'.format(gesture))


def findResponse(spoken):
    
    resp = ""
    
    if "goodbye" in spoken:
        print("Goodbye honey")
        engine.say("Goodbye Honey")
        engine.runAndWait()
        exit()    
    
    if "hello" in spoken:
        print("found hello")
        #engine.say("Hello")
        #engine.runAndWait() 
        resp = resp + "Hello"

        
    if "mom" in spoken:
        print("Hi dear")
        #engine.say("Dear")
        #engine.runAndWait()        
        resp = resp + " " + "dear"
          
    if "dinner" is spoken:
        resp = "What would you like?  swipe up for pizza and down for chicken"
        engine.say(resp)
        engine.runAndWait()
        choice = gesture()
        print("Choice returned: ", choice)
        if choice == 2:
            resp = "Pizza is on the way"
        elif choice == 4:
            resp = "Chicken will be delicious"
        
    engine.say(resp)
    engine.runAndWait()    
  
    

def getSpeech():

    with speech as source:
        print("say something!…")
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        #recog = r.recognize_google(audio, language = 'en-US')
        recog = r.recognize_google(audio, language = 'en-US')
    
        print("You said: " + recog)
        
        lower = recog.lower()
        findResponse(lower)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 


def prox():
    
    stopProx = 0
    while stopProx == 0:
        if apds.proximity >= 50 and apds <= 100:
            print("You want a hug?")
            engine.say("Come get a hug")
            engine.runAndWait() 
            stopProx = 1
   
    


def gesture():
    while True:
        gesture = apds.gesture()
        print('Saw gesture: {0}'.format(gesture)) 
        if gesture == 4:
            print("ok pizza it is!")
            return 4
        elif gesture == 2:
            print("Time for some yummy chicken")
            return 2
     
        
 
while True:
    
   
    prox()   
    #getSpeech()
    #gesture()




    
    #gesture = apds.gesture()
    #print('Saw gesture: {0}'.format(gesture))  
    

# AIzaSyD4YIcs3nWlNWbFXEr1g0NiQp-hKzXmZZU
 
 

## female voice found here https://stackoverflow.com/questions/57751564/pyttsx3-voice-gender-female
## gotten from https://pyttsx3.readthedocs.io/en/latest/engine.html#module-pyttsx3.voice
## basic funstionality for the speech to text part gotten from:
## https://maker.pro/raspberry-pi/projects/speech-recognition-using-google-speech-api-and-python