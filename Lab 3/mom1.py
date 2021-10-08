import speech_recognition as sr
import pyttsx3

# Speech to text stuff:
r = sr.Recognizer()
speech = sr.Microphone(device_index=2)


# Text to speech stuff:
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)   # slower is lower number
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english_rp+f4')


def findResponse(spoken):
    
    if "goodbye" in spoken:
        print("Goodbye honey")
        exit()    
    
    if "hello" in spoken:
        print("found hello")
        engine.say("Hello")
        engine.runAndWait()        
        
    if "mom" in spoken:
        print("Hi Dear")
    if "Mom" in spoken:
        print("Hi Dear")   
   

def getSpeech():

    with speech as source:
        print("say something!…")
        #audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        recog = r.recognize_google(audio, language = 'en-US')
    
        print("You said: " + recog)
        findResponse(recog)
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