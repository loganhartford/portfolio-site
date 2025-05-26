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

This project was completed as part of a the 4th year capstone project at the University of Waterloo. 

Our team received a grade of 97% for the project course and won the Best Prototype Award (2nd highest distinction) at our design symposium (I'm absent from the photo below as I had to fly to California for a job interview).

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1747940403/portfolio-site/WeedWarden/21-IMG_6842_1_qkzr9c.jpg "Award Photo")

The goal of the project was to develop a Roomba for your lawn. The robot is intended to automatically go out and blend up weeds each night. This removes any visual sign of the weeds, eventually leading to their death, without any manual labour or pesticide usage.

As part of our final design review, we captured videos to showcase the robot's performance. The video below shows the robot doing a full clear of our test setup. In this video, the robot is following a pre-defined path and then autonomously identifying and nullifying the fake weeds it detects. During the removal, the drill speed and depth are limited for obvious reasons.

{% include elements/video.html id="LF1d6aeK7RU" %}

In the video above, the robot is locating the weeds along it's path autonomously. The weeds are placed arbitrarily and the robot uses its computer vision (CV) and decision making to remove the weeds. This is shown even better in the following video, which is meant to showcase the repeatability and autonomy of the robot.

{% include elements/video.html id="RoHv5wQGr44" %}

In this video, the robot is shown completing two, time-triggered consecutive clears of the turf, with a reset of the field in between. This is to highlight the fact that the robot can start it's work autonomously, and that the locations of the weeds are not hardcoded in any way.

Since these video's did not in anyway prove the robot could actually "remove" the weeds, we took the robot outside to destroy some garden store plants (dandelions were not in season). 

{% include elements/video.html id="1LL1xRWDjkg" %}

In the video above, the robot is being manually controlled, which is why the destruction of the plant might seem a bit choppy. In a real world scenario, the robot would continue to reposition itself and try and remove plant until it could not longer detect it.

## The Project
We started working on this project even before the official start of the capstone course. We started meeting about a month in advance to start figure out what we wanted to build.

We went about this by having everyone pitch their 3 best ideas and then in a series fo 3 rounds we voted and narrowed down the ideas while also investing more time into the ones that proceeded to validate the feasibility.

The ideas that made it to the final round were:
1. A lake contouring system: a small boat that could autonomously map the floor of small lakes.
2. A tattoo robot: a robot that could someone a tattoo.
3. An agricultural robot: a robot to automate some agricultural task.
4. A hull cleaning robot: a robot that could be used to clean barnacles off of boats.

We decided to go with the agricultural robot, firstly because it would be sufficiently complex, but also we realized that we could modularize the design and thus decrease or increase our scope according to our pace without ever being left with a robot that could do nothing useful. Given that none of us had made an autonomous robot like this before, this was very appealing as we wanted to be as ambitious as we could, but we didn't have a realistic idea of what we could accomplish.

We then had to figure out what agricultural application we would want to solve, when the idea of weed removal robot came to mind. We really liked this idea because we could all understand the problem and imagine what the solution might look like, whereas our knowledge of agricultural industry was limited. This idea hasn't really been commercialized like this before which also made it appealing. 

In keeping with our modular approach, we broke the robot down into two primary subsystems.The first being the weed removal system, also called the cartesian system, which would be responsible for moving the end effector and removing the weed. The second subsystem would be the locomotion system, which would have everything to do with moving the robot in space. We decided to start with the development of the weed removal system.

