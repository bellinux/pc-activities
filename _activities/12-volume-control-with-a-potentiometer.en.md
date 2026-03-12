---
layout: activity
title: "The Volume Control"
image: src/12-volume-control-with-a-potentiometer/12.control-volumen.svg
video: src/videos/12_music_volume.mp4
video_title: "What will we do?"
description: "Learn to read continuous input from a virtual knob (potentiometer) to control the volume of a song in real-time."
lang: en
permalink: /en/activities/the-volume-control/
ref: activity_volume_control_with_a_potentiometer

# ACTIVITY INFO
level: 1
computational_topics:
  - "Sensors & Input"
  - "Loops"
general_topics:
  - "Art & Music"
  - "Science & Technology"

tags: [Analog Input, Potentiometer, Knob, Main Loop, Volume Control]

introduction: |
  So far, our buttons have been either ON or OFF. But what about all the controls in between? Think of a volume knob, a light dimmer, or a joystick. These require smooth, gradual control. In this mission, you'll explore the world of **analog input** by programming a virtual knob, also known as a **potentiometer**. Get ready to learn how to read a continuously changing value to control your project's volume in real-time.

teacher: |
  ### **Courses**
  * Grades 3-12

  ### **Materials**
  * Cellphone, tablet, or computer
  * Internet connection

  ### **Educational Objectives**
  * Understand the concept of a potentiometer.
  * Create a technological object (prototype) using a device.
  * Identify relationships between technology and the surrounding world.
  * Evaluate personal work and the work of others.
  * Engage in dialogue and reflection on improvement ideas.

  ### **Start (10 minutes) - Beyond On and Off**
  1.  Welcome students and introduce the day’s activity: **"Today, we are going to learn how to create a volume knob that gives us smooth, gradual control."**
  2.  Ask a guiding question: **"Think about a volume knob on a stereo or a dimmer switch for a light. How is it different from a simple on/off button?"**
  3.  Guide the discussion to the idea of 'gradual' or 'in-between' values. Explain that this is called **analog control**, and the component that allows us to do this is a potentiometer. Let's dive into how it works and how we can program it.

  {{learn}}

  ### **Development (20-30 minutes) - Building the Volume Controller**
  1.  Now that the students understand the concept of a potentiometer and how to read its value, it's time to build a real-time volume controller.
  2.  Lead them through **the instructions for connecting the components and programming the volume control logic**, as detailed in the hands-on section below. Encourage them to see how the knob's value directly affects the audio player's volume as they turn it.

  ### **Closure (5-10 minutes) - The World of Analog**
  1.  Once everyone has a working volume knob, it's time to brainstorm other uses for this powerful analog input.
  2.  Use the final section to spark a creative discussion about other things that can be controlled gradually and to challenge them to visualize the data from their new sensor.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "What is a potentiometer?"
    type: "learn"
    icon: "book-reader"
    content: |
      Have you ever adjusted the volume of a radio? Or changed the brightness of a lamp using a dimmer? If so, you’ve probably used a potentiometer.
      It's the technology behind any control that isn't just on or off, but allows for a smooth range of values in between. Usually, you control it with a **knob**!
    media: "src/12-volume-control-with-a-potentiometer/a.main-knob.svg"

  - title: "How does it work?"
    type: "learn"
    content: |
      A potentiometer works by changing its electrical resistance as you turn it. Think of it like a faucet for electricity. By turning the knob, you can **gradually** change how much electrical current flows through it.
      In the case of a speaker, adjusting the current allows you to smoothly **increase or decrease the volume**.
    media: "src/12-volume-control-with-a-potentiometer/b.knob-music-anim.svg"

  - title: "How do we program it?"
    type: "learn"
    content: |
      To make our volume knob work, our program needs to know its current position. We have two great ways to do this:
      * **The Main Loop:** We can put our code inside a "repeat forever" loop. The program will constantly check the knob's value and update the volume, over and over.
      * **Events:** A more efficient way! We can use an event that triggers *only when the knob is turned*. The program waits quietly until it gets a signal, then updates the volume.
      In programming, there are often different solutions to the same problem!
    media: "src/12-volume-control-with-a-potentiometer/c.loop-or-event.en.svg"

  - id: "create"
    title: "Let's get to work!"
    type: "create"
    icon: "cogs"
    heading_text: "We are going to create a prototype that lets us control a song's volume with a potentiometer."
    content: |
      First, we'll add two components: one to (1) play the music and a second to (2) act as our control knob.
    steps:
      - "Press <addbutton>Add Device</addbutton> and select <comp>Knob</comp>."
      - "Press <addbutton>Add Device</addbutton> again and select <comp>AudioPlayer</comp>."
      - "Remember that if you don’t have a smartphone to scan the <qr> codes, you can press <openwindow>Open in this window</openwindow>."
    right_content:
      - text: |
          **Suggestion**: In Protobject, you can add more components on the same smartphone by pressing the *SCAN* button as many times as you need.
      - media: "src/general-scan-button.svg"
    ready_message: "We're ready to start prototyping!"

  - title: "Code Composition"
    type: "code-composition"
    icon: "code"
    content: |
      Click on the question mark icon to open the comments that explain the code.
      **Remember**: You can build this using a **main loop** or, for a more efficient approach, use the **event** that triggers **when the knob is turned**.
    media: "[700]https://app.protobject.com/generate?a12-knobvolume&en&dynamic&-1"

  - id: "reflect"
    title: "Reflect"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "You've just unlocked the power of analog control!"
    content: |
      Simple ON/OFF is fine, but gradual control opens up a whole new world of possibilities.
      *What other things in a game or an app would you want to control smoothly with a knob or slider? (Think character speed, screen brightness, or the brush size in a drawing app).*
    right_content:
      - text: |
          **Challenge**: Let’s create a visualizer that shows the current volume as a number on the screen.
      - text: |
          **Hint**: You'll need the <comp>WriteDraw</comp> component. Inside your loop or event, how can you take the value from the knob and tell the WriteDraw component to display it as text?
---