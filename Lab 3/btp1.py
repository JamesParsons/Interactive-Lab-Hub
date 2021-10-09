import subprocess

subprocess.call("ls")

#subprocess.call("arecord -D hw:3,0 -f cd -c1 -r 48000 -d 5 -t wav recorded_mono.wav")
#subprocess.call("python3 test_words2.py recorded_mono.wav")







#arecord -D hw:3,0 -f cd -c1 -r 48000 -d 5 -t wav recorded_mono.wav
#python3 test_words2.py recorded_mono.wav
