

espeak -ven+f2 -k5 -s150 --stdout "May I have your phone number?" | aplay

arecord -D hw:3,0 -f cd -c1 -r 48000 -d 5 -t wav recorded_mono.wav