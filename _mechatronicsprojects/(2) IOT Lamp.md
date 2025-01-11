---
name: IOT NeoPixel Lamp
tools: [NodeMCU, Arduino, C++, SolidWorks, 3D Printing]
image: https://res.cloudinary.com/dlfqn0wvp/image/upload/v1736614045/portfolio-site/lamp/IMG_3979_1_xfollc.jpg
description: An RGB lamp that you can fully configure and control from your phone.
slug: lamp
---

# IOT NeoPixel Lamp
<p class="post-metadata text-muted">
  December 20th, 2024
</p>
***
{% capture list_items %}

{% endcapture %}
{% include elements/list.html title="Table of Contents" type="toc" %}

## Functional Demo

{% include elements/video.html id="HNwT8LUcYLc" %}

### Mode 1: Color Picker
- User can pick any RGB color from the color picker in the app.
- User can adjust brightness.

### Mode 2: Color Cycle
- Ring cycles through RGB spectrum.
- User can set the brightness and speed of the animation.

### Mode 3: Color Wheel
- Ring cycles each LED in the ring through the RBG specture out of phase to give the color wheel effect.
- User can set the brightness and speed of the animation.

### Mode 4: Candle
- NeoPixel ring alternates between different brightnesses and orangish colors at with variable intervals to simulate the flicker of a candle.
- User can set the brightness and speed of the animation.

## Motivation
A long time ago, I made a [Color Shifting Chameleon Lamp](https://lhartford.com/projects/color-shifting-chameleon) for my sister for her to use as a night light. After many years of faithful service, my 1st year engineering design had started to fall apart. As a replacement, I decided to quickly whip up this lamp to essentially do the same thing but better.

I wanted to maintain the color cycling modes of the Chameleon Lamp, hence modes 1 and 2. In addition, my sister is a graphic designer and photographer, so I thought having a controllable RGB light might be useful for photo or packaging shoots, hence mode 1. Lastly, my sister had mentioned to me that she wished that there were plug in fake candles she could use to dim the light in her room in the evening without having to worry about changing batteries, hence mode 4.

I decided to make the device controllable from a phone app firstly, to use up some hardware I had laying around, and secondly, to keep the hardware interface of the lamp as simple as possible. 

## Mechanical Design
The guiding principle of the lamp's design was simplicity. I wanted it to be visually uncomplicated, easy to print, easy to assemble and reasonably robust. In conjunction with this, I tried to incorporate the wires into the design as a feature, rather than making a more complex model which would attempt to hide them. I modelled the everything in a single part file becasue I'm lazy.

The NodeMCU micrcontroller pops into the base part and is secured with 4 M3 fasteners. The NeoPixel ring has an interferance fit with the top part of the lamp.The pins of the lamp's joints are M4 bolts, which can be tightened against a nut to lock the joints in place.

{% capture carousel_images %}
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1736616463/portfolio-site/lamp/carousel/pich_jqwslb.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1736616462/portfolio-site/lamp/carousel/lamph_aeyemf.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1736616185/portfolio-site/lamp/carousel/baseh_s5nigl.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1736616463/portfolio-site/lamp/carousel/toph_rwezcw.png
{% endcapture %}
{% include elements/carousel.html %}

{% include elements/button.html link="https://grabcad.com/library/minimalist-neopixel-lamp-1" text="GrabCAD" style="primary" size="lg" %}

## Electrical
The electrical design for this project is as simple as it gets. One microcontroller and one output device. I had a NodeMCU which I purchased in a pack from previous projects. The NodeMCU is can be programmed with the Arduino IDE and is compatible with Arduino library but includes and ESP32 chip so it can connect to Wi-Fi. I used a NeoPixel ring because I purhcased a pack of two with the purpose of using one for my capstone project.

# Software
The software is also relatively simple. Blynk was used to create the mobile app because I've used it before and I know how simple to setup it is. The UI of the app can be made using drag and drop widgets which are then assigned to datastreams that can be connected to varables in the Arduino code. 

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1736619701/portfolio-site/lamp/2560_sllrn5.png "App")

In the Ardunio app, various functions are defined which allow values to be updated from the Blynk app. In the main loop, every a funciton to update the ring is called which uses the Adafruit_NeoPixel.h library to set the state of the ring. Below is a snippet which shows the logic for how the LED is updated when in the candle mode.

```c
case CANDLE: {
      static float smoothBrightness = brightness;
      
      // Define flicker range as a fraction of current brightness
      float flickerRange = brightness * 0.2; // 20% of brightness
      
      // Ensure some minimum flicker when brightness is low
      if (flickerRange < 10) {
        flickerRange = 10;
      }
      
      // Calculate min/max target
      float minTarget = brightness - flickerRange;
      float maxTarget = brightness + flickerRange;
      
      // Clamp to valid brightness range
      if (minTarget < 0)   minTarget = 0;
      if (maxTarget > 255) maxTarget = 255;
      
      // Pick a random target within flicker range
      float target = random((int)minTarget, (int)maxTarget + 1);
      
      // Smooth transition
      smoothBrightness = smoothBrightness * 0.9 + target * 0.1;
      
      // Set candle color (adjust as desired)
      for (int i = 0; i < ring.numPixels(); i++) {
        ring.setPixelColor(i, 95, 180, 0); 
      }
      ring.setBrightness((uint8_t)smoothBrightness);
      break;
    }
```

{% include elements/button.html link="https://github.com/loganhartford/iot_lighting/blob/main/blynk/blynk.ino" text="View blynk.ino" style="primary" size="lg" %}
<br>

## Reflection
This was a fun and easy project which served as a nice break from the more intensive work I had been doing for school and capstone. I think the result turned out great and my sister really loved it. This project gets and A+ on ROI.



