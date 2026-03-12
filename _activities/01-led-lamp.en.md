---
layout: activity
title: "Light Up an LED"
image: src/01-led-lamp/01.lampara-led.svg
video: src/videos/01_led_lamp.mp4
video_title: "What will we do?"
description: "Take your very first step into the world of coding by learning the magic of block programming."
lang: en
permalink: /en/activities/light-up-an-led/
ref: activity_led_lamp

# ACTIVITY INFO
level: 1
computational_topics:
  - "Programming Fundamentals"
general_topics:
  - "Science & Technology"

tags: [Block Programming, First Activity, LED Lamp, Basic Commands]

introduction: |
  Ever wondered how your favorite games or apps work? It all starts with a single instruction. Get ready to send your very first command and bring a virtual LED lamp to life. In this mission, you'll discover the magic of **programming** by learning how to tell a device exactly what to do, using simple, visual **blocks**.
  
teacher: |
  ### **Courses**
  * Grades 3-12
  
  ### **Materials**
  * Cellphone, tablet, or computer
  * Internet connection
  
  ### **Description**
  In this activity, students can experiment in an introductory manner with Protobject, learning about visual programming and computer science safely and playfully using a device.
  
  ### **Educational Objectives**
  * Understand the concepts of "block programming" and "prototype."
  * Create a technological object (prototype) using a device.
  * Identify relationships between technology and the surrounding world.
  * Evaluate their own work and the work of others, both individually and in teams.
  * Participate in dialogues and reflections to propose improvements.
  
  ### **Start (10 minutes) - Sparking the Idea**
  1.  Welcome the class and introduce the activity: **"Today, we're going to learn how to prototype with Protobject and switch on our very first LED lamp."**
  2.  Spark their curiosity with a question: **"Do you know what programming is?"**
  3.  After a brief discussion to gather their thoughts, it's the perfect time to introduce the core concepts. Explain that programming is simply a way of giving super-specific instructions to a computer, and that we'll be using fun, visual blocks instead of complicated text. Let's explore these ideas together.

  {{learn}}

  ### **Development (20-30 minutes) - Building the Prototype**
  1.  Now that the key concepts are clear, it's time to get hands-on and bring that lamp to life! Prepare the students for the practical phase.
  2.  Ensure every student has a device ready and guide them through **the step-by-step process for creating their first prototype**, as detailed below.
  3.  **Note for the teacher:** Experiment with the activity before the class to anticipate any questions.

  ### **Closure (5-10 minutes) - Reflection and Final Challenge**
  1.  Fantastic work! Once the students have successfully lit up their lamps, it’s time to spark their curiosity further and reflect on what just happened.
  2.  Kick off the discussion with a simple question: **"Great job! You've turned it on, but how would you turn it *off*?"** Let them experiment with the **TURN OFF** block. This is a great moment to explain why it doesn't seem to work (due to the computer's execution speed) and to set the stage for the next adventure with timing. Use the following prompts to guide the conversation.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "What is Programming?"
    type: "learn"
    icon: "book-reader"
    content: |
      Programming is all about giving a computer a set of specific instructions to complete a task. This way, the computer knows exactly what to do by following the steps you laid out.
      Programmers use a special language that computers can understand. We call this a **programming language**, and it can be text-based or block-based.
    media: "src/01-led-lamp/a-programming.svg"

  - title: "Text vs. Blocks: Two Ways to Code"
    type: "learn"
    content: 
      - |
        **Textual programming** is like writing a recipe from scratch, using languages like Python, Java, or C++. It can be tricky for beginners.
      - |
        **Block-based programming**, on the other hand, is like building with LEGO® bricks. Each block is a pre-made piece of code that you can simply drag and snap together with others, no typing required.
        This is exactly the kind of programming we use in Protobject!
    media: ["src/01-led-lamp/b-text-programming.svg","src/01-led-lamp/c-block-programming.svg"]

  - title: "Welcome to Protobject!"
    type: "learn"
    content: |
      Protobject lets you program your smartphone and have it interact with the world around you.
      How? It's simple! You connect a device, build your code by dragging blocks into the workspace, and then activate your prototype!
    media: "src/01-led-lamp/d-introb-protobject.en.svg"

  - title: "Activate Your Prototype"
    type: "learn"
    content: |
      When your code blocks are ready, you can bring your prototype to life by pressing the **red button**.
      We are ready to start experimenting! Follow the instructions below and create your very first invention.
    media: "src/01-led-lamp/e-intro2b-protobject.en.svg"

  - id: "create"
    title: "Create"
    type: "create"
    icon: "cogs"
    heading_text: "Let’s make a lamp on our smartphone and turn it on with Protobject."
    ready_message: "Now we are ready to write the code."
    steps:
      - "Press <addbutton>Add device</addbutton> and select the component <comp>Lamp</comp>."
      - "Scan the <qr> code with your smartphone."
      - "Remember that if you don't have a smartphone to scan the **QR** codes, you can press <openwindow>Open in this window</openwindow> to open the components on the same computer."

  - title: "Drag the TURN ON block"
    type: "create"
    content: |
      Awesome! Let's power up our LED lamp!
      
      Each block represents an **action**. We’ll start by using just one block that will allow us to **turn on our LED lamp**.
      
      To do that, **drag the TURN ON block** to the workspace.
    content_class: "space-y-2"
    media: "src/01-led-lamp/f-intro3b-protobject.en.svg"

  - title: "Now activate the prototype!"
    type: "create"
    content: |
      Your **LED lamp** should **turn on**!
    content_class: "text-center text-xl"
    media: "src/01-led-lamp/g-intro4c-protobject.en.svg"

  - id: "reflect"
    title: "Reflect"
    type: "reflect"
    icon: "lightbulb"
    content: 
      - |
        You've mastered turning the lamp on. What's the next logical step? How would you turn it off?
      - |
        Have you tried adding the **TURN OFF** block right after the first one?
      
    media: ["src/01-led-lamp/h-light-on-to-off.svg", "https://app.protobject.com/generate?encenderApagar&en&static&-1"]
    right_content:
      - text: |
          **Think**: Have you considered the **speed** at which a computer follows instructions? It's so incredibly fast that the lamp turns on and off before your eyes can even notice! To control things like this, we'll need to learn how to manage time.

    
---