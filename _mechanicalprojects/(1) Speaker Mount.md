---
name: Speaker Mount
tools: [SolidWorks, 3D Printing]
image: https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704212086/portfolio-site/3d-modelling/speaker-mount/xzl3y0bm1vcwanz8bwoz.jpg
description: 3D printed mounts for my desktop speakers
slug: speaker-mount
---

# Speaker Mount
<p class="post-metadata text-muted">
  August 8th, 2022
</p>
***
This is one of my favorite projects I’ve made. 

Adding this to my desktop really made my whole setup look so much nicer and put my beautiful speakers out in the open instead of having to hide them behind my monitors on my too-small desk.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704212086/portfolio-site/3d-modelling/speaker-mount/xzl3y0bm1vcwanz8bwoz.jpg "Speaker mount setup")

One of the requirements of this project was that it had to work without any modifications or damage to the desk since the desk is owned by my landlord.

The device mounts to the desk at two points. The main body of the assembly has a bolt vertically through the top to prevent lateral motion, which fits into a random hole in the top of the metal of the desk.

{% capture carousel_images %}
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704213247/portfolio-site/3d-modelling/speaker-mount/ffegdp0djlbxw51cmwqn.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704213248/portfolio-site/3d-modelling/speaker-mount/gdefy2tkufmpolfdfbpg.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704213248/portfolio-site/3d-modelling/speaker-mount/p7jqgqwetjbsk805nhqk.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704213250/portfolio-site/3d-modelling/speaker-mount/q0ekp5pbpucekzkzbgpp.png
{% endcapture %}
{% include elements/carousel.html %}

Underneath the desk, the slot in the secondary body of the assembly mates with one of the screws that holds the desk together. Once fastened to the main body, this allows the model to essentially be clamped to the desk to give a nice rigid fit.

The cutouts for the nuts in the larger model are actually smaller than the nuts. I used a soldering iron to heat the nuts and then pressed them into the plastic, embedding it into the model.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704213296/portfolio-site/3d-modelling/speaker-mount/imfocgrsgn6vdyyz3wsy.gif "Speaker mount setup")

The underside of this model is pretty cool and I made it using pretty simple features. I started by adding 3 ribs to the model's underside, in positions that I thought reasonable to support the speaker's weight.  This looked pretty dumb though and presented some challenges for 3D printing.

{% capture carousel_images %}
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704212787/portfolio-site/3d-modelling/speaker-mount/gxlw9qmllniwecuq8kfz.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704212901/portfolio-site/3d-modelling/speaker-mount/tcxfsu8hpfdf4lhrviaj.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704212785/portfolio-site/3d-modelling/speaker-mount/znbbh4a1puin1vhgsuuv.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1704212810/portfolio-site/3d-modelling/speaker-mount/govhvqbotiozcr19l2do.png
{% endcapture %}
{% include elements/carousel_2.html %}

To remove the overhangs and make them look cool, I added many iterations of filets and chamfers to the space between the ribs. I think this looks way cooler and it was able to print without supports which is also groovy.

A small hook was also added to the back of the model which allows me to route the speaker cable down behind the model, hiding them from view.

There is also only a right side version of this model as my desk is symmetrical and to print the left side I simply mirrored it in my slicing software before generating the g-code for printing.

{% include elements/button.html link="https://grabcad.com/library/speaker-mount-2" text="GrabCAD" style="primary" size="lg" %}