### The Team
The project could be completed in groups up to 5, however, we had a core group of 4 that had built robots together [befor](https://lhartford.com/projects/scara) so we decided to stick with what worked. Below is a photo of the team at our design symposium.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1747940277/portfolio-site/WeedWarden/171-IMG_6404_1_fw8x1w.jpg "Team Photo at Symposium")

On the far left is [Ethan Dau](https://www.linkedin.com/in/ethan-dau-951a1b1b4/). Ethan was the electical lead on this project, helping with the overall architecture as well as desiging, fabricating and tesitng the electrical system. Ethan was also responsible for developing the firmware related to the cartesian system of the robot. Ethan also helped out with some of the mechanical design when needed. In addition to his technical work, Ethan was also the project manager of the team, scheduling meetings and recording minutes, communicating with the teaching team, maitining the timeline and budget and creating the bulk of the content for the course deliverables.

To the right of Ethan is myself. I was the project technical lead. I was resposible for the overall architecture, functional requirements and generally guiding the technical development of the robot to a particular goal. Additionally, I was the software lead, writing all of the higher level logic of the robot. I also helped out with the firmware, primarily manaaging the communicaiton between devices and adding features for the locomotion system. As the software lead, I also ended up doing the majority of the testing and some mechancial design to rectify issues that I found.

On the right of myself is [Eric Gharghouri](https://www.linkedin.com/in/eric-gharghouri-855a281b5/). Eric's primary contribution was the design, favrication and testing of the locomotion system of the robot.

To the right of Eric is [Varrun Vijayanathan](https://www.linkedin.com/in/varrunv/). Varrun was the mechanical lead, responsible for the overall mechanical design of the robot. Varrun's primary contribution was the design, fabrication and testing of of the cartesian system as well as integrating the cartesian and locomotion systems.

## Early Design Ideas
As mentioned, the full robot system was broken down into two subsystems which would be developed independently and then integrated together.

### Weed Removal System
The weed removal system itself was broken down into two more subsystem, that being the cartesian system and the end effector. Below are some sketches of ideas we had for the two sub systems.

{% capture carousel_images %}
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748017353/portfolio-site/WeedWarden/Mechanical/Early%20Sketches/CoringDrillImg_a7gv0l.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748017354/portfolio-site/WeedWarden/Mechanical/Early%20Sketches/PluckerImg_el6qnm.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748017353/portfolio-site/WeedWarden/Mechanical/Early%20Sketches/DrillImag_zpwoiz.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748017351/portfolio-site/WeedWarden/Mechanical/Early%20Sketches/corexy_X_motion_vfljj8.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748017351/portfolio-site/WeedWarden/Mechanical/Early%20Sketches/coreXY_rail_mounts_fsvv1f.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748017350/portfolio-site/WeedWarden/Mechanical/Early%20Sketches/coreXY_motion_mtndkt.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748017349/portfolio-site/WeedWarden/Mechanical/Early%20Sketches/coreXY_main_h1vnbk.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748017349/portfolio-site/WeedWarden/Mechanical/Early%20Sketches/core_ejynwx.png
{% endcapture %}
{% include elements/carousel.html %}

For the end effector, we primarily considered using a pinch method (like many manual weed pullers) and a coring bit. After some testing, we found that the amount of force required to drive the pincers into the ground was too high, and the coring bit worked well. The only concern was how we were going to get the dirt and plant matter out of the bit between removals.

For the cartesian system, we considered many classic designs used for 3D printers and CNC machines. After some time, we realized that having a 3-axis machine on wheels was redundant. We could place the end effector in a plane with just the locomotion system alone and then we would only need to actuate the z-axis. After talking with our advisor, we decided to go with a hybrid approach where the cartesian system would be able to move the end effector in y and z and then the locomotion system would move in x. This would simplify the control and logic required to position the end effector once a weed was detected, and since the robot was going to be heavy, we worried about it's maneuverability.

### Locomotion System
For the locomotion system, we also explored some classic drive trains for mobile robots, sketches shown below.

{% capture carousel_images %}
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748018635/portfolio-site/WeedWarden/Mechanical/Loco%20Sketches/omni_euwvg3.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748018635/portfolio-site/WeedWarden/Mechanical/Loco%20Sketches/roomba_xbpw5n.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748018633/portfolio-site/WeedWarden/Mechanical/Loco%20Sketches/mecanmum_ex2avo.png
{% endcapture %}
{% include elements/carousel_2.html %}

Our advisor recommended we stay away from omni-directional wheels as they would not work well on outdoor terrain.

## Early Software Development
While Varrun and Eric were busy sketching out concepts, I was doing research and trying to wrap my head around where to get started. I know I would need some sort of edge computing device so I started by comparing some common options.

| Option             | Relevance to Industry | Online Support | Development Difficulty | Cost         | Notes                                                                 |
|--------------------|-----------------------|----------------|------------------------|--------------|-----------------------------------------------------------------------|
| Nvidia Jetson      | High                  | Strong         | Moderate               | $200–$400    | • Optimized for computer vision and machine learning                  |
| Raspberry Pi       | Moderate              | Very Strong    | Easy                   | $200         | • Not used in commercial products                                     |
| Intel Nuc          | High                  | Strong         | Easy                   | $300–$1000   | • Not power efficient<br>• Not as well suited to low level tasks     |
| BeagleBone Black   | Moderate              | Moderate       | Moderate               | $100         | • Better than Pi for real-time tasks                                  |

I decided to go with a Raspberry Pi 5 (RPi5). My first choice was to go with an Nvidia Jetson Nano for its dedicated GPU, high relevance and more than enough compute. But I was dissuaded by reading forums where people talked about how horrible working with these devices was since they had lost official support from Nvidia. The newer version of the Nano, the Orin Nano, would have cost about $750 which was not in the budget for this project.

From what I read online, the RPi5 was a huge upgrade from the RPi4, and should have enough compute for what we wanted to do.

### Camera
With compute selected, choosing a camera was the next step. At this point I wasn't sure what the full sensor suite of the robot would look like, but I knew for sure we would need a camera. For the camera's, I was only considering 2D image sensors, as I believed we could get away with a fixed plan assumption for the location of the dandelion bases. This would simplify our implementation and keeps costs low.

| Option               | Resolution | Max FPS | Pros                                      | Cons                                              | Cost  |
|----------------------|------------|---------|-------------------------------------------|---------------------------------------------------|--------|
| RPi CM3              | 12 MP      | 60–120  | • Official support<br>• Autofocus         | • Limited low light capabilities<br>• No stereo vision | $35   |
| Arducam IMX477       | 12.3 MP    | 12–60   | • Can change lenses<br>• High image quality | • Poor FPS at high res                           | $100  |
| Arducam 8 MP IMX219  | 8 MP       | 30–60   |                                           |                                                   | $35   |

I ended up going with the Raspberry Pi Camera Module 3 (RPi CM3) due to it's direct integration with the RPi5 and it's ability to auto focus.

### Computer Vision Pipeline
I had never done any computer vision before so I started really broad with my initial search, starting my comparing deep and shallow computer vision approaches.

|                      | Pros                                                                 | Cons                                                                                          |
|----------------------|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| **Classic**          | • Simple<br>• Understandable<br>• Does not need training data<br>• Computationally less intense | • Fragile to changes in environment such as lighting, shadows and weed variability<br>• Difficult for classic CV to generalize to many weed species |
| **Deep Learning**    | • Much more robust to changes in environment and weed types<br>• Automatically learns to detect features<br>• More accurate localization | • Need data to train with (can fine-tune pre-trained models but still may need at least 100 samples, 1000 is recommended)<br>• Computationally intense<br>• Black box |

My initial assumption was that classic computer vision would be easier to start with, especially if we limited our scope to just removing dandelions instead of all weeds. I thought training a deep learning model would require too much data to get sufficient accuracy.

After doing some more research, I realized that nobody in robotics was taking a classic approach to computer vision anymore. I hadn't realized that deep computer vision models had become very accessible and could be trained with limited data. The family of models that kept coming up over and over in my searches was YOLO (You Only Look Once). These models are design to be light weight do one-shot object detection.

The creators of the model, Ultralytics, also had documentation specifically on running the model on an RPi5 which also drew me to them. I decided that we would start by trying to train YOLOv11n model, which is the 11th gen, nano size of the YOLO model. The nano size can also be exported to NCNN format which is optimized for running on edge computing devices.

### Bring Up
With the basics in hand, my first job was to get the camera working and some basic GPIO functionality. 

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748020668/portfolio-site/WeedWarden/Software/CV/IMG_3706_1_mxssxh.jpg "Indoor Data Collection")

I have never used a Raspberry Pi 5 before, so I didn't really know where to start. I knew I wanted to use RSO2 for the project, and in order to get Tier 1 support, I needed to install Ubuntu 22.04, so that's where I started.

The only thing I wanted to do was take a picture with the camera. After 3 full days of pulling my hair out trying to get the camera to work, I finally gave up and switched to Raspbian OS and has the camera working in 10 mins. Switching to Raspbian would complicate using ROS2, but I wasn't going to be able to get anything done without the camera.

With the camera now working, I wanted to create a basic ROS2 project that would run on power-up so that I could take the RPi5 outside with a batter and take pictures using just some buttons as inputs. To get ROS2 working I had to run it inside of a Docker container, another tool I had only every dipped my toes into before. The docker container meant that everything inside the container worked nicely, but getting things inside was hard. It took forever to figure out how to make the camera and GPIO's accessible from inside the docker container. But with this all working, ready to start collecting some data.

### Training the Model
We realized that the dandelion season and our development timeline, were not well aligned. There would never be an instance before symposium where we'd have both a robot and live dandelions. To mitigate this, we bought some fake dandelions off of Amazon that we would use for our final demos. But we also wanted to prove that our CV approach had the potential to work in a real environment.

With the dandelion season quickly coming to a close, I decided to try and collect as much data as I could before winter came. At this point, the rest of the robot only existed in CAD, so I quickly whipped together a mobile data collection setup that I could take outside and snap some pics with.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748020362/portfolio-site/WeedWarden/Software/CV/Picture6_ngili1.jpg "Indoor Data Collection")

I started by quickly collecting 100 images of our fake dandelions and then I trained a model with that data just to get an idea of how much data we would need and if this would work. The indoor case is obviously a lot easier than the outdoor case, but even with only 100 images, the model was impressively accurate. 

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748021647/portfolio-site/WeedWarden/Software/CV/map_pkgctc.jpg "Indoor mAP")

I was confident that I could collect enough outdoor data to get a decently working model. So I took to my local parks and scoured for the few remaining dandelions left as fall was coming to an end.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748021643/portfolio-site/WeedWarden/Software/CV/out_c8qjkd.jpg "Outdoor Data Collection")

