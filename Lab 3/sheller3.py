import os
import subprocess
from time import sleep



#while True:
subprocess.run(['arecord', '-D', 'hw:3,0', '-f', 'cd', '-c1', '-r', '48000', '-d', '5', '-t', 'wav', 'recorded_mono.wav'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
result = subprocess.run(['python3', 'test_words3.py', 'recorded_mono.wav'], capture_output=True, text=True)
    #sleep()

print("result =", result)
print("type result ", type(result))
print("sub ", subprocess.CompletedProcess)

result.stdout()
