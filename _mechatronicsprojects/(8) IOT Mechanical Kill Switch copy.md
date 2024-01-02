---
name: IOT Mechanical Kill Switch
tools: [IOT, Blynk, Arduino, C++, SolidWorks, 3D Printing]
image: https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704208550/portfolio-site/kill-switch/lf0b0mnbkbuezgpgg7nv.jpg
description: Made a kill switch to turn my 3D printer off from my phone.
slug: kill-switch
---

# IOT Mechanical Kill Switch
<p class="post-metadata text-muted">
  January 6th, 2021
</p>
***
This IOT project was designed as a solution to a problem I had while 3D printing.

When I started prints before work I would ask my sister to turn off my printer when the print was finished because I didn’t like having it sit idle for several hours.

Instead of relying on my sister I created a device which flicks the power switch on or off and can be controlled from a smartphone anywhere in the world.

{% include elements/video.html id="bUHA4UCiuWs" %}

## Hardware Design
The hardware for this project consists of a microcontroller and a SG90 micro servo.The microcontroller is a NodeMCU, which is essentially an Arduino Nano with a Wi-Fi chip. 

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704208881/portfolio-site/kill-switch/cidaaq9tbwvbs4dpwxub.jpg "Kill switch hardware")

The on board Wi-Fi chip enables us to connect to a local wifi network and then with the help of a little bit of code, we are able to control the microcontroller from an app on our phone.

## Code
The backbone of this project is a free app called Blynk. Blynk allows you to easily create apps that interact with Wi-Fi enabled microcontrollers. 

The code for this project is hardly worth talking about. I copied and pasted the ‘Getting Started’ code from the Blynk website in order to connect my NodeMCU to the app.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704209282/portfolio-site/kill-switch/h2fdmcxtmqixjllyb0wm.png "Blynk App")

To connect a device you need to connect your microcontroller to a Wi-Fi network. Then using the authentication key, which is created when you create a new project in Blynk, you are able to connect your phone to your project. 

{% include elements/button.html link="https://github.com/loganhartford/Project-Portfolio/blob/main/Multi-Disciplinary/Kill%20Switch/Firmware/Kill_Switch.ino" text="GitHub" style="primary" size="lg" %}

## Mechanical Design
The CAD for this project is simple, but required many test prints and revisions due to the tight tolerances and a lack of an accurate way to measure desired distances. 

The model slides into the v-slot on the aluminium extrusion on my Ender3 and positions the servo to allow it to flick the switch. To make it easier for the servo to flick the switch and decrease the chance of it getting caught, an extension for the arm was designed. 

{% capture carousel_images %}
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704209178/portfolio-site/kill-switch/bccfjo7aktrxyz7inw4k.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704209589/portfolio-site/kill-switch/c3dwypg3wdy6xeg1ljmh.png
{% endcapture %}
{% include elements/carousel.html %}

This extension decreases the angle of impact between the servo arm and the switch and helps the spread the force of flicking the switch  more evenly across the movement.

{% include elements/button.html link="https://grabcad.com/library/ender3-servo-kill-switch-1" text="GrabCAD" style="primary" size="lg" %}

## Reflection
This project was definitely a success. The projects does what it is meant to flawlessly and I have had minimal issues using it. 

If the sole purpose of this project was to turn off a printer remotely there are much easier ways of doing this. For instance, you could avoid the mechanical engineering altogether by swapping out a servo for a relay which would be connected in series with the printers power.

Additionally, you can purchase ‘smart plugs’ which allow you to control appliances through an app, but for me, purchasing a product was out of the question.

While this project was pretty easy in terms of technical skills, it was a great intro to IOT projects and has given me the confidence try more advance IOT projects in the future.

