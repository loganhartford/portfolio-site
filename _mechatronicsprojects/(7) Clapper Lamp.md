---
name: Clapper Lamp
tools: [Arduino, C++, SolidWorks, 3D Printing]
image: https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704164303/portfolio-site/clapper-lamp/pphuxhwyxdmoq3ivbb71.png
description: Made my reading lamp clap controlled.
slug: clapper-lamp
---

# Clapper Lamp
<p class="post-metadata text-muted">
  January 17th, 2021
</p>
***
The project is a compromise on my original idea. Originally, the plan was to turn a bedroom light into a ‘clapper’, however there were some issues with this.

In order to avoid running power up the wall and across the ceiling to power the Arduino, I was going to splice the mains power from the light and connect it to an AC to DC adapter and power it that way. 

For obvious reasons that idea was thrown out for now and instead I made a clapper lamp.

{% include elements/video.html id="R1ALxKl31OE" %}

## Hardware Design
There is very little hardware needed to this project.  In terms of electronics, there is an Arduino Nano which is wired to a high sensitivity microphone as well as a 5V relay.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704165163/portfolio-site/clapper-lamp/pfc64owvso2yigrrxjhn.jpg "Clapper hardware")

In order to have the cord for the lamp move through the electronics box I cut it and half and threaded it in. inside the box, the ‘hot’ wire from the lamp is connected to the terminals of the relay while the neutral wire is connected using a lever nut.

## Code
I wrote the code for this project several times from scratch to try and get the functionality I wanted out of it. The version of the code I ended up with is named KISS for Keep It Simple Stupid. This was because every time I tried to make the code more complicated it failed.

The KISS version of the code recognizes a spike in sound and then for 300ms afterwards it will wait for a second spike. If it gets two spikes it toggles the lamp, other wise it does nothing. This works great for a double clap but it can also be activated by yelling for example or loud laughter.

```c++
void loop() {
  // Read the mic
  soundRead=analogRead(soundPin);  
  Serial.println(soundRead);

  // Detection of the first clap
  if ((soundRead < low || soundRead > high) && (counter==0)) {
    counter=1;
    // This delay lets the first clap ring out 
    delay(75);
  }

  // Detection of silence between claps
  if (counter==1) {
    for (int i=0; i<25; i++) {
      delay(1);
      soundRead=analogRead(soundPin);
      if (soundRead < lowLow || soundRead > lowHigh) {
        counter=0;
        break;
      }
      else {
        counter=2;
      }
    }
  }

  // Detection of second clap
  if (counter == 2) {
    for (int i = 0; i<200; i++) {
      delay(1);
      soundRead=analogRead(soundPin);
      if (soundRead < low || soundRead > high) {
        counter =3;
        break;
      }
      else {
        counter = 0;
      }      
    }
  }

  // Toggle the light on or off
  if (counter==3 && lightStatus==0) {
    digitalWrite(relayPin, LOW);
    lightStatus=1;
    counter=0;
    Serial.println("ON");
    delay(500);
  }
  else if (counter==3 && lightStatus==1) {
    digitalWrite(relayPin, HIGH);
    lightStatus=0;
    counter=0;
    Serial.println("OFF");
    delay(500);
  }
}
```

To try and prevent yelling from being able to toggle the light, a section in the middle was added which verifies that the noise level does not exceed a small range for a short period of time between the claps.

While the design is certainly not fool proof, it works well for my needs. Occasionally it gets set off accidentally but for the most part it works as intended. To make a more significant improvement to the program I would likely need a microphone that reads pitch in addition to volume to more precisely identify claps.

{% include elements/button.html link="https://github.com/loganhartford/Project-Portfolio/blob/main/Multi-Disciplinary/Clapper%20Lamp/Firmware/Clapper_Lamp.ino" text="GitHub" style="primary" size="lg" %}

## Mechanical Design
The CAD for this project is nothing more than an enclosure for the electronics.

{% capture carousel_images %}
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704165340/portfolio-site/clapper-lamp/rgzhfyhrfjsln3qxqtke.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704165441/portfolio-site/clapper-lamp/j2o5o0pmcz1kqctd66rg.png
{% endcapture %}
{% include elements/carousel.html %}

Instead of trying to model in the holes for mounting the internal components I just printed it, marked the holes and then drilled them out with an appropriate drill bit.

## Reflection
I use this project everyday and it mostly works as intended, therefore I would call it a success. I do believe I am capable to making a clapper which could compare to the production version but I would need a different microphone module.

As previously mentioned, I think the only way to improve the project significantly from here without spending too much time fiddling around with it would be to swap out the mic for one that is able to read pitch and intensity.

My favorite types of projects are one that have functional or practical uses. It gives me great satisfaction when after crawling into bed after a nice read I simply have to clap my hands and the light goes off.
