---
title: Meta-Learning
tags: [Books, L2L, Self-Improvement, Machine Learning]
style: 
color: dark
description: How to Learn Deep Learning and Thrive in the Digital Age
author: Radek Osmulski
---

{% capture list_items %}
Learning Machine Learning
Becoming a Developer
How to Learn
The Hidden Game of ML
How to Structure a Machine Learning Project
How to Win at Kaggle
The Best Hardware for Deep Learning
Side Notes
On Finding a Job
The Party is On Twitter
Sharing Your Work
What to Focus On
Find a Mentor
The Regrets of fast.ai Students
Tap in to the Power of Community
Energize
{% endcapture %}
{% include elements/list.html title="Table of Contents" type="toc" %}

## Learning Machine Learning
* Learn the absolute minimum you need before starting [Practical Deep Learning for Coders](https://course.fast.ai/)
* Start working through the course.

### How to Fast.AI
1. Start with the video lesson.
2. Then head to the book chapter and run the code in the notebook.
    * Focus on understanding what's going on in each cell.
3. Try and recreate the pipeline from  the notebook or video.
    * You can refer back for help but try to do this using your notes, documentation and whatever else.
4. Apply what you have learned to a new dataset.

## Becoming a Developer
Make use of long, uninterrupted work sessions.
* Put away your phone.
* Clear your browser tabs.
* Move to a productive workspace.

### Flow
Good developers spend a lot of time studying their editors and swear by the ones that don't require you to lift a finger. When you reach for you mouse your flow is interrupted.

## How to Learn
Make your learning active.
* Take notes when you watch the videos or read the note books.
* Review you notes.
* Focus on practical application of what you are learning.
* Create mini-projects that you can share with the world.

## The Hidden Game of ML
The hidden game is the ability to generalize to unseen data.
* [How (and why) to create a good validation set.](https://www.fast.ai/2017/11/13/validation-sets/)
* [Learning From Data: A Short Course.](https://www.amazon.com/Learning-Data-Yaser-S-Abu-Mostafa/dp/1600490069)
* [Python for Data Analysis](https://wesmckinney.com/book/)
* [How to deploy.](https://youtu.be/5L3Ao5KuCC4)
* [Building Machine Learning Powered Applications: Going from Idea to Product](https://www.amazon.com/Building-Machine-Learning-Powered-Applications/dp/149204511X)

## How to Structure a Machine Learning Project
1. Create a good train-validation split.
2. Create a baseline.
    * The simplest transformation of the training data that will move the needle on the metric measured by the validation set.
    * Helps to better understand the problem.
    * Helps remove bugs from the pipeline.
3. Next, work on the part of the pipeline that will benefit most from tweaking.
4. Invest time early in exploring a larger set of architectures and developing diagnostic code.
5. Move in small increments.
6. Consider constructing a smaller train set so you can test if you changes are having a positive impact more quickly.

## How to Win at Kaggle
1. Join a competition early.
    * Create a baseline.
2. Read the forums daily.
    * This will take you 80% of the way there.
    * It's the only way to keep up with developments.
    * Make posts about papers you think are relevant to the competition.
3. Make small improvements every day.
    * Focus on small teaks that will compound over the course of the competition.
    * Combine predictions form multiple models and in the hopes their errors are not correlated.
    * Cross-validation is used in most good Kaggle submissions.
4. Find a validation split that tracks the leader boards.
    * If you are doing similar things to others, you should be getting similar results.
    * If you changes in the leader board are not reflecting local changes, revisit you validation set.
5. Posts from top Kagglers will get you 80% of the way.
6. Use research papers, blog posts and creativity for the last 20%.
7. Ensemble results.

## The Best Hardware for Deep Learning
* A home rig is the most cost effective option.
    * Preferred set up is a laptop running Ubuntu Desktop and a headless desktop with a GPU running Ubuntu Server.
        * SSH into the desktops and access notebooks on a local network.
    * Ubuntu Server seems to be more stable and it's easier to install the CUD and CUDNN libraries.

**What GPU should you get?**
The biggest (most RAM) you can afford.

## On Finding a Job
Try and meet people who can influence hiring decisions where they hangout.

### Credibility
This is the name of the game in machine learning. You build credibility by being visible online, share your work and be helpful on forums.

## The Party is On Twitter
Twitter is where the deep learning community hangs out. Twitter is a great way to stay up to day with research and trends.
* Disable the algorithmic timeline and just use the following timeline.
* Disable notifications.

## Sharing Your Work
You should start sharing your work as soon as possible. You are in a unique position at any stage in your learning to be able to communicate concepts well to other people at your stage of understanding. Writing and reflecting also helps you to understand what you are doing on a deeper level.

### What to Focus On
Speak to your experience. This is one  fot he most valuable things you have to offer as others can see what you did an how as well as how you felt along the way and what results you achieved.

## Find a Mentor
A good mentor is someone very good at something you care about. A mentor doesn't even need to know you or even be aware that you exist.

### Permissionless Apprenticeship
[You receive value by giving value first.](https://twitter.com/jackbutcher/status/1261139777061113858?s=20)

Another way to attract the attention of like minded people is to [Learn in Public.](https://www.swyx.io/learn-in-public)

## The Regrets of fast.ai Students
Not spending enough time doing application. Aim to spend 80% of your time doing and 20% of your time learning content.

# Tap in to the Power of Community
Start asking question on the fast.ai forums. Overtime, you will start to see the value of these exchanges. [Insights from others.](https://radekosmulski.medium.com/how-to-use-the-power-of-the-community-to-learn-faster-564939882d62)

## Energize

**When and what you eat matters**
A good way to complete more mental work is to eat less. 

## Side Notes
* Learn to use your code editor really well.
* When working with Jupyter Notebooks, get in the habit of using %%timeit to see how long different cells take to execute.
    * This will give you unexpected insights into the efficiency of your pipeline.