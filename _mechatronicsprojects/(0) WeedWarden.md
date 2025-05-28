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

This project was our 4th year capstone at the University of Waterloo, earning a 97% and the Best Prototype Award (2nd highest distinction) at the design symposium (I missed the photo below due to a job interview).

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1747940403/portfolio-site/WeedWarden/21-IMG_6842_1_qkzr9c.jpg "Award Photo")

We set out to build a "Roomba for your lawn"—a robot that autonomously blends up weeds nightly, eliminating them over time without manual labor or pesticides.

For our final review, we recorded the robot autonomously clearing our test setup. In the first video, it follows a pre-defined path, detects fake weeds, and removes them using computer vision and onboard decision-making. Drill speed and depth are limited for safety.

{% include elements/video.html id="LF1d6aeK7RU" %}

The next video demonstrates repeatability: the robot completes two autonomous clears of the turf, with weeds placed arbitrarily and the field reset between runs.

{% include elements/video.html id="RoHv5wQGr44" %}

To test real plant removal, we took the robot outside (dandelions were out of season, so we used garden store plants). The robot is manually controlled in this clip, so removal appears choppy; in practice, it would reposition and retry until the weed is gone.

{% include elements/video.html id="1LL1xRWDjkg" %}

## The Project
We began working on this project about a month before the official start of the capstone course, meeting early to brainstorm and refine ideas. Each team member pitched three concepts, and through several voting rounds, we narrowed them down while validating feasibility.

Final contenders included:
1. A lake-mapping autonomous boat
2. A tattoo robot
3. An agricultural robot
4. A hull-cleaning robot

We chose the agricultural robot for its complexity and modularity, allowing us to adjust scope as needed. With limited experience in autonomous robotics, this flexibility was key. Weed removal stood out as an approachable, impactful problem that hadn't been widely commercialized.

To keep development manageable, we split the robot into two main subsystems: the weed removal (cartesian) system for manipulating the end effector, and the locomotion system for moving the robot. We started by focusing on the weed removal system.

### The Team

