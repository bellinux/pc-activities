---
layout: activity
title: "The Anti-Theft Alarm"
image: src/08-anti-theft-alarm/08.alarma-antirobo.svg
video: src/videos/08_alarm.mp4
video_title: "What will we do?"
description: "Make your code smart! Use conditionals ('If-Then') to make decisions and build an alarm that reacts to movement."
lang: en
permalink: /en/activities/the-anti-theft-alarm/
ref: activity_anti_theft_alarm

# ACTIVITY INFO
level: 1
computational_topics:
  - "Conditionals & Logic"
  - "Loops"
  - "Sensors & Input"
general_topics:
  - "Everyday Life"

tags: [Conditionals, If-Then, Main Loop, Sensors, Motion Sensor, Camera]

introduction: |
  Let's teach our programs to see and react to the world! This mission introduces you to the power of **sensors** and **conditional logic**. You'll learn how to use a simple but powerful 'IF this happens, THEN do that' command to build a smart anti-theft alarm that triggers when it detects motion. Get ready to create your first intelligent system!

teacher: |
  ### **Courses**
  * Grades 3-12

  ### **Materials**
  * Cell phone, tablet, or computer
  * Internet connection

  ### **Educational Objectives**
  * Understand the concept of "IF-THEN" conditionals.
  * Create a technological object (prototype) using a device.
  * Identify relationships between technology and the surrounding world.
  * Evaluate personal work and the work of others.
  * Engage in discussions and reflect on improvement ideas.

  ### **Start (10 minutes) - The Logic of an Alarm**
  1.  Welcome students and introduce the day’s activity: **"Today, we will learn how to prototype a motion-detecting alarm."**
  2.  Ask the class: **"Have you ever seen an automatic door or a security light? How do you think they know you're there?"**
  3.  After discussing their ideas about sensors, explain that we'll use their phone's camera as a motion sensor. But how does a program *decide* when to sound the alarm? This is the perfect moment to introduce **conditional logic**—the 'IF/THEN' statement.
  4.  Finally, explain that the program needs to check for motion constantly, not just once, which requires a **Main Loop** to run the check over and over.

  {{learn}}

  ### **Development (20-30 minutes) - Building the Security System**
  1.  Now that they understand the logic of "IF motion is detected, THEN sound the alarm," it's time to build the security system.
  2.  Lead the students through **the instructions for adding the components and constructing the conditional code**, as detailed in the hands-on section below. Make sure they understand why the IF block must be placed inside the main loop to be effective.

  ### **Closure (5-10 minutes) - Security Debrief**
  1.  Once the alarms are working, it's time for a security expert's debrief. A real security expert always thinks about the weaknesses of their system.
  2.  Use the final section to guide a discussion about the limitations of their camera-based alarm. This encourages them to think critically about how technology works in the real world and how it could be improved.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Have you ever heard of motion sensors?"
    type: "learn"
    icon: "book-reader"
    content: |
      Motion sensors are smart devices that can detect when someone or something moves near them.
      
      Some, like those in automatic doors, work with **infrared** (a type of light we can't see) or **ultrasound** (a sound we can't hear). They sense changes when their signals bounce off a moving object.
    media: "src/08-anti-theft-alarm/a-movement-sensor.svg"

  - title: "Using a Camera as a Motion Sensor"
    type: "learn"
    content: |
      There are also motion sensors **based on cameras**, which is what we will use in this activity.
      A program can watch the video feed from a camera and detect **changes between frames**. If a large part of the image suddenly changes, the program knows that **something is moving**.
    media: "src/08-anti-theft-alarm/a-smartphone-camera.svg"

  - title: "IF There’s Motion, THEN Sound the Alarm"
    type: "learn"
    content: |
      To make our program smart, we need to teach it how to make decisions. The simplest way to do this is with a conditional statement: **IF a condition is true, THEN an action happens.**
      This "IF... THEN..." structure is a core building block of all programming, from simple games to complex artificial intelligence.
    media: "src/08-anti-theft-alarm/a-simple-condition.en.svg"
  
  - title: "A Practical Example"
    type: "learn"
    content: |
      Let’s see how to use a conditional to activate our alarm.
      We'll tell the program: **IF** the amount of motion detected by the camera is greater than a certain number (like 40), **THEN** play the alarm sound.
      But how do we make the program check for motion *continuously*? We can't just check once! This is where a **main loop** is essential. By placing our 'IF motion' check inside a 'repeat forever' loop, we create a system that is always watching.
    media: "src/08-anti-theft-alarm/a-mov-condition.en.svg"

  - id: "create"
    title: "Let's create our anti-theft alarm!"
    type: "create"
    icon: "cogs"
    heading_text: "Let’s build the prototype for our alarm."
    content: |
      First, we need to add two components: one to (1) detect motion and another to (2) play the alarm sound.
    steps:
      - "Add the component <comp>CameraMotion</comp> which detects motion through the phone's camera."
      - "Add the component <comp>AudioPlayer</comp> to play the sound of an alarm."
      - "Remember that if you don’t have a smartphone to scan the <qr> codes, you can click on <openwindow>Open in this window</openwindow>."
    right_content:
      - text: |
          **Suggestion**: In Protobject, you can add more components on the same smartphone by pressing the SCAN button as many times as you need.
      - media: "src/general-scan-button.svg"
    ready_message: "We are ready to start prototyping!"


  - title: "Code Composition"
    type: "code-composition"
    icon: "code"
    content: |
      Click on the question mark icon to open the comments that explain the code.
      Conditional blocks are found in the <category>Logic</category> category.
    media: "[700]https://app.protobject.com/generate?a08-alarm&en&dynamic&-1"

  - id: "reflect"
    title: "Reflect"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "You've built a security system. Now, think like a security expert."
    content: |
      * What would happen if a thief entered at night with all the lights off? Would a camera-based sensor still work?
      * How reliable is this alarm? What might accidentally trigger a false alarm (like a pet running by)?
    right_content:
      - text: |
          **Hint:** Thinking about a system's weaknesses is the first step to making it stronger. Our sensor relies on light and images to work!
---