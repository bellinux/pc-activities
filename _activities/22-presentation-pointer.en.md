---
layout: activity
title: "The Digital Pointer"
image: src/22-presentation-pointer/22.puntero-presentaciones.svg
video: src/videos/22_laser_pointer.mp4
video_title: "What will we do?"
description: "Combine your phone's accelerometer, gyroscope, and magnetometer to create a pointer you can control with motion."
lang: en
permalink: /en/activities/the-digital-pointer/
ref: activity_presentation_pointer

# ACTIVITY INFO
level: 3
computational_topics:
  - "Sensors & Input"
  - "Graphics & Drawing"
  - "Loops"
general_topics:
  - "Science & Technology"

tags: [Sensor Fusion, Accelerometer, Gyroscope, Magnetometer, Events, Main Loop, Drawing, Coordinates]

introduction: |
  How does your phone know to rotate the screen when you turn it sideways? Or how does a VR headset track your every move? The secret is a powerful technique called **Sensor Fusion**. In this advanced Level 3 mission, you'll learn how your phone combines its accelerometer, gyroscope, and magnetometer to pinpoint its exact orientation in 3D space. Get ready to harness this data to build a motion-controlled digital pointer, just like a high-tech laser pointer!
teacher: |
  ### **Courses**
  * Grades 9-12

  ### **Materials**
  * Cell phone, tablet, or computer
  * Internet connection

  ### **Educational Objectives**
  * Understand what phone motion sensors are and how they work together (Sensor Fusion).
  * Be able to position elements on a Cartesian plane.
  * Understand the concept of a computable function.
  * Evaluate personal and others’ work.
  * Engage in dialogue and reflection on ideas for improvement.

  ### **Start (10 minutes) - The Phone's Sixth Sense**
  1.  Introduce the activity: **"Today we will learn how to prototype a motion-controlled presentation pointer, using some of the most advanced sensors in your phone."**
  2.  Kick off this advanced lesson with an intriguing question: **"Your phone is just a block of glass and metal. How does it know which way is up, down, left, and right in the real world?"**
  3.  Explain that it's not one, but a team of sensors working together. Briefly introduce the three key players: the accelerometer (for movement), the gyroscope (for rotation), and the magnetometer (like a compass). Then, introduce the main concept: **Sensor Fusion**, the process of combining all this data to get one super-accurate result.

  {{learn}}

  ### **Development (20-30 minutes) - Programming with Fused Data**
  1.  Now that the students have a conceptual understanding of Sensor Fusion, it's time to use that fused data to control an object on the screen.
  2.  Lead them through **the instructions for creating the pointer and programming the motion control logic**, as detailed in the hands-on section below. This is a complex build, so pay close attention to how the sensor's X and Y outputs are used to update the pointer's coordinates.

  ### **Closure (5-10 minutes) - The Sensor Team**
  1.  Once everyone has their motion-controlled pointer working, it's time to reflect on the advanced technology they've just implemented.
  2.  Use the final section to guide a discussion that reinforces their understanding of the different sensors and their roles, and to challenge them with a multiplayer version of the project.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "How does the phone know its orientation?"
    type: "learn"
    icon: "book-reader"
    content: |
      Imagine you're in a dark, empty room with your eyes blindfolded. You could probably still point 'up' and 'down' because you can feel gravity. Your phone does something similar, but it's much more advanced. To know its exact orientation in 3D space, it uses a team of specialized sensors.
    media: "src/22-presentation-pointer/a-orientation.svg"

  - title: "Meet the Sensor Team"
    type: "learn"
    content: |
      Your phone's sense of direction comes from three main specialists:
      * **Accelerometer**: The 'Motion Detector.' It feels linear acceleration—moving forward/backward, left/right, and up/down.
      * **Gyroscope**: The 'Rotation Specialist.' It detects twists and turns, measuring changes in the phone's angle.
      * **Magnetometer**: The 'Navigator.' It's a digital compass that detects magnetic fields, always knowing which way is North.
    media: 
      - "src/22-presentation-pointer/z-accelerometer.svg"
      - "src/22-presentation-pointer/b-gyroscope-orientation.svg"
      - "src/22-presentation-pointer/c-magnetometer.svg"

  - title: "Working Together: Sensor Fusion"
    type: "learn"
    content: |
      None of these sensors is perfect on its own. The accelerometer can be jittery, and the gyroscope can 'drift' over time. But when they work together, their strengths cover for each other's weaknesses. This collaboration is called **Sensor Fusion**. The phone's software intelligently 'fuses' the data from all three sensors to get a single, highly accurate reading of its orientation. It's the ultimate teamwork!
    media: "src/22-presentation-pointer/d-fusion.en.svg"
  
  - title: "From Fusion to Coordinates"
    type: "learn"
    content: |
      The result of Sensor Fusion is a stream of numerical data. Our job as programmers is to give that data meaning. When we move the phone, the values for the X and Y axes of rotation change. By reading these values, we can map the phone's physical movement to the X and Y coordinates of a pointer on our digital canvas.
    media: "src/22-presentation-pointer/e-coordenates.svg"

  - id: "create"
    title: "Make the Presentation Pointer"
    type: "create"
    icon: "cogs"
    heading_text: "Let’s create the prototype: we will need a smartphone and a computer/tablet."
    steps:
      - "On the same smartphone, add the <comp>Direction</comp> and <comp>TouchButton</comp> components."
      - "Add the <comp>WriteDraw</comp> device by opening it on your computer/tablet by clicking <openwindow>Open in this window</openwindow>."
    ready_message: "We are ready to start prototyping!"

  - title: "Code Composition"
    type: "code-composition"
    icon: "code"
    content: |
      Click on the question mark icon to open the comments that explain the code.
    media: "[600]https://app.protobject.com/generate?a22-pointermap&en&dynamic&-1"

  - id: "reflect"
    title: "Reflect"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "You've just harnessed an advanced smartphone feature! Let's review the sensor team:"
    content: |
      * Which sensor acts like a compass, detecting magnetic north?
      * Which sensor is best at detecting tilting and spinning?
      * What is the purpose of the 'reset' button in this project? What happens if you don't use it?
    right_content:
      - text: |
          **Challenge**: Let’s program two pointers simultaneously so that two people can independently point to different areas on the screen with their own phones!
---