Our core group of four had previously built robots together ([see previous project](https://lhartford.com/projects/scara)), so we stuck with what worked. Below is a photo of the team at our design symposium.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1747940277/portfolio-site/WeedWarden/171-IMG_6404_1_fw8x1w.jpg "Team Photo at Symposium")

- **[Ethan Dau](https://www.linkedin.com/in/ethan-dau-951a1b1b4/):** Electrical lead and project manager. Designed, fabricated, and tested the electrical system, developed firmware for the cartesian system, managed meetings, timeline, budget, and course deliverables.
- **[Myself](https://www.linkedin.com/in/logan-hartford-31b084195/):** Technical and software lead. Oversaw overall architecture, functional requirements, and technical direction. Wrote all higher-level software, managed device communication, contributed to firmware and mechanical design, and led testing.
- **[Eric Gharghouri](https://www.linkedin.com/in/eric-gharghouri-855a281b5/):** Designed, fabricated, and tested the locomotion system.
- **[Varrun Vijayanathan](https://www.linkedin.com/in/varrunv/):** Mechanical lead. Designed, fabricated, and tested the cartesian system and integrated it with the locomotion system.

## Early Design Ideas

The robot was divided into two main subsystems: weed removal and locomotion, each developed independently before integration.

### Weed Removal System

This system had two parts: the cartesian mechanism and the end effector. Below are early sketches of both:

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

We tested both a pinch method and a coring bit for the end effector. The coring bit was chosen due to lower force requirements, though clearing debris from the bit remained a challenge.

For the cartesian system, we initially considered full 3-axis motion but realized that combining y/z actuation with x-axis movement from the drive system was simpler and more practical for a heavy robot. This hybrid approach reduced complexity and improved maneuverability.

### Locomotion System

We explored several classic mobile robot drive trains:

{% capture carousel_images %}
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748018635/portfolio-site/WeedWarden/Mechanical/Loco%20Sketches/omni_euwvg3.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748018635/portfolio-site/WeedWarden/Mechanical/Loco%20Sketches/roomba_xbpw5n.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748018633/portfolio-site/WeedWarden/Mechanical/Loco%20Sketches/mecanmum_ex2avo.png
{% endcapture %}
{% include elements/carousel_2.html %}

Omni-directional wheels were ruled out due to poor performance on outdoor terrain, as advised by our supervisor.

## Early Software Development

While Varrun and Eric worked on concepts, I researched edge computing options for the robot:

| Option           | Industry Relevance | Online Support | Dev Difficulty | Cost        | Notes                                                      |
|------------------|-------------------|----------------|----------------|-------------|------------------------------------------------------------|
| Nvidia Jetson    | High              | Strong         | Moderate       | $200–$400   | Optimized for CV/ML, but older models lack support         |
| Raspberry Pi     | Moderate          | Very Strong    | Easy           | $200        | Not used commercially, but easy to develop on              |
| Intel Nuc        | High              | Strong         | Easy           | $300–$1000  | Not power efficient, less suited for low-level tasks       |
| BeagleBone Black | Moderate          | Moderate       | Moderate       | $100        | Better real-time performance than Pi                       |

I chose the Raspberry Pi 5 for its improved performance and strong community support. Nvidia Jetson Orin Nano was too expensive, and older Jetsons had poor support.

### Camera

For vision, I considered only 2D image sensors to keep things simple and affordable:

| Option              | Resolution | Max FPS | Pros                        | Cons                              | Cost |
|---------------------|------------|---------|-----------------------------|-----------------------------------|------|
| RPi CM3             | 12 MP      | 60–120  | Official, autofocus         | Limited low light, no stereo      | $35  |
| Arducam IMX477      | 12.3 MP    | 12–60   | Swappable lenses, high IQ   | Low FPS at high res               | $100 |
| Arducam IMX219      | 8 MP       | 30–60   |                             |                                   | $35  |

I picked the RPi Camera Module 3 for its autofocus and seamless RPi5 integration.

### Computer Vision Pipeline

I compared classic vs. deep learning approaches:

| Approach      | Pros                                                        | Cons                                                      |
|---------------|-------------------------------------------------------------|-----------------------------------------------------------|
| Classic       | Simple, no training data, less compute                      | Fragile to lighting/weed variation, hard to generalize    |
| Deep Learning | Robust, learns features, accurate localization              | Needs training data, more compute, less interpretable     |

Initially, I thought classic CV would be easier, but research showed deep learning (especially YOLO models) is now standard and accessible, even with limited data. Ultralytics’ YOLO had good RPi5 support, so I chose to start with YOLOv11n (nano), which can be exported to NCNN for edge devices.

### Bring Up

My first task was to get the camera and basic GPIO working on the Raspberry Pi 5. 

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748020668/portfolio-site/WeedWarden/Software/CV/IMG_3706_1_mxssxh.jpg "Indoor Data Collection")

I started with Ubuntu 22.04 for ROS2 Tier 1 support, but after three days struggling to get the camera working, I switched to Raspbian OS, which had the camera running in 10 minutes. This made ROS2 setup trickier, requiring it to run in a Docker container. Making the camera and GPIO accessible inside Docker took some effort, but once set up, I could take the RPi5 outside with a battery and use buttons to collect data.

### Training the Model

Dandelion season didn't align with our development timeline, so we bought fake dandelions for demos and rushed to collect real data before winter. I built a quick mobile setup to gather images outside.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748020362/portfolio-site/WeedWarden/Software/CV/Picture6_ngili1.jpg "Indoor Data Collection")

Starting with 100 indoor images of fake dandelions, I trained a model to gauge data needs. Even with this small set, the model was impressively accurate indoors.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748021647/portfolio-site/WeedWarden/Software/CV/map_pkgctc.jpg "Indoor mAP")

Confident, I collected 1400 outdoor images of dandelions and grass in local parks.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748021643/portfolio-site/WeedWarden/Software/CV/out_c8qjkd.jpg "Outdoor Data Collection")

Some examples:

{% capture carousel_images %}
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748022210/portfolio-site/WeedWarden/Software/CV/captured_image_20241016_152908_jji4zi.jpg
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748022208/portfolio-site/WeedWarden/Software/CV/captured_image_20241017_153508_fulu22.jpg
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748022209/portfolio-site/WeedWarden/Software/CV/captured_image_20241016_154347_cfb06g.jpg
{% endcapture %}
{% include elements/carousel_3.html %}

We quickly labeled 100 images using [roboflow](https://app.roboflow.com/) and trained a model with decent results. Since we didn't need an outdoor model immediately, we labeled the rest gradually.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748021645/portfolio-site/WeedWarden/Software/CV/val_huyfny.jpg "Outdoor Base Performance")

### Model Type

Standard YOLO models output bounding boxes, but we needed to pinpoint the weed base. I discovered YOLO 'Pose' models, which predict key points in addition to boxes—perfect for our needs. My pose model included key points for the base, stem, and flower, improving localization even if parts were occluded.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748103220/portfolio-site/WeedWarden/Software/CV/model_ag8aib.jpg "Pose Model")

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748103977/portfolio-site/WeedWarden/Software/CV/both_vorpq5.png "Box vs Pose")

The main downside: pose labeling is much more labor intensive, since each key point must be marked on every object.

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

While the robot was being fabricated, I focused on developing the core software features needed to test the weed removal system: camera integration, computer vision inference, and communication with the Nucleo for cartesian axis control.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748106325/portfolio-site/WeedWarden/Software/CV/arch1_pu1jma.jpg "Arch V1")

{% include elements/button.html link="https://github.com/daue02/481MotorControl" text="Software Repo" style="primary" size="lg" %}

My initial ROS2 architecture was overly complex, with too many nodes running mostly sequentially, leading to unnecessary overhead. I later streamlined this for efficiency.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748107864/portfolio-site/WeedWarden/Software/CV/state_diagram.drawio_2_rie57s.png "State")

