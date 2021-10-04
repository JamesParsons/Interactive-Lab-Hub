
import pyttsx3

engine = pyttsx3.init()




# RATE
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)   # slower is lower number

# VOICE
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english_rp+f4')

x = 0

while x == 0:
    response = input()
   
    response = int(response)
    
    print(response)
    
    if response == 1:
        engine.say("Hi honey you look tired, did you get enough sleep?")
    #if response == 3:
        #engine.say("I am sure that is not true, but if you are worried you can skip soccer tomorrow so you will have more time to study")
    #if response == 4:
        #engine.say("I am sorry, maybe try to avoid her for a little while.  No sense in stooping to her level")
    #if response == 5:
        #engine.say("What would you like for dinner?")
    #if response == 6:
        #engine.say("You always want hamburgers and pizza.  I do not have the stuff for that.  How about some nice chicken and rice with a salad?")
    #if response == 7:
        #engine.say("I am sorry to hear that, tell me all about it while i make us some coffee")
    #if response == 8:
        #engine.say("Hi honey how was school?")
    #if response == 9:
        #engine.say("How was work today?")
    #if response == 2:
        #engine.say("sit up straight")
   
    if response == 10:
        x = 1


#engine.say("Hello say lur")
engine.runAndWait()


# female voice found here https://stackoverflow.com/questions/57751564/pyttsx3-voice-gender-female
# gotten from https://pyttsx3.readthedocs.io/en/latest/engine.html#module-pyttsx3.voice