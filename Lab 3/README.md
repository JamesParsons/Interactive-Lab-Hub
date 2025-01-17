# Chatterboxes
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Additional Parts

As mentioned during the class, we ordered additional mini microphone for Lab 3. Also, a new part that has finally arrived is encoder! Please remember to pick them up from the TA.

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2021
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.
### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using a USB microphone, and the speaker on your webcamera. (Originally we intended to use the microphone on the web camera, but it does not seem to work on Linux.) In the home directory of your Pi, there is a folder called `text2speech` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)
mine is saved in Lab 3 as 
'hello3.py'
also 
morning.sh

Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. Then try `./vosk_demo_mic.sh`

One thing you might need to pay attention to is the audio input setting of Pi. Since you are plugging the USB cable of your webcam to your Pi at the same time to act as speaker, the default input might be set to the webcam microphone, which will not be working for recording.

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

miccer.sh

Bonus Activity:

If you are really excited about Speech to Text, you can try out [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) and [voice2json](http://voice2json.org/install.html)
There is an included [dspeech](./dspeech) demo  on the Pi. If you're interested in trying it out, we suggest you create a seperarate virutal environment for it . Create a new Python virtual environment by typing the following commands.

```
pi@ixe00:~ $ virtualenv dspeechexercise
pi@ixe00:~ $ source dspeechexercise/bin/activate
(dspeechexercise) pi@ixe00:~ $ 
```

### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

\*\***Post your storyboard and diagram here.**\*\*

![IDDLab3Storyboard1Rotated](https://user-images.githubusercontent.com/89811189/135354422-fa3a80c6-b0cc-46cb-8a65-b896510ffcec.jpeg)


Write out what you imagine the dialogue to be. Use cards, post-its, or whatever method helps you develop alternatives or group responses. 

\*\***Please describe and document your process.**\*\*

The process was just me trying to figure out things that a mother would say in response to someone speaking to her.

[IDD Lab 3 Part 1 Dialogue.docx](https://github.com/JamesParsons/Interactive-Lab-Hub/files/7278529/IDD.Lab.3.Part.1.Dialogue.docx)


### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*

It was much slower to get the device to respond than I had anticipated.  This was undoubtedly caused by user error.  


https://user-images.githubusercontent.com/89811189/135876861-ae3b46cf-cf75-48e6-bfed-1cca7b8456d9.mp4


### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*
I got the web page to display hello world but could not figure out what to do with it / how to work it from there.

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...
   The timing could be better, and to have the machine respond automatically.
2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?  
   Gestures, proximity recognition
3. Make a new storyboard, diagram and/or script based on these reflections.

![IDDLab3 2Storyboard](https://user-images.githubusercontent.com/89811189/136940041-f5a06527-5b25-4120-b153-4c910aa3ebe8.jpeg)

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*
   The system works primarily by voice controls.  The user speaks to the device.  The device translates that offline using the Kaldi recognizer class.  Then it parses the response looking for keywords.  The device responds appropriately given which keywords it has found.  The device also recognizes gestures.  The real struggle with this assignment was getting the mic input and voice responses to work as intended.  The limit on using google speech to text of only 50 inquiries a day really hurt.  Eventually I ended up using the python subprocess.run() commands to run command line instructions. This came with it's own set of complications however.  Despite everything being localized there was still significant lag between input and response.  
   
   The file to use is sheller4.py

*Include videos or screencaptures of both the system and the controller.*

![sheller4](https://user-images.githubusercontent.com/89811189/136970276-cc94ab72-e888-4d21-be9a-b53a7f298018.PNG)
![momdevice1](https://user-images.githubusercontent.com/89811189/136970556-37871f1c-9b92-4f9e-9c36-282c6fef1e31.JPG)
![momdevice2](https://user-images.githubusercontent.com/89811189/136970565-6cbd3f13-c0f2-4249-990f-d2cb9440d7c1.JPG)



## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?
   The program had to be re-run after every interaction.  That is ok, the user's did not seem to notice, they only noticed that it was slow.  It took a few tries with all three users for them to get the timing down.  The device does not start recording sound until a second after the program starts, and then the user only has a limited time to state their command / question.  With practice with each participant we finally got it down.  As a result of this they knew it was being wizarded, because I had to point at them when I wanted them to start speaking.  Ideally this would have been seamless, and the device would be constantly monitoring for a command.  
      The system also exited after every interaction despite the meat of the program being in a while loop.  Still investigating why that is heppening.

### What worked well about the controller and what didn't?

   The command / response / gestures all worked well.  What did not work so well was the timing of using the device.

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

   A way to get the system to be constantly listening would be good.  Also, having the system not exit after a single command / response would be necessary for it to be a truly functional device.  Being able to recognize gestures from further away would also be useful.


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

   Feedback to responses could be sent to a database.  For instance, whether the user responded affirmative or negative, what choices they made on subjective questions posed by the device, and the frequency of each type of question.  Then the device could be tweaked to maximize the most common types of interactions.
   
 David Opatrny was the one that clued me into the fact that I was dealing with a json object.  Also Magdalena Horowitz helped to try and diagnose what was going on with my github account.

