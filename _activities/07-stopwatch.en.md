---
layout: activity
title: "Build Your Own Stopwatch"
image: src/07-stopwatch/stopwatch-cover.svg
video: src/videos/07_stopwatch.mp4
video_title: "What will we do?"
description: "Master the use of variables and loops to build a functional stopwatch that counts seconds on the screen."
lang: en
permalink: /en/activities/build-your-own-stopwatch/
ref: activity_stopwatch

# ACTIVITY INFO
level: 1
computational_topics:
  - "Loops"
  - "Variables & Data"
  - "Timing & Events"
general_topics:
  - "Mathematics & Logic"

tags: [Variables, Counter, Loops, Main Loop, Timing, Stopwatch]

introduction: |
  Ever wondered how a game keeps score or a clock counts the seconds? It's all about remembering and updating a number. In this mission, you'll unlock that secret by combining **loops** and **variables** to build a fully functional stopwatch. Get ready to learn how to make your program count, remember, and display information that changes over time.

teacher: |
  ### **Courses**
  * Grades 3 to 12
  
  ### **Materials**
  * Mobile phone, tablet, or computer
  * Internet connection
  
  ### **Description**
  In this activity, students will combine loops and variables to create a practical application: a stopwatch. They will learn how to initialize, increment, and display a variable's value over time, reinforcing these core computer science concepts.
  
  ### **Educational Objectives**
  * Understand the concept of a variable as a counter.
  * Create a technological object (prototype) using a device.
  * Identify relationships between technology and the environment.
  * Evaluate one's own work and that of others.
  * Participate in discussions and reflections to propose improvements.
  
  ### **Start (10 minutes) - The Challenge of Counting**
  1.  Welcome the class and introduce the activity: **"Today we will learn how to build a stopwatch that counts seconds from scratch."**
  2.  Spark curiosity with a question: **"How do you think a computer 'remembers' what number it has reached while counting?"**
  3.  After a brief discussion, explain that computers, just like us, can 'forget' if they don't have a place to store information. This is the perfect opportunity to introduce the concept of a variable as a 'memory box' for our program. Let's explore how this works.

  {{learn}}
  
  ### **Development (20-30 minutes) - Building the Counter**
  1.  Now that the theory is solid, it's time to build the stopwatch and see these concepts in action. This project is a fantastic example of how loops and variables work together.
  2.  Guide the students through **the instructions for setting up the variable and creating the counting loop**, as detailed in the hands-on section below.
  3.  **Note for the teacher:** Experiment with the activity before the class to anticipate questions.

  ### **Closing (5-10 minutes) - Reflection and Upgrades**
  1.  Once everyone has a working stopwatch, it's time to reflect on the powerful tool they've just used and think about how to make their project even better.
  2.  Use the final section to guide a discussion about other uses for variables and to introduce a challenging new feature for their stopwatch: adding minutes!
  
  {{reflect}}
  
  #### **Additional information for the teacher**
  The solution to the challenge proposed in the reflect section is available at [this link](https://app.protobject.com/generate?cronometro-desafio). Use it as a reference to guide students who may have difficulties.

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "How does a stopwatch work?"
    type: "learn"
    icon: "book-reader"
    content: |
      A stopwatch has a simple job: count the passing seconds. Every second, it essentially says: "**Hey, another second went by. I'll add 1 to the total number of seconds I've already counted.**"
      So, if the stopwatch is at 9 seconds, after one more second passes, it calculates 9 + 1 = 10 seconds. This process repeats over and over... **It's a perfect job for a loop!**
    media: "src/07-stopwatch/a-count.svg"
  
  - title: "What if we lose count?"
    type: "learn"
    content: |
      Have you ever been counting something and forgotten the last number you were on? You have to start all over again! **A computer can have the same problem.**
      To prevent this, you'd probably write the number down. Then, to continue counting, you'd just look at the number, add 1, and write down the new total. You're storing a value that changes over time!
    media: "src/07-stopwatch/a-count-lost.svg"

  - title: "How does the computer 'write it down'?"
    type: "learn"
    content: |
      To solve this memory problem, we use a fundamental programming tool: a **Variable**.
      Think of a variable as a small box inside the computer's memory where you can store something. To keep things organized and remember what's inside, you give the box a name.
      By using a variable, we can make our computer keep count without ever forgetting which number it's on.
    media: "src/07-stopwatch/a-num-var.en.svg"

  - title: "How do we use it?"
    type: "learn"
    content: |
      First, we need to create our variable and give it a name so we know what it's for. In this case, let's call it "**time**."
      Next, we need to give it a starting value. Since a stopwatch starts counting from 0, at the very beginning of our program, we will set the "**time**" variable to be equal to 0.
    media: "src/07-stopwatch/a-num-var-time.en.svg"

  - title: "Variables... They Vary!"
    type: "learn"
    content: |
      As the name suggests, the value inside a variable can change, or "vary." We can take the value out, change it, and then save the new value back into the same variable.
      For our stopwatch, every time our main loop runs, we'll tell the program to add 1 to the value of the "**time**" variable. **And just like that, we're counting!**
    media: "src/07-stopwatch/a-var-change.en.svg"

  - title: "Let's get to work!"
    type: "learn"
    content: |
      To build our stopwatch, we'll start by creating a variable named "time" and setting its initial value to 0. Then, we will create a loop that runs over and over. Inside the loop, we will increase the value of our "time" variable by 1 and then wait for one second.
    media: "src/a.working.svg"

  - id: "create"
    title: "Create"
    type: "create"
    icon: "cogs"
    heading_text: "Now we will build our own stopwatch."
    ready_message: "Now we are ready to write the code."
    steps:
      - "Press <addbutton>Add device</addbutton> and select the <comp>WriteDraw</comp> component. Let's name it **Stopwatch** so we can write the numbers on the screen."
      - "Scan the <qr> code."
      - "Remember that if you don't have a smartphone to scan the **QR** codes, you can press <openwindow>Open in this window</openwindow> to open the components on the same computer."

  - title: "Code Composition"
    type: "code-composition"
    icon: "code"
    content: |
      Click on the question mark symbol to open the comments that explain the code.
      Variables are managed in the <category>Variables</category> category.
    media: "https://app.protobject.com/generate?a07-stopwatch&en&dynamic&-1"


  - id: "reflect"
    title: "What else can we invent?"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "Let's answer the following questions:"
    content: |
      * Besides numbers, what other kinds of information could we store in a variable?
      * What other prototypes could you build now that you know how to make a counter?
      * How could we make our stopwatch count minutes as well as seconds?
    right_content:
      - text: |
          **Challenge**: Let's upgrade our stopwatch to include minutes!
      - text: |
          **Hint**: How many seconds are in a minute? You might need a second variable to track the minutes. Could a loop *inside* your main loop help you count the seconds up to 60 before it adds one to your minute counter?
---