Over a few days I managed to collect 1400 images of dandelions (and also plain grass), some examples shown below.

{% capture carousel_images %}
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748022210/portfolio-site/WeedWarden/Software/CV/captured_image_20241016_152908_jji4zi.jpg
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748022208/portfolio-site/WeedWarden/Software/CV/captured_image_20241017_153508_fulu22.jpg
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748022209/portfolio-site/WeedWarden/Software/CV/captured_image_20241016_154347_cfb06g.jpg
{% endcapture %}
{% include elements/carousel_3.html %}

We quickly labelled 100 of these images using [roboflow](https://app.roboflow.com/) and trained a model and got decent performance. As we didn't have a need for an outdoor model anytime soon, we put labelling these images on the back burner and worked on them slowly over course of the project.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748021645/portfolio-site/WeedWarden/Software/CV/val_huyfny.jpg "Outdoor Base Performance")

### Model Type
The default type of YOLO model returns the coordinates of a bounding box around identified objects. Since we need to locate the base of the weed in order to remove it, I was not sure how we could use a bounding box to accurately locate the center. I thought of first training the model to predict a small back around the base, but this seemed silly. Luckily before I wasted too much time, I discovered that YOLO also has 'Pose' versions of their models. The pose models can be trained to predict key points along an object in addition to a bounding box. This was exactly what I was looking for. The pose model I made for labelling can be seen below.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748103220/portfolio-site/WeedWarden/Software/CV/model_ag8aib.jpg "Pose Model")

