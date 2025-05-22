---
name: WeedWarden
tools: [ROS2, YOLOv11, OpenCV, RPi5, STM32]
image: https://res.cloudinary.com/dlfqn0wvp/image/upload/v1747318648/portfolio-site/WeedWarden/robot_2_vtzsey.jpg
description: A WeedControl robot for residential lawns.
slug: weedwarden
---

# WeedWarden - Full Write up TBD
<p class="post-metadata text-muted">
  April 24th, 2025
</p>
***
{% capture list_items %}

{% endcapture %}
{% include elements/list.html title="Table of Contents" type="toc" %}

## 4th Year Capstone Project

This project was completed as part of a the 4th year capstone project at the University of Waterloo. Our team received a grade of 97% for the project course and won the Best Prototype Award (2nd highest distinction) at our design syposium (I'm absent from the photo below as I had to fly to California for a job interview).

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1747940403/portfolio-site/WeedWarden/21-IMG_6842_1_qkzr9c.jpg "Award Photo")

The goal of the project was to develop a Roomba for your lawn. The robot is intended to automatically go out and blend up weeds each night. This removes any visial sign of the weeds, eventually leading to their death, without any manual labour or pesticide usage.

As part of our final design review, we captured videos to showcase the robot's performance. The video below shows the robot doing a full clear of our test setup. In this video, the robot is programed to follow a path which covers the turn, identify and remove dandelions. The removal is at limited speed and depth for obvious reason's.

{% include elements/video.html id="LF1d6aeK7RU" %}

In the video above, the robot is locating the weeds along it's path autonomously. The weeds are placed arbitrarily and the robot uses its computer vision (CV) and decision making to remove the weeds. This is shown even better in the following video, which is meant to showcase the reapeatability and autonomy of the robot.

{% include elements/video.html id="RoHv5wQGr44" %}

In this video, the robot is shown completing two time-triggered consecutive clears of the turf, with a reset of the feild in between. This is to highlight the fact that the robot can start it's work autonomously, and that the locations of the weeds are not hardcoded in any way.

Since these video's did not in anyway prove the robot could actually "remove" the weeds, we took the robot outside to destroy some garden store plants (dandelions wer not in season). 

***add spinner bit video***

## The Project
- Ideation
- Brekdown between sub systems
- Functional goals
- Original design decisions

### The Team
The project could be completed in groups up to 5, however, we had a core group of 4 that had built robots together [befor](https://lhartford.com/projects/scara) so we decided to stick with what worked. Below is a photo of the team at our design symposium.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1747940277/portfolio-site/WeedWarden/171-IMG_6404_1_fw8x1w.jpg "Team Photo at Symposium")


On the far left is [Ethan Dau](https://www.linkedin.com/in/ethan-dau-951a1b1b4/). Ethan was the electical lead on this project, helping with the overall architecture as well as desiging, fabricating and tesitng the electrical system. Ethan was also responsible for developing the firmware related to the cartesian system of the robot. Ethan also helped out with some of the mechanical design when needed. In addition to his technical work, Ethan was also the project manager of the team, scheduling meetings and recording minutes, communicating with the teaching team, maitining the timeline and budget and creating the bulk of the content for the course deliverables.

To the right of Ethan is myself. I was the project technical lead. I was resposible for the overall architecture, functional requirements and generally guiding the technical development of the robot to a particular goal. Additionally, I was the software lead, writing all of the higher level logic of the robot. I also helped out with the firmware, primarily manaaging the communicaiton between devices and adding features for the locomotion system. As the software lead, I also ended up doing the majority of the testing and some mechancial design to rectify issues that I found.

On the right of myself is [Eric Gharghouri](https://www.linkedin.com/in/eric-gharghouri-855a281b5/). Eric's primary contribution was the design, favrication and testing of the locomotion system of the robot.

To the right of Eric is [Varrun Vijayanathan](https://www.linkedin.com/in/varrunv/). Varrun was the mechanical lead, responsible for the overall mechanical design of the robot. Varrun's primary contribution was the design, fabrication and testing of of the cartesian system as well as integrating the cartesian and locomotion systems.

### Project Managment
- Timeline
- Budget

## From 0 to Autonomy

## Development Outline
- Introduce the product
- Brining up the Pi
- Collecting Data and Validating the CV approach
- Building the cartesian system - problems and learnings
- Re-design of the cartesian system - why?
- Developing the locomotion system - Control
- Re-branding/shifting focus - Why? Feedback, decisions
  - Weed control vs weed removal
- Re-design of the locomotion system
  - Castor wheel
  - Silicone wheels
- Developing the autononmy
  - Sensor fusion
  - Path planning
  - Decision making
- Final hardware architecture - initial vs final, changes and reasons
- Final software architecture - intiial vs final, changes and reasons
- Symposium - snappy pictures, strengths and weaknesses, how it all went
- What would it take to make this a real product?
- Reflection - Lesson's learned
  - What did we do right?
  - What mistakes did we make?
    - Simpler locomotion system - odrive with hoverboard motors
  - What would I do differently?

