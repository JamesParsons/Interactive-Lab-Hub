import speech_recognition as sr


r = sr.Recognizer()
speech = sr.Microphone(device_index=2)
stopper = 0


def findResponse(spoken):
    if "hello" in spoken:
        print("found hello")
        
    if "mom" in spoken:
        print("Hi Dear")
    if "Mom" in spoken:
        print("Hi Dear")   
    if "goodbye" in spoken:
        stopper = 1

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
    
while stoper == 0:
    getSpeech()
    
    
    