In addition to a base key point, I added two key points for the stem and one for the flower. I figured this would allow the model to better learn how the points are oriented relative to one another rather than having say, a flower and a base key point independently. The additional key points can also be defaulted to when locating a weed in the case where the base is occluded from the camera by the stem or flower.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748103977/portfolio-site/WeedWarden/Software/CV/both_vorpq5.png "Box vs Pose")

One downside of using a pose model is that labelling the images is a lot more labor intensive, as you have to position the key points on every object in addition to the bounding boxes.

## Progress Report #1 - 1.5 Months In
While I was busy with the software, the rest of the team was busy working on the hardware.

### Mechanical
Eric and Varrun had finished the CAD for the weed removal system and had begun fabrication.

{% capture carousel_images %}
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748186379/portfolio-site/WeedWarden/Mechanical/First%20Removal%20Car/front_jtrgie.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748186379/portfolio-site/WeedWarden/Mechanical/First%20Removal%20Car/back_fzynzr.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748186380/portfolio-site/WeedWarden/Mechanical/First%20Removal%20Car/y-axis_h5gkux.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748186380/portfolio-site/WeedWarden/Mechanical/First%20Removal%20Car/zaxis_jyumeb.png
{% endcapture %}
{% include elements/carousel_4.html %}

One thing to note is the bin on the bottom right of the frame. The idea was to have a spade bit mounted inside this bin and then have the coring bit spin and lower itself onto the spade bit to clear out the dirt. This was the simplest possible solution we could come up with the clear the coring bit.

