import pyttsx3

engine = pyttsx3.init()

# RATE
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)   # slower is lower number

# VOICE
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english_rp+f4')

engine.say("Can i get your digits?")
engine.runAndWait()

arecord -D hw:3,0 -f cd -c1 -r 48000 -d 5 -t wav recorded_mono.wav
#python3 test_words.py recorded_mono.wav


