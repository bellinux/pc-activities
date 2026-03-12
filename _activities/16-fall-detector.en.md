---
layout: activity
title: "Build a Fall Detector"
image: src/16-fall-detector/16.detector-caida.svg
video: src/videos/16_fall_detector.mp4
video_title: "What will we do?"
description: "Learn how to measure total acceleration with your phone's motion sensor to create a system that can detect a sudden fall."
lang: en
permalink: /en/activities/build-a-fall-detector/
ref: activity_fall_detector

# ACTIVITY INFO
level: 1
computational_topics:
  - "Sensors & Input"
  - "Conditionals & Logic"
  - "Loops"
general_topics:
  - "Everyday Life"

tags: [Accelerometer, Sensors, Absolute Value, Main Loop, Conditionals, Health, Safety]

introduction: |
  Did you know your phone can sense when it's falling? Its built-in **accelerometer** is so sensitive it can detect sudden changes in motion. By adding up the data from all three axes of movement (X, Y, and Z), we can measure the total force of an impact. In this mission, you'll harness that power to build a real fall detector that sounds an alarm when it senses a sharp, sudden jolt.
  
teacher: |
  ### **Courses**
  * Grades 3-12

  ### **Materials**
  * Cell phone, tablet, or computer
  * Internet connection

  ### **Educational Objectives**
  * Understand the concepts of “if-else” and the “Cartesian plane.”
  * Create a technological object (prototype) using a device.
  * Identify relationships between technology and the surrounding world.
  * Evaluate personal and others’ work.
  * Engage in dialogue and reflection on improvement ideas.

  ### **Start (10 minutes) - The Physics of a Fall**
  1.  Welcome students and introduce the day’s activity: **"Today we will learn to prototype a ‘fall detector’ with our phones."**
  2.  Start by asking the class: **"How do smartwatches or phones sometimes know if a person has had a fall?"** Guide the discussion toward the idea of detecting sudden motion.
  3.  Explain that the phone's **accelerometer** is the key. Introduce the core challenge: a fall can happen in any direction, so how can our program detect the overall *magnitude* of the motion? This leads perfectly into the concept of combining the X, Y, and Z axes to get a total motion value.

  {{learn}}

  ### **Development (20-30 minutes) - Building the Detector**
  1.  Now that the students understand the logic of measuring total motion, it's time to build the fall detector.
  2.  Lead them through **the instructions for creating the prototype and programming the detection logic**, as detailed in the hands-on section below. Emphasize how the 'IF' statement is used to check if the total motion exceeds a certain threshold.
  3.  Have students test their prototypes by carefully but quickly shaking the device, or by dropping it a very short distance onto a soft surface like a book or pillow.

  ### **Closure (5-10 minutes) - Real-World Reliability**
  1.  Once the fall detectors are working, it's time to think about the real-world implications and challenges of such a device.
  2.  Use the final section to guide a critical discussion about the reliability of their fall detector. This encourages them to think like engineers about false positives and improving their designs.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "How does the phone detect a fall?"
    type: "learn"
    icon: "book-reader"
    content: |
      Your phone's **accelerometer** is a powerful motion sensor. It constantly measures acceleration in three directions or "axes": left-right (X-axis), forward-backward (Y-axis), and up-down (Z-axis).
      When a phone is dropped, it experiences a sharp, sudden change in acceleration. To detect a fall, we don't care about the *direction* of the fall, only that it was a powerful jolt. To measure this total jolt, we can take the **absolute value** (the positive version of the number) of the motion on each axis and add them together. This gives us a single number representing the total magnitude of the motion.
    media: "src/16-fall-detector/z-accelerometer.svg"

  - title: "Let's get to work!"
    type: "learn"
    content: |
      Protobject simplifies this process for us with the `generalMotion` variable. This special variable automatically does the math for us: it sums the absolute values of the X, Y, and Z axes in real-time.
      All we need to do is set a threshold. We'll tell our program: **IF** the `generalMotion` value exceeds a certain number (like 150), it means a sharp jolt has occurred, and we should trigger an alarm sound.
    media: "src/a.working.svg"

  - id: "create"
    title: "Make the Fall Detector"
    type: "create"
    icon: "cogs"
    heading_text: "Let’s create a prototype to detect falls."
    content: |
      First, we need to add two components: one to (1) detect the smartphone's movements and another to (2) play sounds.
    steps:
      - "Press <addbutton>Add device</addbutton> and select <comp>Motion</comp>."
      - "Click on <addbutton>Add device</addbutton> again and select <comp>AudioPlayer</comp>."
    right_content:
      - text: |
          **Tip**: In Protobject, you can add more components on the same smartphone by pressing the *SCAN* button as many times as you need.
      - media: "src/general-scan-button.svg"
    ready_message: "We are ready to start prototyping!"

  - title: "Code Composition"
    type: "code-composition"
    icon: "code"
    content: |
      Click on the question mark icon to open the comments that explain the code.
      
      **Note:** This code uses the `generalMotion` variable. As an extra challenge, try modifying the code to do the math manually by adding the absolute values of the X, Y, and Z axes yourself!
    media: "[700]https://app.protobject.com/generate?a16-falldetector&en&dynamic&-1"

  - id: "reflect"
    title: "Reflect"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "You've built a device with real-world applications. Now, let's think like engineers."
    content: |
      * How reliable do you think this fall detector is? Could a false alarm be triggered just by running, jumping, or putting the phone down too hard?
      * Would you trust this to be used in a real-life situation for an elderly person? What improvements would you need to make first?
    right_content:
      - text: |
          **Challenge**: Create a light that changes colors based on the phone’s accelerations.
      - text: |
          **Hint**: You can feed the values from the three different axes of the accelerometer (X, Y, and Z) into the three primary color channels (Red, Green, and Blue) of a lamp. Use an event to detect changes in the accelerometer.
---