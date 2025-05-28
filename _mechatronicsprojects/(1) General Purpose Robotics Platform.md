---
name: 3E8 Robotics
tools: [Jetson Orin Nano, ROS2, Solidworks, O-Drive]
image: https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748454556/portfolio-site/3e8/robot-2_ibp0gu.jpg
description: A WeedControl robot for residential lawns.
slug: 3e8
---

# 3E8 Robotics
<p class="post-metadata text-muted">
  May 20th, 2025
</p>
***
{% capture list_items %}
Architecture
CAD
Software
Arm Integration
Update
{% endcapture %}
{% include elements/list.html title="Table of Contents" type="toc" %}
My friend [Ari Wasch](https://www.linkedin.com/in/ariwasch/) asked me if I wanted to help him out with his [robotics startup](https://3e8robotics.com/). My main contributions to the project were developing the architecture of the robot and carrying out the Mechanical design and fabrication.

## Architecture
The platform was designed as a low-cost, versatile robot for basic manipulation and transport tasks, aiming to quickly enter the market and address applications targeted by emerging humanoid companies.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748455113/portfolio-site/3e8/HardwareArchitecture_0_0_1_.drawio_1_bt3udz.png "Award Photo")

We reused parts from previous projects and hackathons. The architecture includes:
* 36V scooter battery
* Jetson Orin Nano
* O-Drive BLDC motor controller
* Hoverboard BLDC motors
* Two Intel Realsense cameras
* Two Rpi LiDARs
* 12V & 24V buck converters
* [PiPER robotic arm](https://global.agilex.ai/products/piper)

These components met the minimum requirements for an autonomous mobile robot with manipulation. We chose an off-the-shelf arm to save development time.

## CAD
The frame uses 4040 aluminum extrusions, with electronics mounted via 3D printed parts.

{% capture carousel_images %}
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748455829/portfolio-site/3e8/CAD/ref_hzpnvn.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748455828/portfolio-site/3e8/CAD/full_hx1oto.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748455829/portfolio-site/3e8/CAD/midrack_v3hmvq.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748455828/portfolio-site/3e8/CAD/bottom_rack_tzcmot.png
{% endcapture %}
{% include elements/carousel.html %}

{% include elements/button.html link="https://github.com/loganhartford/cad_3e8" text="CAD Repo" style="primary" size="lg" %}

## Software
I added [tele-operation](https://x.com/i/status/1923608202819592247) using an X-Box controller.

{% include elements/button.html link="https://github.com/loganhartford/3e8_ros2" text="Software Repo" style="primary" size="lg" %}

## Arm Integration
The arm was received and integrated into the platform.

{% include elements/video.html id="dQzUpovOmT8" %}

## Update
The team is moving to SF to work at [Founders Inc.](https://f.inc/). I’ve left the project, as I’m not able to commit to a hardware startup right now. Best of luck to them.



