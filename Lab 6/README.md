# Little Interactions Everywhere

## Prep

1. Pull the new changes from the class interactive-lab-hub. (You should be familiar with this already!)
2. Install [MQTT Explorer](http://mqtt-explorer.com/) on your laptop.
3. Readings before class:
   * [MQTT](#MQTT)
   * [The Presence Table](https://dl.acm.org/doi/10.1145/1935701.1935800) and [video](https://vimeo.com/15932020)


## Overview

The point of this lab is to introduce you to distributed interaction. We have included some Natural Language Processing (NLP) and Generation (NLG) but those are not really the emphasis. Feel free to dig into the examples and play around the code which you can integrate into your projects if wanted. However, we want to emphasize that the grading will focus on your ability to develop interesting uses for messaging across distributed devices. Here are the four sections of the lab activity:

A) [MQTT](#part-a)

B) [Send and Receive on your Pi](#part-b)

C) [Streaming a Sensor](#part-c)

D) [The One True ColorNet](#part-d)

E) [Make It Your Own](#part-)

## Part 1.

### Part A
### MQTT

MQTT is a lightweight messaging portal invented in 1999 for low bandwidth networks. It was later adopted as a defacto standard for a variety of [Internet of Things (IoT)](https://en.wikipedia.org/wiki/Internet_of_things) devices. 

#### The Bits

* **Broker** - The central server node that receives all messages and sends them out to the interested clients. Our broker is hosted on the far lab server (Thanks David!) at `farlab.infosci.cornell.edu/8883`. Imagine that the Broker is the messaging center!
* **Client** - A device that subscribes or publishes information to/on the network.
* **Topic** - The location data gets published to. These are *hierarchical with subtopics*. For example, If you were making a network of IoT smart bulbs this might look like `home/livingroom/sidelamp/light_status` and `home/livingroom/sidelamp/voltage`. With this setup, the info/updates of the sidelamp's `light_status` and `voltage` will be store in the subtopics. Because we use this broker for a variety of projects you have access to read, write and create subtopics of `IDD`. This means `IDD/ilan/is/a/goof` is a valid topic you can send data messages to.
*  **Subscribe** - This is a way of telling the client to pay attention to messages the broker sends out on the topic. You can subscribe to a specific topic or subtopics. You can also unsubscribe. Following the previouse example of home IoT smart bulbs, subscribing to `home/livingroom/sidelamp/#` would give you message updates to both the light_status and the voltage.
* **Publish** - This is a way of sending messages to a topic. Again, with the previouse example, you can set up your IoT smart bulbs to publish info/updates to the topic or subtopic. Also, note that you can publish to topics you do not subscribe to. 


**Important note:** With the broker we set up for the class, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`. Also, setting up a broker is not much work, but for the purposes of this class, you should all use the broker we have set up for you!


#### Useful Tooling

Debugging and visualizing what's happening on your MQTT broker can be helpful. We like [MQTT Explorer](http://mqtt-explorer.com/). You can connect by putting in the settings from the image below.


![input settings](imgs/mqtt_explorer.png?raw=true)


Once connected, you should be able to see all the messages under the IDD topic. , go to the **Publish** tab and try publish something! From the interface you can send and plot messages as well. Remember, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`.

![publish settings](imgs/mqtt_explorer_2.png?raw=true)


### Part B
### Send and Receive on your Pi

[sender.py](./sender.py) and and [reader.py](./reader.py) show you the basics of using the mqtt in python. Let's spend a few minutes running these and seeing how messages are transferred and shown up. Before working on your Pi, keep the connection of `farlab.infosci.cornell.edu/8883` with MQTT Explorer running on your laptop.

**Running Examples on Pi**

* Install the packages from `requirements.txt` under a virtual environment, we will continue to use the `circuitpython` environment we setup earlier this semester:
  ```
  pi@ixe00:~ $ source circuitpython/bin/activate
  (circuitpython) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 6
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ pip install -r requirements.txt
  ```
* Run `sender.py`, fill in a topic name (should start with `IDD/`), then start sending messages. You should be able to see them on MQTT Explorer.
  ```
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python sender.py
  pi@ReiIDDPi:~/Interactive-Lab-Hub/Lab 6 $ python sender.py
  >> topic: IDD/ReiTesting
  now writing to topic IDD/ReiTesting
  type new-topic to swich topics
  >> message: testtesttest
  ...
  ```
* Run `reader.py`, and you should see any messages being published to `IDD/` subtopics.
  ```
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python reader.py
  ...
  ```

**\*\*\*Consider how you might use this messaging system on interactive devices, and draw/write down 5 ideas here.\*\*\***

1) Trivia game:  One Pi could host the questions and the other pi's could be used for people answering the question.
2) Simon gestures:  Pi's have gesture sensors connected.  The first person makes a gesture.  The second person has to respond with the same gesture.  If they get it right, they make another gesture.  Whenever someone can not mimic the previous gesture the other pi gets a point.
3) Novel generator:  The main pi publishes the first line of a novel, like "It was a dark and stormy night. (2)"  Then whoever is pi #2 writes the next line, and names the successive author when they are done.  Around and around it goes until something fun has been written.
4) Car army:  Multiple satellite pi's could be communicating with the broker.  The satellite pi's send their distance sensor values to the brokerPi, which tells them to move right, left, forward or backward to make cool shapes.  You could make your car army form a star.  Or a letter (like "B").
5) Best friend waker-upper.  If both pi's are connected, then pi A can send a message that actuates a servo on pi B that dumps a glass of water on their friend who is late to class.
6) Joy stick horse.  One person goes first and enters a 'letter' using the joystick, like the script letter 'a'.  Then the remaining players have a chance to copy it.  If they succesfully copy the letter within a reasonable percentage, the original player gets a letter.  Then if the players can not match the original letter drawn, they pick up a letter.  The player who has not earned all the letters in horse (the last remaining player) is the winner.

