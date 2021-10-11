import subprocess
text = 'Hello World.'
print(text)
subprocess.call(['espeak', text], stderr=subprocess.DEVNULL)