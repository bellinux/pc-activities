---
layout: activity
title: "Create a People Counter"
image: src/11-manual-people-counter/11.contador-personas.svg
video: src/videos/11_people_counter.mp4
video_title: "What will we do?"
description: "Use events and variables to build a practical tool for counting people, just like at a real concert or store."
lang: en
permalink: /en/activities/create-a-people-counter/
ref: activity_manual_people_counter

# ACTIVITY INFO
level: 1
computational_topics:
  - "Timing & Events"
  - "Variables & Data"
  - "Conditionals & Logic"
general_topics:
  - "Mathematics & Logic"

tags: [Events, Variables, Counter, User Input, Data]

introduction: |
  Ever been to a big event or a busy store and seen someone at the door with a clicker, counting everyone who enters? Let's build a digital version of that! In this mission, you'll combine two of the most powerful concepts in programming—**events** and **variables**—to create a practical people counter. Get ready to build a real tool that listens for input and tracks data.

teacher: |
  ### **Courses**
  * Grades 3-12

  ### **Materials**
  * Cell phone, tablet, or computer
  * Internet connection

  ### **Educational Objectives**
  * Understand the concepts of "event" and "numeric data."
  * Create a technological object (prototype) using a device.
  * Identify relationships between technology and the world around them.
  * Evaluate personal and others’ work.
  * Engage in discussions and reflect on improvement ideas.

  ### **Start (10 minutes) - The Logic of a Counter**
  1.  Welcome students and introduce the day’s activity: **"Today, we are going to learn how to prototype a digital people counter."**
  2.  Ask the class: **"What is a counting device, and where have you seen one being used?"** (e.g., stores, concerts, transportation).
  3.  After discussing its real-world uses, explain the logic behind it. We need a place to 'store' the current count, and a way to 'know' when to add one more person. This is the perfect scenario to show how **variables** (for storing data) and **events** (for triggering actions) work together to create a useful tool.

  {{learn}}

  ### **Development (20-30 minutes) - Building the Device**
  1.  Now that the students understand the logic of using a variable as a counter and an event as the trigger, it's time to build the device.
  2.  Lead them through **the instructions for creating the user interface and programming the counting logic**, as detailed in the hands-on section below. This project is a fantastic real-world application of the concepts they've learned.

  ### **Closure (5-10 minutes) - Reflection and Upgrades**
  1.  Once everyone has a working counter, it's time for a critical thinking exercise. Is an event the *only* way to build this? And how can we make it even more useful?
  2.  Use the final sections to guide a discussion comparing the efficiency of events versus loops, and then challenge them to upgrade their counter with an important new feature: subtraction.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "What is a counting device?"
    type: "learn"
    icon: "book-reader"
    content: |
      A counting device, or "clicker," is a simple tool used to **keep track of a quantity**. It could be used to count products in a warehouse, laps in a race, or in our case, people entering a venue.
      Each time someone enters, you **press a button**, and the **counter on the display increases by one**. It's a simple and effective way to keep an accurate count.
    media: "src/11-manual-people-counter/a.lcd-counter.svg"

  - title: "What is the purpose of a people counter?"
    type: "learn"
    content: |
      People counters are surprisingly useful in many situations. Stores use them to track customer flow, event organizers use them to control venue capacity for safety, and public transport can use the data to improve service. It's a simple tool that helps make systems safer and more efficient.
    media:
      - "src/11-manual-people-counter/b.shop_.example.svg"
      - "src/11-manual-people-counter/b.event_.example.svg"
      - "src/11-manual-people-counter/b.bus_.example.svg"

  - title: "We use a variable to keep track"
    type: "learn"
    content: |
      Remember **variables**? They're like labeled boxes for storing information. For our people counter, a variable is the perfect tool to act as our digital scoreboard. We will create a variable to store the current count, and we can update the value inside it whenever a new person enters.
    media: "src/11-manual-people-counter/c.variable-use.en.svg"

  - title: "And how do we know when to count?"
    type: "learn"
    content: |
      How do we know *when* to update our variable? We use an **event**!
      Instead of constantly asking "Is the button pressed?", the program just listens. When you press the button, it sends a signal—an event—to our code. That event is the trigger that tells our program: 'Okay, time to add 1 to the counter variable!' It's an efficient and smart way to program.
    media: "src/11-manual-people-counter/evento-icon.en.svg"

  - id: "create"
    title: "Let's build the counter"
    type: "create"
    icon: "cogs"
    heading_text: "We are going to create a prototype that allows us to count people entering a place."
    content: |
      First, we need to add two components: one to (1) display the number of people and a second to (2) act as our "add" button.
    steps:
      - "Press <addbutton>Add device</addbutton> and select <comp>WriteDraw</comp>, the device where we will display the number."
      - "Press <addbutton>Add device</addbutton> again and select <comp>TouchButton</comp> to create the button."
      - "Remember that if you don’t have a smartphone, you can press <openwindow>Open in this window</openwindow>."
    ready_message: "We are ready to start prototyping!"

  - title: "Code Composition"
    type: "code-composition"
    icon: "code"
    content: |
      Click on the question mark icon to open the comments that explain the code.
    media: "[700]https://app.protobject.com/generate?a11-peoplecounter&en&dynamic&-1"

  - id: "reflect"
    title: "Reflect"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "What if we used a main loop instead of an event?"
    content: |
      You built this counter using an event, which is super efficient. But could you build it with a main loop? Take a look at the code below. What's the main difference? What do you think would happen if you held the button down in the loop version versus the event version?
    media: "[450]https://app.protobject.com/generate?contarpersonaswhile&en&dynamic&-1"

  - title: "Challenge"
    icon: "trophy"
    type: "reflect"
    heading_text: "Your counter can only go up. But what happens if people leave?"
    content: |
      A real counter needs a way to subtract! Your challenge is to add a second button to your prototype that **decreases** the count by one every time it's pressed.
    media: "src/videos/counter_challenge.mp4"
    right_content:
      - text: |
          **Hint:** You'll need to add a second <comp>TouchButton</comp> component. How would you program a *second* event to handle subtraction?
---