Despite the complexity, this setup was close to the final working system: the robot would drive, scan for dandelions, stop to localize them, position the drill, and command the Nucleo to perform removal.

## Term 1 Final Design Review - 3 Months In

By this point, the electro-mechanical assembly of the removal system was complete.

{% capture carousel_images %}
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748187000/portfolio-site/WeedWarden/Mechanical/Electromechanical%20System/frontassm_m4uguc.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748186999/portfolio-site/WeedWarden/Mechanical/Electromechanical%20System/backassm_vihrhr.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748187000/portfolio-site/WeedWarden/Mechanical/Electromechanical%20System/boards_jxgtpa.png
https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748187000/portfolio-site/WeedWarden/Mechanical/Electromechanical%20System/schem_yk1qad.png
{% endcapture %}
{% include elements/carousel_5.html %}

The Nucleo could now control the stepper motors and position the drill along two axes with 0.1mm precision, receiving coordinates via UART from the Pi.

{% include elements/video.html id="5beaoe6T68Q" %}

During the review, staff questioned the robot's height and whether our removal method could handle a dandelion's 12" taproot. They also suggested dropping locomotion from scope, but we decided to keep it.

## Initial Design Review Term 2

Progress slowed over the winter break. Varrun added the camera and LED ring, while I sourced the locomotion electronics and developed their drivers and logic.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748188593/portfolio-site/WeedWarden/Mechanical/christmas%20break/IMG_3960_1_zzr2de.png "Camera and Light")

### Motor Control

We chose [high torque DC motors](https://ca.robotshop.com/products/e-s-motor-36d-dc-planetary-gearmotor-w-encoder-24v-23rpm?qd=bd213a3b156f6f37e21d00c80bcbb270) for their low cost, power density, and simple control. The [Cytron 20A dual output driver](https://ca.robotshop.com/products/cytron-20a-6v-30v-dual-dc-motor-driver) was used.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748188594/portfolio-site/WeedWarden/Mechanical/christmas%20break/IMG_3987_1_cxdezm.png "Locomotion Driver Development")

Each motor channel uses a direction and PWM speed input. The RPi5 handles locomotion logic and control loops, but lacks hardware input capture for encoders. Therefore, the Nucleo captures encoder pulses and sends tick counts to the RPi5 for odometry, adding some UART bus complexity.

## Major Autonomy Milestone #1 – Basic Demo

To make autonomy manageable, I set a clear first milestone: a simple demo where the robot would:

- Start in autonomous mode.
- Drive forward at a constant speed.
- Continuously check for dandelions.
- Stop and align its y-axis with a detected dandelion.
- Command the Nucleo to move the drill over the weed.

This guided the following architecture:

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748274831/portfolio-site/WeedWarden/Software/archv2_1_bsu9zd.png "Basic Demo Architecture")

**Key improvements over the previous version:**
- Better use of OOP.
- Combined camera, homography, and CV model into a single class.
- Refactored UART as a reusable class.
- Simplified node logic by handling images, inference, and UART comms synchronously.

### Locomotion Architecture

The locomotion system included:

- A **motor control class** for PWM output and safety.
- A **controller node** with a timer-driven control loop.
- A **localization node** for wheel odometry.
- A **PID class** for control output based on pose error.

During the demo, the decision node requested velocity from the controller. On dandelion detection, it requested a pose change along the x-axis, handled by PID control using feedback from the localization node, which updated pose estimates from encoder ticks sent by the Nucleo.

### Hardware Progress

#### Frame Re-Design
Varrun redesigned the frame to make the robot shorter and more compact, addressing feedback that it was too tall.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748278269/portfolio-site/WeedWarden/Mechanical/framce.drawio_loon2m.png "Frame Re-Design")