### Electrical/Firmware

Ethan had been working on prototyping the electrical system for th weed removal robot, and updating the firmware from our [previous project](https://lhartford.com/projects/scara) to work for this new robot.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748104987/portfolio-site/WeedWarden/Software/CV/ee_w6tkcz.png "YZ motor control")

{% include elements/button.html link="https://github.com/daue02/481MotorControl" text="Firmware Repo" style="primary" size="lg" %}

## Software Architecture
While the robot was being fabricated and assembled. I began working on the software features that would be needed to bring it to life. I focused on building out what would be needed to functionally test the weed removal system. This meant the camera, the computer vision inference and communication with the Nucleo which controlled the cartesian axes.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748106325/portfolio-site/WeedWarden/Software/CV/arch1_pu1jma.jpg "Arch V1")

{% include elements/button.html link="https://github.com/daue02/481MotorControl" text="Software Repo" style="primary" size="lg" %}

This original architecture was a bit convoluted. I had just started using ROS2 so I was guilty of over-using the tools it provided me and made everything I could it's own node. One problem with this is there is some overhead related to process switching and managing individual processes so have a bunch of process that only run sequentially and then sit idly the rest of the time doesn't really make sense. I would figure that out later.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748107864/portfolio-site/WeedWarden/Software/CV/state_diagram.drawio_2_rie57s.png "State")

This actually ended up being pretty close what worked on the final robot. I imaged the robot driving around, checking the camera for dandelions, and then if it found one stopping to accurately locate it. From there it would position the drill over it and then send a command to the Nucleo to carry out the removal procedure and wait until it was done.

## Term 1 Final Design Review - 3 Months In
By this point the electro-mechanical assembly of the removal system was done.

{% capture carousel_images %}
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748187000/portfolio-site/WeedWarden/Mechanical/Electromechanical%20System/frontassm_m4uguc.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748186999/portfolio-site/WeedWarden/Mechanical/Electromechanical%20System/backassm_vihrhr.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748187000/portfolio-site/WeedWarden/Mechanical/Electromechanical%20System/boards_jxgtpa.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748187000/portfolio-site/WeedWarden/Mechanical/Electromechanical%20System/schem_yk1qad.png
{% endcapture %}
{% include elements/carousel_5.html %}

The Nucleo is able to commutate the stepper motors and position the drill along two axes with 0.1mm precision. The Nucleo can also receive coordinates via UARt from the Pi and will move the end effector ot that location.

{% include elements/video.html id="5beaoe6T68Q" %}

During the design review, the teaching staff gave us some valuable, and some not so valuable feedback about our design. One thing they questioned was the height of the robot, and the validity of our removal method. They were right, the robot was almost ridiculously large, and we hadn't really proven that the removal method could actually remove the 12" taproot of a dandelion. They also recommended we abandon locomotion from the scope but we ignored that.

## Initial Design Review Term 2
Over the christmas break, progress slowed. Varrun added the camera and LED ring to the assembly, I procured the electrical components of the locomotion system and wrote the driver and functional logic or them.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748188593/portfolio-site/WeedWarden/Mechanical/christmas%20break/IMG_3960_1_zzr2de.png "Camera and Light")

### Motor Control
The locomotion motors I selected were [high torque DC motors](https://ca.robotshop.com/products/e-s-motor-36d-dc-planetary-gearmotor-w-encoder-24v-23rpm?qd=bd213a3b156f6f37e21d00c80bcbb270). We chose these motors due to their low cost, high power density and simple control scheme. The driver is a [Cytron 20A dual output DC motor driver](https://ca.robotshop.com/products/cytron-20a-6v-30v-dual-dc-motor-driver). 

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748188594/portfolio-site/WeedWarden/Mechanical/christmas%20break/IMG_3987_1_cxdezm.png "Locomotion Driver Development")

