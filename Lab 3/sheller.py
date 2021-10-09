#arecord -f cd -r 16000 -d 5 -t wav recorded.wav && sox recorded.wav recorded_mono.wav remix 1,2

# arecord -D hw:3,0 -f cd -c1 -r 48000 -d 5 -t wav recorded_mono.wav
# python3 test_words2.py recorded_mono.wav


import os
import subprocess

#arecord = subprocess.run(['arecord', '-D', 'hw:3,0', '-f', 'cd', '-c1', '-r', '48000', '-d', '5', '-t', 'wav', 'recorded_mono.wav'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


#subprocess.run(['arecord', '-D', 'hw:3,0', '-f', 'cd', '-c1', '-r', '48000', '-d', '5', '-t', 'wav', 'recorded_mono.wav'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
##subprocess.run(['python3', 'test_words2.py', 'recorded_mono.wav'])


#result = subprocess.run(['python3', 'test_words2.py', 'recorded_mono.wav'])

#print(result)

#if "dinner" in result:
    #print("found dinner")
    
    
result = subprocess.run("arecord -D hw:3,0 -f cd -c1 -r 48000 -d 5 -t wav recorded_mono.wav | python3 test_words2.py recorded_mono.wav", shell=True)
print("result =", result)

# converting the shell to python gotten from:
# https://codefather.tech/blog/shell-command-python/#:~:text=There%20are%20multiple%20ways%20to%20execute%20a%20shell,to%20standard%20output%2C%20standard%20error%20and%20command%20piping.