The original height was due to the 10cm hole saw and spade bit for clearing debris. To simplify, we deprioritized automatic bit clearing, focusing on a more compact design and leaving advanced solutions for later.

#### Locomotion
Eric developed the locomotion system:

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748278209/portfolio-site/WeedWarden/Mechanical/locomotions.drawio_ucxw3d.png "Locomotion Design")

The robot uses front wheel differential drive with two passive rear wheels for stability during turns.

#### Electrical
Ethan planned the electrical layout and assembled the harnesses:

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748278179/portfolio-site/WeedWarden/Mechanical/electrical.drawio_at043h.png "Electrical Design")

#### Full Assembly CAD
The complete system CAD came together quickly:

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748278346/portfolio-site/WeedWarden/Mechanical/full_mimzit.jpg "Full Assembly CAD")

This design looked much more refined and professional, making the robot’s function clear even to non-technical viewers.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748278148/portfolio-site/WeedWarden/Mechanical/CADupdate.drawio_fwauca.png "Full Assembly CAD")

Despite its polished appearance, the design still presented many engineering challenges.

### Locomotion & Weed Removal System Integration
Soon after the completion of the CAD, the new removal system was complete and the locomotion system was added.

{% include elements/video.html id="zaWzhWqcslc" %}

The team was in a rush to get the system to me before they left for the long weekend, so the robot didn't have any tires on the wheels yet.

### Improving Indoor Computer Vision Performance
To boost model reliability, we needed more indoor data. Moving the system by hand was tedious, so after adding stick-on weather strips to the wheels for grip, I quickly collected 400 images of fake dandelions in various positions.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748283052/portfolio-site/WeedWarden/Mechanical/IMG_4022_1_1_l8hahv.jpg "Indoor Data Collection")

#### Homography Transform

After the vision model predicts a dandelion base, its pixel location must be mapped to the robot's frame for targeting. Since the robot operates on a flat, known surface, a simple homography transform sufficed.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748283628/portfolio-site/WeedWarden/Software/badhomo_1_qg9lns.jpg  "Bad Homography Calibration")

Using [OpenCV's](https://docs.opencv.org/4.x/index.html) `findHomography`, I first tried aligning a ruler to the y-axis and using points along it for calibration. This was inaccurate—errors reached 10mm.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748283868/portfolio-site/WeedWarden/Software/ransac_1_ppgiks.jpg  "Good Homography Calibration")

To improve, I designed a 17-point calibration fixture. Using a laser diode on the end effector, I aligned the fixture, then used CAD for ground truth distances and OpenCV to click pixel locations.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748284192/portfolio-site/WeedWarden/Software/cims_lfol98.jpg  "Fixture Dimensions")

With these 17 pairs, I used RANSAC (RANdom SAmple Consensus) to robustly compute the transformation matrix, as more than 4 points require a robust estimator. The transform matrix generated with this method, had an max error of 0.1mm across the working area.

#### Results

After training new models with and without the additional data and applying the improved homography transform, we evaluated each model on 5 images across 5 dandelion configurations, measuring true base positions.

| Model Description                     | Dist. (mm) | Point Conf. | Box Conf. | Point Type | Num. Boxes |
|----------------------------------------|------------|-------------|-----------|------------|------------|
| Original indoor pose model             | **92.52**  | 0.90        | 0.67      | **1.03**   | **2.20**   |
| Only new indoor data                   | 10.01      | 0.95        | 0.72      | 0.83       | 1.20       |
| All indoor data                        | **8.27**   | 0.93        | 0.78      | **0.50**   | **1.03**   |
| Old indoor model retrained on new data | 11.23      | 0.95        | 0.71      | 0.97       | 1.20       |

The best model achieved 10x better base localization accuracy, more consistent base key point predictions, and fewer false positives compared to the initial model. Our goal was to be able to target dandelion bases with greater than 12.5mm accuracy, and given that our cartesian system was accurate to 0.1mm, this was promising.

## Midterm Design Review - 5.5 Months In
Leading up to the midterm design review, we addressed several reliability issues with the locomotion system—bolts, couplers, and grub screws kept coming loose, causing slack and shaft slipping. Fully resolving these took most of the term. On the software side, odometry accuracy was a challenge due to an incorrect stated gear ratio, which I determined empirically. There were also data typing issues in Pi–Nucleo communication.

{% include elements/video.html id="7L5U28Yua8I" %}

With locomotion mostly stable, I integrated all parallel software features into "autonomous mode" the night before the review. Despite some integration hiccups, I achieved a working milestone by midnight.

