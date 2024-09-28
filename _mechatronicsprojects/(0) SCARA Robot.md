---
name: SCARA Robot
tools: [STM32, PlatformIO, C++, SolidWorks, 3D Printing]
image: https://res.cloudinary.com/dlfqn0wvp/image/upload/v1724861923/portfolio-site/grack/IMG_1314_1_w4zpc4.jpg
description: A SCARA Pick and Place Robot.
slug: scara
---

# SCARA Robot
<p class="post-metadata text-muted">
  April 20th, 2024
</p>
***
{% capture list_items %}
Design Challenge
The Plan
Inverse Kinematics
Stepper Motor Drivers
CAD
First Build
Limit Switch Problem
Z-Axis Problmem
Slack Problem
Joint 1 Re-Design
Symposium
{% endcapture %}
{% include elements/list.html title="Table of Contents" type="toc" %}

## Design Challenge

This project was completed as part of a design project course at the University of Waterloo.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1727535445/portfolio-site/grack/problem_description/challenge_enpxc6.jpg "Design Challenge")

The challenge was to design and electro-mechanical system that could move a 50x50mm, solid PLA 20 sided die, from a start location to and end location with a delta of 300x150x75mm from the start location. Additionally, the final design could not cost more than $300 and could not make use of projectile motion.

Each team also had to pick two additional design objective from a list that they would have to prove their design meets. Our group chose repeatability and accuracy as our design objectives.

The final design had to be complete within 3 months and ready for an in person functional demo, where the design would be scored by the teaching team judges.

### The Team
The project was to be completed in groups of 4.
![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1727536407/portfolio-site/grack/problem_description/IMG_1153_2_1_xksul1.jpg "Symposium Group Pic")

On the far left is [Ethan Dau](https://www.linkedin.com/in/ethan-dau-951a1b1b4/). Ethan's responsibilities included mechanical design, fabrication and assembly as well as some firmware when he had the bandwidth. Ethan also helped out with project management related tasks.

To the right of Ethan is [Varrun Vijayanathan](https://www.linkedin.com/in/varrunv/). Varrun was the mechanical lead, responsible for the overall mechanical design and the majority of the CAD and he also did some firmware.

To the right of Varrun is myself. I was the team lead, both for technical and project management related duties. Additionally, I was primarily responsible for developing the firmware and controls for the robot. I also heavily supported the electrical design and was in charge of overall system integration and debugging.

On the far right is [Eric Gharghouri](https://www.linkedin.com/in/eric-gharghouri-855a281b5/). Eric was responsible for the electrical system architecture, electrical fabrication and testing as well as some firmware support.


## The Plan
With the team in place and the challenge understood, it was time to start formulating a plan. Our first objective was to create a design proposal that would be reviewed by the teaching team. Our team presented two concepts but we knew which one we were interested in working on.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1727538790/portfolio-site/grack/problem_description/sketch_bxgocj.jpg "Initial Sketch")

The idea we decided to go with was a SCARA style robot arm. We chose this design since it is common for pick and place applications like this once. Given the singular nature of the challenge however, the SCARA robot was certainly not the easiest, most effective or most efficient way we could have solved this design problem, but it was the one we were interested in working on. We also considered creating a cartesian robot and a direct conveyance system but found them too boring. Our general philosophy for this project was that we wanted to take the path that would result in the maximum amount of learning and give us all valuable design experience.

From the rough sketch, an electrical system architecture was defined.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1727538791/portfolio-site/grack/problem_description/Final_System_Circuit_2_tdwage.jpg "Electrical Architecture")

On the left of the diagram there are 6 limit switches, two for each of the axes of motion. In the center is our microprocessor, which was a NUCLEO-STM32 development board. We chose to use and STM32 because it would give better peripheral access than an arduino for developing drivers. In terms of actuators, the three axes of motion would all be driven by stepper motors. Stepper motors are cheap and provide precise position control so they were suitable for this project. The end effector actuator was a servo since it was well suited to the requirements of a gripper. The system would be supplied by 12V which would power the Nucleo and the motors and then a 5V buck was included to drive the servo motor. The stepper motors would be driven by a 4-motor stepper motor driver shield. We planned to interface with the robot via and buttons and joystick which captures in the HMI (Human Machine Interface) section in the bottom right.

![alt text](https://res.cloudinary.com/dlfqn0wvp/image/upload/v1727539406/portfolio-site/grack/problem_description/fwarch.drawio_2_1_ewewx4.png "DW Architecture")


The firmware architecture was designed to be modular and to have proper separation of concerns. The program flow would be that the main program polled the interface using the HMI HAL and when needed, would send position requests to the controls functional layer would would computed the inverse kinematics (IK) and determine the optimal motor deltas to achieve the requested position. The controls functional layer would then request the motor deltas and desired speed from the motor hardware abstraction layer which would set up and start the timers that drive the motors. All the while the limit switch hall would trigger a hardware interrupt if one of the switches was contacted and update the state machine which would halt the robots operations. The HMI HAL ended up functioning more like a functional layer since main.c called it directly and it is also where the state machine lived.


## Inverse Kinematics
* Explain development plan
* Show simulation
* Show simulation with physical contraints
* Show demo with motors

## Stepper Motor Drivers
* Show the implementation of the driver incode
* Talk about gain scheduling and why we added it

## CAD
* Carousel of the CAD
* Talk about some of the design decisions
  * Link 2 being belt driven
  * Keeping stepper motor at the end of link 2
  * Servo on the gripper

## First Build
* Some pictures
* Talk about some of the challenges
  * Limit switch wires weren't long enough
  * Problems with the nucleo sheild

## Limit Switch Problem
* Describe the problem and why it was unexpected
  * Limit switched behaved erratically
  * Bouncing like craxy
  * Triggered by motor noise
  * Initially thought it was entirely a noise issue becasue we did have a cap
  * Adding a bigger cap did not help
* Describe the solution
  * Better debounce circuit

## Z-Axis Problmem
* Describe the problem
  * Using a small motor to save weight at the end effector
  * Skipping at higher speeds
* Describe the solution
  * Gain scheduling
  * Changing stepping
  * Thinner rack
  * tighter tolerances

## Slack Problem
* Describe the problem
  * Link 1 and Link 2 were both slacking due to plastic deformation
  * Causing high friction which was causing belt 2 to skip
  * Slack in the belt since we could not tighten it enough and even if it did, it would deform over time
* Describe the solution
  * Redesigned link 1 to used a much larger thrust bearing and a larger radial bearing
  * Incerased the base of support
  * This allowed the ID to be larger, which meant more clamping force, and more plastic
  * Added thrust washed to both sides of all thrust bearings
  * Added in machine grease
  * Redesigned the link 2 belt tensioner and printed out of solid PLA
  * Gain scheduling to descrease the impact from movelments

## Symposium
* Sexy pictures
* Videos validating design objectives
