---
name: Smart Greenhouse
tools: [IOT, Blynk, Arduino, C++, SolidWorks]
image: https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704148382/portfolio-site/smart-greenhouse/isqt0aitcngbdh7j5u1q.jpg
description: An IOT greenhouse designed to maintain a stable temperature and humidity.
category: "Full Scope"
slug: smart-greenhouse
---

# Smart Greenhouse
<p class="post-metadata text-muted">
  May 5th, 2021
</p>
***
The inspiration for this project comes from my interest in bonsai. I have a Ficus Retusa bonsai and I want it to sprout aerial roots this summer. In order for this to happen, it needs to be hot an humid.

I created this greenhouse as a way to both monitor and control the temperature and humidity inside the greenhouse.

In the future I will likely add a pump and mist system the will water the bonsai in the morning and mist in the afternoon.

{% include elements/video.html id="HQLkqG_uGd4" %}

## Hardware Design
The microcontroller used in the project is a NodeMCU which is essentially an Arduino Nano with wifi capabilities. 

As for components, the temperature and humidity inside the greenhouse is monitored using DHT11 sensor. The soil moisture is monitored using a EK1940 capacitive soil moisture sensor. The hatch at the top of the greenhouse is opened using two SG90 micro servos.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704149062/portfolio-site/smart-greenhouse/fn1pgvrz9s42z7aj3wgj.jpg "Greenhouse electronics")

All these components are soldered to the NodeMCU which is housed  inside a “Waterproof Electrical Box” I bought from amazon. I would have 3D printed this but  FDM prints are not watertight by default.

## Mechanical Design
The mechanical engineering for this project was quite straight forward. I sketched out and dimensioned what I wanted the greenhouse to look like and then I started building the frame out of wood. I used 3D printed couplers to attach pieces of wood together in spots where I would otherwise be splitting the wood or hitting a previously laid screw.

{% capture carousel_images %}
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704148604/portfolio-site/smart-greenhouse/fhpvlal35azl0ogspiay.jpg
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704148604/portfolio-site/smart-greenhouse/ui0ppgfs5d0zich2y40s.jpg
{% endcapture %}
{% include elements/carousel.html %}

Once the frame of the greenhouse was built I modeled up the components for the center axis hatch. This included modeling a mount for the servo as well as a piece that connects the wood door to the servo.

{% include elements/button.html link="https://grabcad.com/library/smart-greenhouse-1" text="GrabCAD" style="primary" size="lg" %}

## Code
This project makes use of an app called Blynk which makes it easy to integrate your phone into arduino projects.

```c++
  // Opens hatch if its too hot
  if (temp > openTemp) {
    while (s1Pos >= 0) {
    delay(30);
    s1Pos--;
    s2Pos++;
    Servo1.write(s1Pos);
    Servo2.write(s2Pos);
    }
  }
  // Closes it once it cools down
  else if (temp < closeTemp) {
    while (s1Pos <= 82) {
    delay(30);
    s1Pos++;
    s2Pos--;
    Servo1.write(s1Pos);
    Servo2.write(s2Pos);
    }
  }
```

The code for this project can essentially be broken down into two sections, controlling the servos and sending data to Blynk. Every iteration of the program, the DHT11 is read and if that temp is higher than openTemp, the hatch door opens to cool the greenhouse. Once the temperature falls back below closeTemp, the hatch will be closed again, keeping the greenhouse within a desired temperature range. 

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704149830/portfolio-site/smart-greenhouse/ejylno3sklfeelzxdsuz.png "Screenshot of blynk app")

Each cycle the program sends temperature, humidity and soil moisture data to be used in the Blynk app. We can add logic within the Blynk app. The squiggle and phone icon next to the soil moisture panel makes it so that the app sends me a push notification if my soil dries out below a certain threshold.

{% include elements/button.html link="https://github.com/loganhartford/Project-Portfolio/blob/main/Multi-Disciplinary/Smart%20Greenhouse/Firmware/Smart%20Greenhouse.ino" text="GitHub" style="primary" size="lg" %}

## Reflection
I really like this project because it has a practical use and will hopefully help my bonsai grow some aerial roots this summer.

This project was more difficult than anticipated due to the constant concern of exposing the electronics to water. The microcontroller is in a waterproof case but that isn’t an option for the servos. Special consideration needed to be taken to protect everything and I’m still not sure of the longevity of it.

Some other issues with the current design that I realized through testing is the temperature reading and regulation. I don’t think the temperature sensor is giving accurate air temperature data right now. It is under direct sunlight so I think the plastic of the sensor is heating up rather than the air which is giving use abnormally high readings. To counteract this I will build some shade for the sensor or maybe even wrap it in tin-foil. I am also unsure if opening a hatch is going to be sufficient to reduce the temperature on a really hot day. I will have to do some testing before leaving the bonsai in there un-attended. I may need to add some fans or some other powered cooling system.

In the next version of this project, I will address the concerns listed above as well as add some additional features. A bonsai in bonsai soil needs to be watered daily so I will add an automatic watering system to the greenhouse. Additionally, moistening the bonsai and the air with mist in the afternoon helps promote the growth of aerial roots so I would like to add a mist system as well.

Overall this project was a success but it made me realize that this is only part one of a two part project. I’m excited to keep working on this and see the results of the finished product.
