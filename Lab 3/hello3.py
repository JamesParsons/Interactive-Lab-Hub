
import pyttsx3

engine = pyttsx3.init()




# RATE
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)   # slower is lower number

# VOICE
voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[11].id) #male
#engine.setProperty('voice', 'english_rp+f3') # high female
engine.setProperty('voice', 'english_rp+f4')
#engine.setProperty('voice', voices[1].id) #male australian?

#x = 0
#index = 0
#for voice in voices:
    #print(f'index-> {index} -- {voice.name}')
    #engine.setProperty('voice', voice.id)
    #engine.say('this voice number is' + str(x))
    #x = x + 1
    #index = index + 1


engine.say("Hello say lur")
engine.runAndWait()


# female voice found here https://stackoverflow.com/questions/57751564/pyttsx3-voice-gender-female
# gotten from https://pyttsx3.readthedocs.io/en/latest/engine.html#module-pyttsx3.voice