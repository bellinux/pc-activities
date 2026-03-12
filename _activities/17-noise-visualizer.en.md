---
layout: activity
title: "The Noise Meter"
image: src/17-noise-visualizer/17.visualizador-ruido.svg
video: src/videos/17_noise_visualizer.mp4
video_title: "What will we do?"
description: "Learn the basics of drawing on a digital canvas by creating a line that grows and shrinks with the volume of surrounding noise."
lang: en
permalink: /en/activities/the-noise-meter/
ref: activity_noise_visualizer

# ACTIVITY INFO
level: 2
computational_topics:
  - "Graphics & Drawing"
  - "Sensors & Input"
  - "Loops"
general_topics:
  - "Mathematics & Logic"
  - "Art & Music"

tags: [Cartesian Plane, Drawing, Coordinates, Noise Sensor, Main Loop, Data Visualization]

introduction: |
  How can you turn sound into a picture? In this Level 2 mission, we're diving into the world of digital graphics! You'll learn how programmers use the **Cartesian Plane** (X and Y coordinates) to draw shapes and lines on a screen. Get ready to build a real-time noise visualizer that uses your microphone's input to control a dynamic, graphical display.
  
teacher: |
  ### **Courses**
  * Grades 6-12

  ### **Materials**
  * Cell phone, tablet, or computer
  * Internet connection

  ### **Educational Objectives**
  * Understand the concepts of the Cartesian plane and screen drawing.
  * Create a technological object (prototype) using a device.
  * Identify the relationships between technology and the surrounding world.
  * Evaluate their own work and that of others.
  * Engage in dialogue and reflect on ideas for improvement.

  ### **Start (10 minutes) - The Canvas is a Map**
  1.  Welcome students and introduce the day’s activity: **"Today we will learn how to prototype a noise visualizer, turning sound into graphics."**
  2.  Kick off the lesson with a question that connects to their math classes: **"Have you ever heard of the Cartesian plane in math? What is it used for?"**
  3.  Connect their answers to the world of programming. Explain that every screen—from their phone to a video game—is a grid. Programmers use X and Y coordinates to place every single visual element. Today, they'll become digital artists, using this system to draw a line whose length is controlled by sound.

  {{learn}}

  ### **Development (20-30 minutes) - Drawing with Data**
  1.  Now that the students understand the fundamentals of drawing on a coordinate plane, it's time to build their sound visualizer.
  2.  Lead them through **the instructions for creating the drawing canvas and programming the visualization logic**, as detailed in the hands-on section below. Pay close attention to the `draw line` block and how the noise level from the sensor is used to determine the line's length in real-time.

  ### **Closure (5-10 minutes) - The Digital Artist**
  1.  Once everyone has a working visualizer that reacts to their voice, it's time to reflect on the new graphical powers they've unlocked.
  2.  Use the final section to challenge their understanding of the coordinate system and to introduce a more complex visualization challenge that involves shapes and text.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "What is the Cartesian Plane?"
    type: "learn"
    icon: "book-reader"
    content: |
      Think of a screen not as a flat surface, but as a piece of graph paper. To tell the computer where to draw something, you need to give it an "address," just like a location on a map. This map is called the **Cartesian Plane**. It's a coordinate system composed of two perpendicular axes: the horizontal line is called the **X-axis**, and the vertical line is called the **Y-axis**. The point where they meet is the "origin" (0,0).
    media: "src/17-noise-visualizer/a-cartesian.svg"

  - title: "How do the X and Y axes work?"
    type: "learn"
    content: |
      The **X-axis** (horizontal) works just like a number line: smaller numbers are on the left, and larger numbers are on the right. The **Y-axis** (vertical) places smaller numbers at the bottom and larger ones at the top. By combining an X and a Y value, we can define the precise location of any point on the screen.
    media: 
      - "src/17-noise-visualizer/b-cartesianx.svg"
      - "src/17-noise-visualizer/c-cartesiany.svg"

  - title: "The First Quadrant"
    type: "learn"
    content: |
      The Cartesian plane is divided into four quadrants. In Protobject, to keep things simple, we primarily use the **first quadrant**, where both X and Y values are positive numbers. The origin point (0,0) corresponds to the bottom-left corner of our drawing canvas.
    media: "src/17-noise-visualizer/d-quadrants.svg"

  - title: "How to Draw a Line"
    type: "learn"
    content: |
      To draw a line, you just need to give the computer three instructions: a starting point (an X, Y coordinate), the direction to travel (an angle), and how far to go (a length).
      For a vertical bar, we'll start at the bottom of the screen, point straight up (a 90-degree angle), and make the length change based on the noise level!
    media: "src/17-noise-visualizer/f-drawlin.svg"

  - title: "Why visualize noise?"
    type: "learn"
    content: |
      Visualizing sound intensity isn't just for fun; it's useful! In loud environments like factories, a noise meter can help protect workers' hearing. In a classroom or library, it can be a great visual cue to help everyone be more aware of noise levels, creating a better environment for learning and focusing.
    media: 
      - "src/17-noise-visualizer/g-mechanical.svg"
      - "src/17-noise-visualizer/h-classrooml.svg"

  - id: "create"
    title: "Make the Noise Visualizer"
    type: "create"
    icon: "cogs"
    heading_text: "Let’s create the prototype that visualizes the noise level in real-time."
    content: |
      First, we need to add two components: one to (1) detect noise with the microphone and another to (2) act as our drawing canvas.
    steps:
      - "Press <addbutton>Add Device</addbutton>, select <comp>NoiseLevel</comp>, and scan the <qr> code with your smartphone."
      - "Click on <addbutton>Add Device</addbutton>, select <comp>WriteDraw</comp>, and press <openwindow>Open in this window</openwindow> to generate a drawing surface on the computer."
    ready_message: "We are ready to start prototyping!"

  - title: "Code Composition"
    type: "code-composition"
    icon: "code"
    content: |
      Click on the question mark icon to open comments explaining the code. Note that we have to clear the screen in every loop cycle to erase the old line before drawing the new one!
    media: "[600]https://app.protobject.com/generate?a17-noisevisualizer&en&dynamic&-1"

  - id: "reflect"
    title: "Reflect"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "You just drew with data! Now, let's get creative."
    content: |
      * Our code draws a vertical line. How would you change the parameters of the "draw line" block to make it a **horizontal** line instead?
      * Besides a line, what other ways could you visualize the noise? A circle that grows? A color that changes from green to red?
    right_content:
      - text: |
          **Challenge**: Let's create a noise visualizer for a classroom. We want it to show a circle that grows as the noise level increases. Additionally, if the noise level gets too high (exceeds a specific value), it should display the word **SILENCE!** on the screen.
      - text: |
          **Hint**: You can use the "draw a point at" block to draw the circle, and set its size based on the noise level. You'll need a conditional (IF block) to check the noise level and decide when to write the text.
    media: "src/videos/silent_challenge.mp4"
---