### Feedback
During our design review, the teaching team doubted our drivetrain. They pointed out that grub screws weren't reliable for securing the drive wheels (they were right) and that two fixed passive rear wheels would hinder turning (also correct). We were initially defensive, expecting higher torque motors to solve our issues—but we were wrong.

> Side Note: I accidentally ordered 230RPM motors instead of 23RPM, so the robot moved too fast with little torque. With the correct 23RPM motors, we hoped for better turning, but the drivetrain design was still a problem.

One comment that stood out was, "make sure you don't oversell what you've got here." I was frustrated, feeling we had achieved a lot in a short time, but in hindsight, the advice was partly justified, even if poorly delivered.

## Re-Branding

The feedback about "overselling" stemmed from our focus on autonomous mobility rather than fully eradicating weeds. Dandelions regrow from deep taproots, which our design didn't address. After discussion, we shifted from "weed removal" to "weed control."

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748441533/portfolio-site/WeedWarden/Mechanical/41UXkkha0iL._AC__1_o3oppt.jpg "Weed Spinner")

Instead of removing weeds, our robot would blend up the visible parts nightly using a bit like the one above, suppressing regrowth by depriving the plant of light. This approach is used by [other products](https://tertill.com/) and supported by [research](https://www.tandfonline.com/doi/abs/10.1080/00288233.1967.10426362).

## Re-Design of the Locomotion System

Initially, the team was hesitant to redesign the drivetrain before testing the new high-torque motors. However, I suspected the slippery TPU wheels and dual passive wheels would still cause traction and friction issues, especially given the robot’s weight. To demonstrate this, I ran my own tests.

### caster Wheel Testing
I attached a caster wheel from Home Depot to the back of the robot and compared its maneuverability to the original setup by driving in an arc. The videos below show the dramatic improvement:

{% include elements/video.html id="dNVoFog3w6w" %}
{% include elements/video.html id="FsFwFDhB-sk" %}

The caster made turning much easier, proving the need for a new drivetrain. This convinced the team to move forward with a redesign.

{% include elements/video.html id="UNZv2nUFPPE" %}

Finally, some fun driving.

### Developing New Tires
Since making custom rubber tires seemed daunting, I experimented with silicone, which was readily available.

{% include elements/video.html id="100GDV_8_CU" %}

Key challenges in designing the 3D printed mold included:
* Optimizing air hole density and size
* Finding an effective mold release agent
* Deciding how much to undersize the tire for a snug fit

Stretching the soft silicone helped stiffen the tires. 

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1748443177/portfolio-site/WeedWarden/Mechanical/mold_1_fxfrkq.jpg "Weed Spinner")

After successful small-scale tests, I made a full-sized version—the improvement in traction was immediate.

{% include elements/video.html id="YU1iyJ5kySo" %}

Watching the video, you can see the right side of the robot jerks more aggressively as the tire maintains traction while the TPU tire slips out.

### Drivetrain Testing

To choose the best drivetrain, we tested four passive wheel setups:
1. Original dual fixed wheels
2. Wide dual fixed wheels (less friction)
3. Single caster wheel
4. Dual caster wheels

We ran these tests:
1. **Zero point turn:** Opposite drive wheels, measure rotation/displacement.
2. **Arc turn:** Drive in an arc, measure deviation.
3. **Side hilling:** Max slope before sliding.
4. **Tipping point:** Force at which wheels lift during drilling.
5. **Circuit test:** Timed course, note handling.

#### Zero Point Turn – Single Caster
{% include elements/video.html id="2z3DASWAQAI" %}

#### Arc Turn – Dual Caster
{% include elements/video.html id="lbXCkQBkh_Q" %}

#### Tipping Point – Thin Passive Wheels (Original)
{% include elements/video.html id="0JelYa8wTN0" %}

#### Circuit Test – Thin Passive Wheels (Original)
{% include elements/video.html id="D_K4q7je0Qk" %}

#### Circuit Test – Single Caster Wheel
{% include elements/video.html id="cjR8pI3jryk" %}

**Summary:**
- Casters outperformed passive wheels in all driving tests.
- Single caster was more agile but slightly less stable than 4-wheel setups.
- Casters struggled with side hilling.
- Single caster was more maneuverable than dual caster.

We prioritized maneuverability over maximum stability, choosing the single caster. In hindsight, consulting mobile robot research and kinematic models could have saved time.





## Development Outline
- Re-branding/shifting focus - Why? Feedback, decisions
  - Weed control vs weed removal
- Re-design of the locomotion system
  - caster wheel
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