To control each motor channel only requires a boolean direction and PWM speed input. I wanted the RPi5 to handle all of the locomotion logic, since it would be the one running the control loops and sensor fusion and would need to generate motor commands. Unfortunately, this was only partially possible. The RPi5 is equipped with a hardware PWM peripheral, but lacks a hardware input capture peripheral. As a result, I needed to use the Nucleo to capture the encoder pulses. This meant the Nucleo would need to send the encoder ticks to the RPi5 so the RPi5 could compute the wheel odometry. This added an additional element of complexity when trying to architect the project as I needed to be cognizant of congestion on the UART bus.

## Major Autonomy Milestone #1 - Basic Demo
It was very hard for me to wrap my head around how I was going to make this robot "autonomous". To guide my development and make sure I was working on impactful and high leverage tasks, I came up with a simple first demonstration to work towards. The first demo would entail:
* The robot "starts" in autonomous mode.
* Drives forward at a constant velocity.
* The robot would be taking pictures checking for dandelions.
* If the robot detected a dandelion, it would stop, and then re-position itself until the y-axis was aligned with the dandelion. 
* Once aligned, the robot would send the y-axis coordinated to the Nucleo to move the drill over the dandelion.

It was with this demo in mind that the following architecture was made.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748274831/portfolio-site/WeedWarden/Software/archv2_1_bsu9zd.png "Basic Demo Architecture")

**Changes from previous architecture:**
* More appropriate use of OOP.
* Converted the camera, homography and CV model nodes into a single class.
* UART node was changed to a class that could be instantiated by multiple nodes
* Simplified node logic since they didn't have to request images, inferences or UART comms asynchronously.

### Locomotion Architecture
The basic composition of the locomotion system is:
* A **motor control class** for generating PWM outputs and implementing hardware limitations and safeguards.
* A **controller node** which included a timer which would trigger the control loop.
* A **localization node** which computes the robot's localization (wheel odometry at this point).
* A **PID class** which which generates control outputs based on error between set point and current pose estimate.

During the demo, the decision node would request a velocity from the controller. Then if a dandelion was detected, it would request the controller to change the robot's pose in the x-axis. The controller would do this using PID control. The error would be computed between the requested and estimated pose. The estimated pose was computed by the localization node. The controller node would request a pose, which would prompt the localization node to request the encoder ticks from the Nucleo and then update and return the pose estimate to the control node.

### Hardware Progress

#### Frame Re-Design
In the meantime, Varrun was working on a re-design of the frame to make the robot shorter and more compact. This was following feedback we got in our previous design review, where the teaching staff thought the robot was a bit tall.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748278269/portfolio-site/WeedWarden/Mechanical/framce.drawio_loon2m.png "Frame Re-Design")

The robot's original height was being driven by:
* The 10cm long hole saw.
* The 10cm tall spade bit to empty the hole saw, which the bit needed to clear. 

While this was a good method for clearing the bit, it was having too much impact on the rest of the design. We decided to ignore the need to clear the bit, and solve the problem with a more complicated solution if time permitted. If time ran out, we could always just drill out the weed with a regular drill bit and reduce claims about weed "removal".

#### Locomotion
In parallel, Eric was working designing and building the locomotion system.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748278209/portfolio-site/WeedWarden/Mechanical/locomotions.drawio_ucxw3d.png "Locomotion Design")

The drive train would be front wheel differential drive with two passive wheels at the back which would slide during turns.

#### Electrical
Ethan was busy planning out the electrical layout of the various board and fabricating and assembling the harnessing between them.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748278179/portfolio-site/WeedWarden/Mechanical/electrical.drawio_at043h.png "Electrical Design")

#### Fully Assembly CAD
It wasn't long until the CAD for the full system was more or less complete.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748278346/portfolio-site/WeedWarden/Mechanical/full_mimzit.jpg "Full Assembly CAD")

We felt that visually, this was a major improvement over our previous design in terms of design refinement and professional quality. If we said "this robot removes weeds", a non-technical person would have a good idea of how that might work.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748278148/portfolio-site/WeedWarden/Mechanical/CADupdate.drawio_fwauca.png "Full Assembly CAD")

Unfortunately, as pretty as this design was, it was full of interesting problems to solve.



* Putting wheels on the new frame
* Collecting more indoor data
* Developing robust homography
* 






## Development Outline
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

