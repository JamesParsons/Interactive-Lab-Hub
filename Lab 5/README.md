# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms needs to be aware of.

## Prep

1.  Pull the new Github Repo.
2.  Install VNC on your laptop if you have not yet done so. This lab will actually require you to run script on your Pi through VNC so that you can see the video stream. Please refer to the [prep for Lab 2](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2021/Lab%202/prep.md), we offered the instruction at the bottom.
3.  Read about [OpenCV](https://opencv.org/about/), [MediaPipe](https://mediapipe.dev/), and [TeachableMachines](https://teachablemachine.withgoogle.com/).
4.  Read Belloti, et al.'s [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf).

### For the lab, you will need:

1. Raspberry Pi
1. Webcam 
1. Microphone (if you want to have speech or sound input for your design)

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

#### OpenCV
A more traditional method to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python. We included 4 standard OpenCV examples: contour(blob) detection, face detection with the ``Haarcascade``, flow detection (a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (e.g. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example. 

Following is a nicer way you can run and see the flow of the `openCV-examples` we have included in your Pi. Instead of `ls`, the command we will be using here is `tree`. [Tree](http://mama.indstate.edu/users/ice/tree/) is a recursive directory colored listing command that produces a depth indented listing of files. Install `tree` first and `cd` to the `openCV-examples` folder and run the command:

```shell
pi@ixe00:~ $ sudo apt install tree
...
pi@ixe00:~ $ cd openCV-examples
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```

The flow detection might seem random, but consider [this recent research](https://cseweb.ucsd.edu/~lriek/papers/taylor-icra-2021.pdf) that uses optical flow to determine busy-ness in hospital settings to facilitate robot navigation. Note the velocity parameter on page 3 and the mentions of optical flow.

Now, connect your webcam to your Pi and use **VNC to access to your Pi** and open the terminal. Use the following command lines to try each of the examples we provided:
(***it will not work if you use ssh from your laptop***)

```
pi@ixe00:~$ cd ~/openCV-examples/contours-detection
pi@ixe00:~/openCV-examples/contours-detection $ python contours.py
...
pi@ixe00:~$ cd ~/openCV-examples/face-detection
pi@ixe00:~/openCV-examples/face-detection $ python face-detection.py
...
pi@ixe00:~$ cd ~/openCV-examples/flow-detection
pi@ixe00:~/openCV-examples/flow-detection $ python optical_flow.py 0 window
...
pi@ixe00:~$ cd ~/openCV-examples/object-detection
pi@ixe00:~/openCV-examples/object-detection $ python detect.py
```

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\***

Contours - ![Contours1](https://user-images.githubusercontent.com/89811189/139149522-3eed8754-a006-4a88-a872-128833eafd22.PNG)
Design for contours - Using contour detection would be great for path navigation.  If you had a robot vaccuum and want it to only clean a rug that is covering part of a floor - but not the uncovered part, you could use contour detection to only vaccuum the rug.

Face detection - ![face-detection1](https://user-images.githubusercontent.com/89811189/139149583-ecceb11f-8086-4e52-8e0d-82c82b6dfd24.PNG)
Design for face detection - a device like a video motion sensor that only alerts the system when a face is detected, instead of being triggered by birds or squirrels or flying spaghetti.

Flow detection - ![Optical_flow_Worked](https://user-images.githubusercontent.com/89811189/139250719-a942f6ee-13b9-4c63-ac05-39abc6856bc0.PNG)
Design for flow detection - A static mounted device could be used to track the paths of people crossing a space, so that landscapers know where to put the paving stones.  Lets say you are building a campus, and you want to lay paths between buildings that people will use (instead of walking through the landscaping).  You could mount the camera on a pole and it could record the paths people organically take.  Then create your paths / landscaping accordingly.  (this used to be done by just planting grass over the entire space and waiting to see where people walked on it so much that the grass died)

Object detection - ![object-detection1](https://user-images.githubusercontent.com/89811189/139149649-db45f4bc-4ec6-4a38-baf4-d26468d0e3a3.PNG)
Design for object detection - An automated trash can.  When the can senses an object being thrown at it, it opens it's lid to catch the trash.



#### MediaPipe

A more recent open source and efficient method of extracting information from video streams comes out of Google's [MediaPipe](https://mediapipe.dev/), which offers state of the art face, face mesh, hand pose, and body pose detection.

![Alt Text](mp.gif)

To get started, create a new virtual environment with special indication this time:

```
pi@ixe00:~ $ virtualenv mpipe --system-site-packages
pi@ixe00:~ $ source mpipe/bin/activate
(mpipe) pi@ixe00:~ $ 
```

and install the following.

```
...
(mpipe) pi@ixe00:~ $ sudo apt install ffmpeg python3-opencv
(mpipe) pi@ixe00:~ $ sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr23
(mpipe) pi@ixe00:~ $ pip3 install mediapipe-rpi4 pyalsaaudio
```

Each of the installs will take a while, please be patient. After successfully installing mediapipe, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the hand pose detection script we provide:
(***it will not work if you use ssh from your laptop***)


```
(mpipe) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(mpipe) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python hand_pose.py
```

Try the two main features of this script: 1) pinching for percentage control, and 2) "[Quiet Coyote](https://www.youtube.com/watch?v=qsKlNVpY7zg)" for instant percentage setting. Notice how this example uses hardcoded positions and relates those positions with a desired set of events, in `hand_pose.py` lines 48-53. 

**\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\***

![hand_pose1](https://user-images.githubusercontent.com/89811189/139149695-6a9d769d-1cf2-4008-8a7b-4b457d4b69b6.PNG)


(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)



#### Teachable Machines
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple. However, its simplicity is very useful for experimenting with the capabilities of this technology.

![Alt Text](tm.gif)

To get started, create and activate a new virtual environment for this exercise with special indication:

```
pi@ixe00:~ $ virtualenv tmachine --system-site-packages
pi@ixe00:~ $ source tmachine/bin/activate
(tmachine) pi@ixe00:~ $ 
```

After activating the virtual environment, install the requisite TensorFlow libraries by running the following lines:
```
(tmachine) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ sudo chmod +x ./teachable_machines.sh
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ ./teachable_machines.sh
``` 

This might take a while to get fully installed. After installation, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the example script:
(***it will not work if you use ssh from your laptop***)

```
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python tm_ppe_detection.py
```


(**Optionally**: You can train your own model, too. First, visit [TeachableMachines](https://teachablemachine.withgoogle.com/train), select Image Project and Standard model. Second, use the webcam on your computer to train a model. For each class try to have over 50 samples, and consider adding a background class where you have nothing in view so the model is trained to know that this is the background. Then create classes based on what you want the model to classify. Lastly, preview and iterate, or export your model as a 'Tensorflow' model, and select 'Keras'. You will find an '.h5' file and a 'labels.txt' file. These are included in this labs 'teachable_machines' folder, to make the PPE model you used earlier. You can make your own folder or replace these to make your own classifier.)

**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***

The T-Machine! - It thinks my face is a mask.  I feel seen.  

![tmachine1](https://user-images.githubusercontent.com/89811189/139149773-f13501fc-278d-4d24-bbfc-5533f01b9c4d.PNG)




*Don't forget to run ```deactivate``` to end the Teachable Machines demo, and to reactivate with ```source tmachine/bin/activate``` when you want to use it again.*


#### Filtering, FFTs, and Time Series data. (optional)
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU data stream could create a simple activity classifier between walking, running, and standing.

Using the accelerometer, try the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up averaging** Can you average your signal in N-sample blocks? N-sample running average?

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

**\*\*\*Include links to your code here, and put the code for these in your repo--they will come in handy later.\*\*\***


### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interaction outputs and inputs.

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***

Testing how well the camera can detect object edges when mounted on a wheeled platform.  This could have many uses. A robot vaccuum could use this information to avoid obstacles, or to stay only on (or off) a floor covering.  A machine on a roof could be trained to avoid the edges.  If the system works well enough it could be used for street sweepers to get as close as possible to the curb.  It could also be used in vehicles for wall / other vehicle detection systems. The test is to see if the contour recognizer could keep up and update quickly enough if mounted on a moving object.

### Part C
### Test the interaction prototype

https://user-images.githubusercontent.com/89811189/139499926-66e22998-70ea-4022-bbb1-1f2af5657f4b.mp4

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do?  It seems to work when moving at most speeds I achieved by pushing / pulling the lego car with the camera mounted on it.
1. When does it fail? Like most things that deal with connections over a network it 'jumps', but this occurs seldomly.  The question is wether it happens because of the software, hardware, or network.
1. When it fails, why does it fail?  Speed?  Network connection?  Tough to say.
1. Based on the behavior you have seen, what other scenarios could cause problems?  Using it for edge avoidance in a car might cause it to fail because of the speed of cars.   For instance, I would not want to bet my life on it if it were used in collision avoidance systems in my car (at least not if it were running on a raspberry pi over a network).

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?  If the system were in a vaccuum it would probably not matter.  If it were used in a vehicle safety system it would matter very much.  I think the users would be aware either way if the system failed.
1. How bad would they be impacted by a miss classification?  In a car?  Let's hope we never find out.
1. How could change your interactive system to address this?  Multiple redundancies.  Airbags. Autobraking.
1. Are there optimizations you can try to do on your sense-making algorithm.  I can not figure out how to manipulate the feedback from the contour detection program to get any useful feedback despite what it already does. I do not know how to 'use' that output.

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?  You could use it for vehicle or vaccuum obstacle avoidance 
* What is a good environment for X? A clean monotone environment where the contours you want to detect are the only 'noise' in the environment.  An environment where there is too much going on visually can distract the program.  This can be seen in the difference between the first video done on a clean white table, and the second video done on a loud carpet.  The device actually did pretty well on the loud carpet, but not well enough to be useful for most applications.
* What is a bad environment for X?  A visually busy environment is bad for the device.
* When will X break?  When there is too much stimuli combined with moving the camera too quickly.
* When it breaks how will X break?  It misses some of the contours.  In the busy carpet test it caught the variations in the carpet, but missed the corner of the wall.
* What are other properties/behaviors of X?  The program does a decent job of recognizing contours but the edges are not crisp and clear.
* How does X feel?  It's still pretty cool despite the issues, feels great.

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***



https://user-images.githubusercontent.com/89811189/139502858-2e40b37b-f7f7-463a-8ad1-17dd46d7e4f6.mp4



### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**\*\*\*Include a short video demonstrating the finished result.\*\*\***
