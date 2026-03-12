---
layout: activity
title: "The Traffic Light"
image: src/05-creating-a-traffic-light/05.semaforo.svg
video: src/videos/05_traffic_light.mp4
video_title: "What will we do?"
description: "Say goodbye to repetitive code! Learn how to use infinite loops to automate a classic traffic light sequence."
lang: en
permalink: /en/activities/the-traffic-light/
ref: activity_create_a_traffic_light

# ACTIVITY INFO
level: 1
computational_topics:
  - "Loops"
  - "Timing & Events"
general_topics:
  - "Everyday Life"

tags: [Loops, Main Loop, Repeat Forever, Automation, Timing, Traffic Light]

introduction: |
  How do you make a program run on its own, forever? If you had to code a traffic light for a whole day by copying and pasting commands, your program would be millions of lines long! In this mission, you'll learn the programmer's secret to automation: the infinite **loop**. Get ready to build a smart, fully automated traffic light that never stops.
  

teacher: |
  ### **Courses**
  * Grades 3-12

  ### **Materials**
  * Cell phone, tablet, or computer
  * Internet connection

  ### **Educational Objectives**
  * Understand the concept of "repeat forever" (Main Loop).
  * Create a technological object (prototype) using a device.
  * Identify relationships between technology and the surrounding environment.
  * Evaluate their own and others’ work, both individually and in a team.
  * Engage in dialogues and reflections to propose improvements.

  ### **Start (10 minutes) - The Problem of Repetition**
  1.  Welcome students and introduce the day’s activity: **"Today, we are going to learn how to prototype an automated traffic light."**
  2.  Start by revisiting the concept of a sequence. Ask the class: **"We know how to turn a light on for a few seconds. But how would we create a sequence, like a green light, then a yellow, then a red?"**
  3.  After they brainstorm, introduce the bigger challenge: **"Okay, but what if we need that traffic light to run for a whole hour, or all day? Copying and pasting that sequence hundreds of times would be impossible!"** This sets up the perfect problem for which loops are the solution.

  {{learn}}

  ### **Development (20-30 minutes) - Building the Automated System**
  1.  Now that the students understand the power of loops for automation, it's time to build the traffic light.
  2.  Lead them through **the instructions for creating the light sequence and placing it inside the infinite loop**, as detailed in the hands-on section below. This is their first taste of creating a program that runs on its own.

  ### **Closure (5-10 minutes) - From Code to the Real World**
  1.  Once everyone's traffic light is running continuously, it's time to connect their digital creation to the world around them.
  2.  Use the final section to spark a discussion about how traffic lights function in our cities and why they are so important for safety and order. This helps them see the real-world application of the coding concepts they've just learned.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "What can we do with an LED lamp?"
    type: "learn"
    icon: "book-reader"
    content: |
      If we program an LED lamp to change from green, to yellow, and then to red in a timed sequence... we've created a traffic light!
      To do this, we just need to program the right **timing** and the right **colors**.
    media: "src/05-creating-a-traffic-light/a.trafficlight.svg"

  - title: "The Problem: The Code Stops!"
    type: "learn"
    content: |
      If you just code one cycle—green, yellow, red—the program will run it once and then stop. To make it repeat, you could copy and paste the blocks over and over again.
      But what if you wanted the traffic light to run for an hour? **You'd end up with an enormous amount of repeated code!** That's inefficient and impossible to manage.
    media: "src/05-creating-a-traffic-light/a.trafficlight-seq.svg"

  - title: "The Solution: The 'Repeat Forever' Loop"
    type: "learn"
    content: |
      ### How do we make it repeat on its own? We use a loop!

      The **"repeat forever"** block is a fundamental tool in programming. This concept, also known as the **Main Loop**, tells the computer to repeat all the code inside it over and over again, until the user manually stops the program.
      By placing our traffic light sequence inside this loop, we can keep it running indefinitely!
    media: "src/05-creating-a-traffic-light/a.trafficlight-seq2.en.svg"
  
  - title: "Let's get to work!"
    type: "learn"
    content: |
      We are going to create our traffic light prototype by placing the color and timing code inside the **“repeat forever”** loop. We'll program the light to be green for 6 seconds, yellow for 1 second, and red for 6 seconds, creating a realistic cycle.
    media: "src/a.working.svg"

  - id: "create"
    title: "Make our Traffic Light!"
    type: "create"
    icon: "cogs"
    heading_text: "Let’s build our traffic light!"
    steps:
      - "Press <addbutton>Add Device</addbutton> and select <comp>Lamp</comp>."
      - "Scan the <qr> code."
      - "Remember that if you don’t have a smartphone, you can press <openwindow>Open in this window</openwindow> to open the components on the same computer."
    ready_message: "We are ready to start prototyping!"

  - title: "Code Composition"
    type: "code-composition"
    icon: "code"
    content: |
      Click on the question mark icon to open the comments that explain the code.

      The "repeat forever" block is located in the <category>Basic</category> category.
    media: "[700]https://app.protobject.com/generate?a05-trafficlight&en&dynamic&-1"

  - id: "reflect"
    title: "Reflect"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "You've built a working traffic light! Now, let's think about the real world."
    content: |
      * How do real traffic lights work? Are they all alone, or do they work in teams?
      * How many traffic lights are usually needed to control a single intersection?
      * What is the most important purpose of a traffic light in our communities?
---