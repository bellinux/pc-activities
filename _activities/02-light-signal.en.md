---
layout: activity
title: "Create a Flashing Beacon"
image: src/02-light-signals/cover.svg
video: src/videos/02_beacon.mp4
video_title: "What will we do?"
description: "Discover how to control the speed of your code by programming a blinking light sequence."
lang: en
permalink: /en/activities/create-a-flashing-beacon/
ref: activity_light_signals

# ACTIVITY INFO
level: 1
computational_topics:
  - "Programming Fundamentals"
  - "Timing & Events"
general_topics:
  - "Science & Technology"

tags: [Timing, Delay Block, Sequencing, Light Signal, Blinking Effect]

introduction: |
  Ever seen the flashing lights on a tower or an emergency vehicle and wondered how they're controlled? That blinking isn't random—it's programmed with a sense of **time**. In this mission, you'll become the master of time, learning how to use **delays** to create your own flashing beacon from scratch.
  
teacher: |
  ### **Courses**
  * Grades 3-12

  ### **Materials**
  * Cellphone, tablet, or computer
  * Internet connection

  ### **Description**
  In this activity, students will learn the fundamental programming concept of "timing." They will use delay blocks to control the sequence of a virtual lamp, creating a classic blinking beacon effect and understanding why pauses are crucial in coding.

  ### **Educational Objectives**
  * Understand the concepts of "LED" and "timing".
  * Create a technological object (prototype) using a device.
  * Identify relationships between technology and the surrounding world.
  * Evaluate personal and others’ work in individual or team work.
  * Discuss and reflect on improvement ideas.

  ### **Start (10 minutes) - Introducing the Concept of Time**
  1.  Welcome the students and introduce the activity: **"Today we will learn how to prototype a beacon that flashes on and off."**
  2.  To spark the discussion, begin with a question: **"Do you know what makes your cellphone screen light up?"**
  3.  After they share their ideas, explain that the screen is made of tiny lights called LEDs. Then, pose a thought experiment: **"Imagine you write a program that tells a lamp to turn on, and on the very next line, you tell it to turn off. What do you think you'd actually see?"** Let them debate. The answer is... nothing! This is the perfect moment to explain that computers are incredibly fast and why we need to program pauses, introducing the concept of "Timing."

  {{learn}}

  ### **Development (20-30 minutes) - Building the Beacon**
  1.  With the theory of timing covered, it's time to put it into practice and build the flashing beacon.
  2.  Guide your students through **the instructions for connecting the device and coding the light sequence** detailed in the hands-on section below. Encourage them to experiment with different delay times to see how it affects the blinking speed.

  ### **Closure (5-10 minutes) - Reflection and Future Applications**
  1.  Excellent! Once everyone has a working beacon, transition into a final discussion to solidify their understanding and challenge them to think bigger.
  2.  Start the reflection by asking the key question from the activity: **"In what other situations could we use timing?"** Use the following prompts to guide a conversation about how timing is used in technology all around us.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "What is an LED?"
    type: "learn"
    icon: "book-reader"
    content: |
      Have you ever looked really closely at your TV or smartphone screen? It's made up of millions of tiny, powerful lights called **LEDs**.
      LEDs are everywhere around us, from the big ones that light up a room to the tiny ones that work together to create the images you see on a screen.
    media: "src/02-light-signals/a-examples1.svg"

  - title: "What about the cellphone screen?"
    type: "learn"
    content_class: "space-y-2 text-xl"
    content: |
      Your cellphone screen is packed with thousands of these tiny LEDs. When you watch a video or look at a photo, these are the lights that turn on and off to form the image.
      When we prototype with Protobject, these are the very LEDs we are controlling with our code!
    media: "src/02-light-signals/b-led-smartphone.svg"

  - title: "The Problem with Speed"
    type: "learn"
    content: |
      Here's a puzzle: imagine you tell your prototype to turn a lamp **ON**, and then in the very next instruction, you tell it to turn **OFF**. You'd expect to see a quick flash, right? But you'd actually see nothing!
      Why? **Machines are incredibly fast!** The lamp does turn on, but it turns off so quickly that our human eyes can't even perceive it.
    media: "src/02-light-signals/c-no-time.svg"
  
  - title: "Instructions Must Be Precise!"
    type: "learn"
    content: |
      Computers can't guess what we want. If our instructions are ambiguous, the program won't work as expected.
      In our flashing light puzzle, the missing piece was telling the computer **how long to wait** between turning the light on and turning it off. This action of pausing for a specific duration is called **Timing**.
    media: "src/02-light-signals/d-time.svg"

  - title: "What does 'timing' mean?"
    type: "learn"
    content: |
      To make a light flash like a beacon, we need to create a sequence that includes **wait times**, or delays, between the ON and OFF commands.
      In programming, we can measure time in different units. In Protobject, we can use **seconds** or **milliseconds** (1000 milliseconds = 1 second) to control our timing perfectly.
    media: "src/02-light-signals/e-sequence.svg"

  - id: "create"
    title: "Create a Beacon"
    type: "create"
    icon: "cogs"
    heading_text: "We’re going to create a prototype of a beacon."

    steps:
      - "Press <addbutton>Add device</addbutton> and select the <comp>Lamp</comp> component."
      - "Scan the <qr> code with your smartphone."
      - "If you don't have a smartphone, you can press <openwindow>Open in this window</openwindow> to open the lamp on the same computer."

  - title: "Where are the delay blocks located?"
    type: "create"
    content_class: "text-center text-xl"
    content: |
      First, let's find the blocks that control time. Open the <category>Timing</category> category.
    media: "src/02-light-signals/f-delay-a.en.svg"

  - title: "Code Composition"
    type: "code-composition"
    icon: "code"
    content: |
      Click on the question mark to open the comments that explain the code.
      
      *Remember*: the delay blocks are located in the <category>Timing</category> category.
    media: "[600]https://app.protobject.com/generate?a02-timing&en&dynamic&-1"

  - id: "reflect"
    title: "Reflect"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "You've learned how to control a beacon. Now, think bigger!"
    content: |
      * In what other real-world situations could you use timing and delays? Think about games, animations, or even tools you use every day.
    right_content:
      - text: |
          **Remember:** programming is all about creating a clear sequence of steps to achieve a goal.
          By adding delays, you made a simple light into a functional beacon!
---