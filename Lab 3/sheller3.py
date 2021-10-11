import os
import subprocess
import time



while True:
    subprocess.run(['arecord', '-D', 'hw:3,0', '-f', 'cd', '-c1', '-r', '48000', '-d', '5', '-t', 'wav', 'recorded_mono.wav'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = subprocess.run(['python3', 'test_words2.py', 'recorded_mono.wav'])
    sleep(10)

print("result =", result)
