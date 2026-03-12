---
layout: activity
title: "The Spirit Level: Is It Straight?"
image: src/15-tilt-sensor/15.sensor-inclinacion.svg
video: src/videos/15_tilt_sensor.mp4
video_title: "What will we do?"
description: "Use your phone's tilt sensor and advanced conditionals ('Else If') to build a tool that tells you if something is perfectly level."
lang: en
permalink: /en/activities/the-spirit-level-is-it-straight/
ref: activity_tilt_sensor

# ACTIVITY INFO
level: 1
computational_topics:
  - "Conditionals & Logic"
  - "Sensors & Input"
  - "Loops"
general_topics:
  - "Science & Technology"

tags: [Conditionals, Else If, Multi-Condition, Tilt Sensor, Accelerometer, Main Loop]

introduction: |
  Our programs can already make simple choices: IF this, THEN that, ELSE do something else. But life is usually more complicated than just two options! In this mission, you'll learn how to handle multiple conditions using the powerful **'ELSE IF'** command. Get ready to use your phone's motion-sensing **accelerometer** to build a digital spirit level that changes color based on how much it's tilted.

teacher: |
  ### **Courses**
  * Grades 3-12

  ### **Materials**
  * Cell phone, tablet, or computer
  * Internet connection

  ### **Educational Objectives**
  * Understand the concepts of “else if” (elif) and the “Cartesian plane.”
  * Create a technological object (prototype) using a device.
  * Identify relationships between technology and the surrounding world.
  * Evaluate personal and others’ work in individual or team tasks.
  * Engage in dialogue and reflection on improvement ideas.

  ### **Start (10 minutes) - Decisions with Many Paths**
  1.  Welcome students and introduce the day’s activity: **"Today, we will learn to prototype a digital tilt detector, just like a carpenter's spirit level."**
  2.  Start by briefly recapping the 'IF/ELSE' conditional for two options (like ON/OFF). Then, introduce a more complex problem: **"An IF/ELSE block is great for two choices. But what if you have *four* choices? For example, you want a program to suggest a meal based on the time of day."**
  3.  Use this analogy to show why we need more than just one 'ELSE'. This is the perfect setup to introduce the **'ELSE IF'** structure as a way to chain multiple checks together to make more complex decisions.

  {{learn}}

  ### **Development (20-30 minutes) - Building the Spirit Level**
  1.  Now that the students understand how to build a multi-path decision with 'ELSE IF', it's time to apply that logic to a real sensor.
  2.  Lead them through **the instructions for building the spirit level and programming the multi-conditional logic**, as detailed in the hands-on section below. Make sure they understand how each 'ELSE IF' block checks for a different range of tilt values, creating the different color warnings.

  ### **Closure (5-10 minutes) - Reflection on Sensors and Logic**
  1.  Once everyone's spirit level is changing colors correctly, it's time to reflect on the sensor and the powerful logic they've used.
  2.  Use the final section to guide a discussion about the accelerometer's other capabilities and to challenge them to create a new prototype combining tilt and sound.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "More Than Two Options?"
    type: "learn"
    icon: "book-reader"
    content: |
      You've seen how conditionals can work with two options: **IF** a condition is true, do something, **ELSE** do something different. This is perfect for a simple on/off switch.
      But what if you need to check for multiple, different conditions?
    media: "src/15-tilt-sensor/a-ifsimple.en.svg"

  - title: "Introducing 'Else If'"
    type: "learn"
    content: |
      The **“else if”** structure lets you chain multiple checks together in a single, neat block. You can think of it like a referee in a soccer match:
      * **IF** the foul is very serious, **THEN** show a red card.
      * **ELSE IF** the foul is just a warning, **THEN** show a yellow card.
      * **ELSE** (if neither of the above is true), **THEN** it’s just a simple foul.
      The program checks each condition in order until it finds one that is true.
    media: "src/15-tilt-sensor/multiple-if.en.svg"

  - title: "ELSE IF: 4 Options for our Spirit Level"
    type: "learn"
    content: |
      We'll use this multi-path logic to program a tilt detector that helps us hang pictures perfectly straight.
      The screen will light up with different colors based on the tilt value: green for level, yellow for slightly off, orange for more tilted, and red for very tilted.
    media: "src/15-tilt-sensor/y-multiple-inclination.svg"
  
  - title: "How does the phone detect tilt?"
    type: "learn"
    content: |
      To detect the tilt of a phone, we use a tiny built-in sensor called an **accelerometer**. This sensor can measure forces like gravity, telling the phone its orientation in space. It measures tilt on three different axes: X (left-right), Y (forward-backward), and Z (up-down). This allows the phone to know if it’s tilted to one side, standing upright, or lying flat.
    media: "src/15-tilt-sensor/z-accelerometer.svg"

  - id: "create"
    title: "Make the Tilt Sensor"
    type: "create"
    icon: "cogs"
    heading_text: "Let’s create a prototype that helps us detect if a picture frame is tilted."
    content: |
      First, we'll add two components: one to detect the phone's tilt and another to display the colored light.
    steps:
      - "Click on <addbutton>Add device</addbutton> and select <comp>Inclination</comp>."
      - "Click on <addbutton>Add device</addbutton> again and select <comp>Lamp</comp>."
      - "**Add both devices to the same smartphone for this project.**"
    ready_message: "We are ready to start prototyping!"

  - title: "Code Composition"
    type: "code-composition"
    icon: "code"
    content: |
      Click on the question mark icon to open the comments that explain the code.
      The "absolute" block (which makes a number positive) is located in the <category>Mathematics</category> category, inside the "square root" block's dropdown menu.
    media: "[700]https://app.protobject.com/generate?a15-inclination&en&dynamic&-1"

  - id: "reflect"
    title: "Reflect"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "You've built a program that can make complex decisions!"
    content: |
      This 'IF / ELSE IF / ELSE' chain is a super powerful tool.
      * Our spirit level used the Y-axis (forward-backward tilt). What do you think would happen if you changed the code to read the X-axis (left-right tilt) instead?
      * What other real-world tool or game could you build using your phone's tilt sensor?
    right_content:
      - text: |
          **Challenge**: Create a music player where you can adjust the volume by tilting your smartphone up and down.
      - text: |
          **Hint**: You'll need the <comp>AudioPlayer</comp> component. Inside your main loop, you can set the volume based on the value you get from the tilt sensor.
---