### Part C
### Streaming a Sensor

We have included an updated example from [lab 4](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Fall2021/Lab%204) that streams the [capacitor sensor](https://learn.adafruit.com/adafruit-mpr121-gator) inputs over MQTT. We will also be running this example under `circuitpython` virtual environment.

Plug in the capacitive sensor board with the Qwiic connector. Use the alligator clips to connect a Twizzler (or any other things you used back in Lab 4) and run the example script:

<p float="left">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
<img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150"/>
<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" height="150">
</p>

 ```
 (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python distributed_twizzlers_sender.py
 ...
 ```

**\*\*\*Include a picture of your setup here: what did you see on MQTT Explorer?\*\*\***
When i touched the red or the green grape in MQTT it read 'Twizzler 6 / Twizzler 11 touched!'

![IMG_2766](https://user-images.githubusercontent.com/89811189/141133807-782eebb5-37c7-4485-9518-e8382c69cabb.JPG)

![IMG_2767](https://user-images.githubusercontent.com/89811189/141133890-aaca6427-ab09-4517-a352-5eec517b0341.JPG)

i ate the grapes afterward. 
![image](https://user-images.githubusercontent.com/89811189/141134305-d409ad22-156f-4659-83de-482814cd27dc.png)



**\*\*\*Pick another part in your kit and try to implement the data streaming with it.\*\*\***

I used the joystick. This holds the potential for a lot of fun.
![IMG_2768](https://user-images.githubusercontent.com/89811189/141137688-a6245a0d-cc92-40ff-b073-baab6ae181b2.JPG)

![image](https://user-images.githubusercontent.com/89811189/141137529-05d1f4e1-1f83-420b-939c-5420e7875155.png)


### Part D
### The One True ColorNet

It is with great fortitude and resilience that we shall worship at the altar of the *OneColor*. Through unity of the collective RGB, we too can find unity in our heart, minds and souls. With the help of machines, we can overthrow the bourgeoisie, get on the same wavelength (this was also a color pun) and establish [Fully Automated Luxury Communism](https://en.wikipedia.org/wiki/Fully_Automated_Luxury_Communism).

The first step on the path to *collective* enlightenment, plug the [APDS-9960 Proximity, Light, RGB, and Gesture Sensor](https://www.adafruit.com/product/3595) into the [MiniPiTFT Display](https://www.adafruit.com/product/4393). You are almost there!

<p float="left">
  <img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
  <img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
  <img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" height="150">
</p>


The second step to achieving our great enlightenment is to run `color.py`. We have talked about this sensor back in Lab 2 and Lab 4, this script is similar to what you have done before! Remember to ativate the `circuitpython` virtual environment you have been using during this semester before running the script:

 ```
 (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python color.py
 ...
 ```

By running the script, wou will find the two squares on the display. Half is showing an approximation of the output from the color sensor. The other half is up to the collective. Press the top button to share your color with the class. Your color is now our color, our color is now your color. We are one.

(A message from the previous TA, Ilan: I was not super careful with handling the loop so you may need to press more than once if the timing isn't quite right. Also, I haven't load-tested it so things might just immediately break when everyone pushes the button at once.)

You may ask "but what if I missed class?" Am I not admitted into the collective enlightenment of the *OneColor*?

Of course not! You can go to [https://one-true-colornet.glitch.me/](https://one-true-colornet.glitch.me/) and become one with the ColorNet on the inter-webs. Glitch is a great tool for prototyping sites, interfaces and web-apps that's worth taking some time to get familiar with if you have a chance. Its not super pertinent for the class but good to know either way. 

**\*\*\*Can you set up the script that can read the color anyone else publish and display it on your screen?\*\*\***
I am one with the collective. Hail color!
![IMG_2769](https://user-images.githubusercontent.com/89811189/141140253-e6faa564-d38b-44e4-be35-717a386a0dbc.JPG)


### Part E
### Make it your own

Find at least one class (more are okay) partner, and design a distributed application together based on the exercise we asked you to do in this lab.

James Parsons - jsp285       Victoria Zhang - cz237     Mahir Kothary - mk942

**\*\*\*1. Explain your design\*\*\*** For example, if you made a remote controlled banana piano, explain why anyone would want such a thing.
(ok who WOULDN'T want such a thing??  I think we could all use a banano.  A pianana)

We made a game of HORSE using the distance sensors over a distributed system.  This was especially cool as two of us live off campus so it was a true distributed system.

**\*\*\*2. Diagram the architecture of the system.\*\*\*** 
Each individual pi has a distance sensor hooked up.  Each pi can send distance measurements.  Each pi receives, sees, and prints every distance that a player enters.  The main scoring program was run on James's computer.  The scoring program records and changes every player's score accordingly, which also gets published and can be seen by each individual pi.  Every node on the system receives and publishes alerts to the entire system.

![horse](https://user-images.githubusercontent.com/89811189/141792630-0761ff09-089a-4b90-ba24-c32b45ebb54f.jpeg)


**\*\*\*3. Build a working prototype of the system.\*\*\*** 
With proper signage people might understand the system.  With just the distance sensor connected to a raspberry pi out in the wild i imagine people would think 'Why is there a little computery doohickey out in the wild?  Why am I in the wild?  How did I get here?  Maybe if i jump around in front of this doohickey somebody will come get me'.  Since the pi is connected to a distributed system, someone might see their distance measurement and come rescue them.  We are saving lives.

**\*\*\*4. Document the working prototype in use.\*\*\*** It may be helpful to record a Zoom session where you should the input in one location clearly causing response in another location.

My set up (then I accidentally moved my pi so it is out of frame, but its there)

https://user-images.githubusercontent.com/89811189/141866216-116e65b4-50f8-4119-83b5-4a8237ac7c85.mp4

All of us playing!

https://user-images.githubusercontent.com/89811189/141866225-71be7c7f-077b-4729-9aab-6674fa004c25.mp4



https://user-images.githubusercontent.com/89811189/141880106-9021cdf5-716e-425e-b486-eddf87e70ebf.mp4

A 3 minute long video is available upon request (I dont know how to youtube it) or is also probably available on Mahir or Victoria's lab pages.

<!--**\*\*\*5. BONUS (Wendy didn't approve this so you should probably ignore it)\*\*\*** get the whole class to run your code and make your distributed system BIGGER.-->

