---
layout: activity
title: "The Lighthouse"
image: src/19-lighthouse-with-a-switch/19.faro_.svg
video: src/videos/19_lighthouse.mp4
video_title: "What will we do?"
description: "Master the 'For' loop to create a beautiful, gradual flashing effect for a lighthouse that you can turn on and off."
lang: en
permalink: /en/activities/the-lighthouse/
ref: activity_lighthouse_with_a_switch

# ACTIVITY INFO
level: 2
computational_topics:
  - "Loops"
  - "Timing & Events"
  - "Variables & Data"
  - "Conditionals & Logic"
general_topics:
  - "Science & Technology"

tags: [Loops, For Loop, Nested Loops, Variables, Timing, Gradual Effect, Events]

introduction: |
  A simple flashing light is cool, but a real lighthouse has a gentle, gradual glow. How can we code that smooth fade-in and fade-out effect? In this mission, you'll learn to use the **'For' loop**—a powerful loop that is designed to run for a precise number of steps. Get ready to program a beautiful, pulsing lighthouse that gradually brightens and dims.

teacher: |
  ### **Courses**
  * Grades 6-12

  ### **Materials**
  * Cell phone, tablet, or computer
  * Internet connection

  ### **Educational Objectives**
  * Understand the concept of a FOR loop.
  * Create a technological object (prototype) using a device.
  * Identify relationships between technology and the surrounding world.
  * Evaluate personal and peer work.
  * Engage in dialogue and reflection on improvement ideas.

  ### **Start (10 minutes) - The Controlled Loop**
  1.  Welcome students and introduce the day’s activity: **"Today we will learn to prototype a lighthouse with a gradual, glowing light."**
  2.  Introduce the new programming tool for today. Ask the class: **"What if we need a loop that runs an exact number of times, like 100 steps to go from dim to bright?"**
  3.  Explain that while a 'forever' loop is great for endless automation, we sometimes need more control. This is where the **'For' loop** comes in. Break down its components for them: a counter variable, a start value, an end value, and a step size. This is the perfect tool for creating smooth, gradual animations.

  {{learn}}

  ### **Development (20-30 minutes) - Building the Glow**
  1.  Now that the students understand the mechanics of a 'For' loop, it's time to build the gradual glowing effect.
  2.  Lead them through **the instructions for creating the lighthouse prototype**, as detailed in the hands-on section below. Pay close attention to how they will use two 'For' loops: one to count up (fade in) and a second to count down (fade out).

  ### **Closure (5-10 minutes) - The Great Loop Debate**
  1.  Once everyone has a working lighthouse with a smooth pulse, it's time for a deeper dive into loop theory. This is a key conceptual moment.
  2.  Use the final section to guide a critical discussion comparing the 'For' loop with the 'While' loop they've seen before. Challenge them to rebuild this project with the "wrong" tool to see why programmers choose different loops for different jobs.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "The FOR Loop"
    type: "learn"
    icon: "book-reader"
    content: |
      A **‘count with variable’** loop, known in most programming languages as a **‘for’** loop, is designed to repeat a block of code a specific, known number of times. It uses a counter variable to keep track of its progress from a start point to an end point.
    media: "src/19-lighthouse-with-a-switch/a-what-is.svg"

  - title: "Components of the FOR loop"
    type: "learn"
    content: |
      Think of a **'For' loop** like a mission plan:
      1.  **Variable**: Your counter or "agent" that will be doing the counting (e.g., `i` or `intensity`).
      2.  **Initial value**: The starting number for your counter.
      3.  **Final value**: The target number where the loop will stop.
      4.  **Steps**: How much the counter changes in each repetition (e.g., counting up by 1, or down by 1).
    media: "[600]https://app.protobject.com/generate?contador&en&static&-1"

  - title: "How do we use it for a gradual glow?"
    type: "learn"
    content: |
      A **'for'** loop is perfect for animation because it runs for a known number of steps.
      To make our lighthouse light up gradually, we'll use a 'for' loop that counts an `intensity` variable from 0 to 100. In each step, we set the light's brightness to the current value of `intensity`. This creates a smooth fade-in.
      To make it dim, we'll use a second 'for' loop that counts `intensity` from 100 back down to 0!
    media: 
      - "src/19-lighthouse-with-a-switch/b-cycle.svg"
      - "src/19-lighthouse-with-a-switch/z.lighthoyuse-anim.svg"

  - id: "create"
    title: "Make the Lighthouse"
    type: "create"
    icon: "cogs"
    heading_text: "Let’s create the prototype that allows us to control the lighthouse."
    content: |
      We'll need 2 components: a lamp to be our light source, and a switch to turn the whole system on and off.
    steps:
      - "Press <addbutton>Add Device</addbutton>, select <comp>Lamp</comp>, and use <openwindow>Open in this Window</openwindow> or a smartphone."
      - "Press <addbutton>Add Device</addbutton> and select <comp>Switch</comp>."
    ready_message: "We are ready to start prototyping!"

  - title: "Code Composition"
    type: "code-composition"
    icon: "code"
    content: |
      Click on the question mark icon to open comments that explain the code.
    media: "[700]https://app.protobject.com/generate?a19-lighthouse&en&dynamic&-1"

  - id: "reflect"
    title: "Reflect: FOR vs. WHILE"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "You've now used different kinds of loops. Let's compare them."
    content: |
      * What is the main difference between a **'for' loop** (count with variable) and a **'while' loop** (repeat while)?
      * A 'for' loop is great when you know the exact start and end points (like 0 to 100). A 'while' loop is great when you just need to wait for a condition to change.
      * Are there cases where you could use either one? Absolutely!
    right_content:
      - text: |
          **Challenge**: Can you modify this project to work the same way but using **"repeat while"** blocks instead of "count with variable" blocks?
      - text: |
          **Hint**: You would need to create your own `intensity` variable, manually add or subtract 1 from it inside the loop, and make the loop run *while* `intensity` is less than 100 (or greater than 0).
---