---
layout: activity
title: "Smart Code: Using Functions"
image: src/20-light-button-panel/20.botonera-luces.svg
video: src/videos/20_light_button_panel.mp4
video_title: "What will we do?"
description: "Learn to write cleaner, reusable code by creating functions with parameters for a two-button light game."
lang: en
permalink: /en/activities/smart-code-using-functions/
ref: activity_light_button_panel

# ACTIVITY INFO
level: 2
computational_topics:
  - "Functions"
  - "Timing & Events"
general_topics:
  - "Mathematics & Logic"

tags: [Functions, Parameters, Reusable Code, Events, User Input]

introduction: |
  Tired of copying and pasting the same blocks over and over? As your programs get more complex, you need a way to stay organized and efficient. The ultimate pro-coder secret to this is the **Function**! In this mission, you'll learn how to bundle your code into smart, reusable blocks that can be called anytime. Get ready to build a single light pattern function that can be triggered by different buttons to create different results.

teacher: |
  ### **Courses**
  * Grades 6-12

  ### **Materials**
  * Cell phone, tablet, or computer
  * Internet connection

  ### **Educational Objectives**
  * Understand the concept of functions and parameters.
  * Create a technological object (prototype) using a device.
  * Identify relationships between technology and the surrounding world.
  * Evaluate personal and others’ work.
  * Engage in dialogue and reflection on improvement ideas.

  ### **Start (10 minutes) - The Problem with Repetition**
  1.  Welcome students and introduce the day’s activity: **"Today we will learn how to write smarter, more efficient code using functions."**
  2.  Kick off the lesson by asking: **"Imagine you're writing a program and you need to use the exact same 10 blocks of code in five different places. What's the problem with just copying and pasting them?"** (Guide them to issues of size, messiness, and the difficulty of making changes—you'd have to fix a bug in 5 places!).
  3.  Explain that programmers have a powerful solution for this: **Functions**. Use the analogy of a recipe: instead of writing out the steps every time, you just refer to the recipe name. This is the perfect entry point to explain how functions help us write reusable code.

  {{learn}}

  ### **Development (20-30 minutes) - Building a Reusable Function**
  1.  Now that the students understand the power of creating reusable code blocks, it's time to build their first function.
  2.  Lead them through **the instructions for creating their own `light_sequence` function and then calling it from two different button events**, as detailed in the hands-on section below. This is their first time defining a custom block and then using it in their program, which is a major step.

  ### **Closure (5-10 minutes) - The Power of Parameters**
  1.  Once everyone has their two-button light panel working from a single function, it's time to reflect on the power and elegance of this new tool.
  2.  Use the final section to encourage experimentation with the function's parameters and to challenge them to build a second, different function for another task.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "What are functions?"
    type: "learn"
    icon: "book-reader"
    content: |
      Functions are reusable groups of code that you can name and then "call" whenever you need them.
      Imagine you have a favorite recipe with five steps to make dinner. Instead of writing those five steps out every single time, you can create a single "recipe card" named "DINNER". Now, you only need to call that one function, and the program runs all five steps. This is a function **without parameters** because it does the exact same thing every time.
    media: "src/20-light-button-panel/a-dinner.svg"

  - title: "Functions with Parameters"
    type: "learn"
    content: |
      But what if you want to make the same recipe with different main ingredients? We can make our function smarter by giving it **parameters**—inputs that can change the result.
      Think of the DINNER function again. We can add a parameter for the main ingredient. Now, calling `DINNER(noodles)` will give a different result than `DINNER(rice)`. The steps are the same, but the input changes the outcome.
      In our activity, we will create a `light_sequence` function with a **color** parameter. The function will always perform the same blinking pattern, but the color of the light will change based on the parameter we provide when we call it.
    media: "src/20-light-button-panel/b-green-red.svg"

  - id: "create"
    title: "Make the Light Panel"
    type: "create"
    icon: "cogs"
    heading_text: "Let's create the prototype. We'll need 3 devices (or open them in the same window)."
    steps:
      - "On the first device, add the <comp>Lamp</comp> component."
      - "On the second device, add the first <comp>TouchButton</comp>."
      - "On the third device, add the second <comp>TouchButton</comp>. Remember, you can use <openwindow>Open in this window</openwindow> to open components on your computer."
    right_content:
      - text: |
          **Tip**: You can add more components on the same smartphone by pressing the *SCAN* button as many times as you need.
      - media: "src/general-scan-button.svg"
    ready_message: "We are ready to start prototyping!"

  - title: "Code Composition"
    type: "code-composition"
    icon: "code"
    content: |
      Click on the question mark icon to open comments that explain the code.
    media: "[600]https://app.protobject.com/generate?a20-functions&en&dynamic&-1"

  - id: "reflect"
    title: "Reflect"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "You've created your first function! Now it's time to experiment."
    content: |
      * How would you add a third button that calls the same function but with the color **blue**?
      * How would you change the speed of the blinking? (Hint: you only have to edit the function in one place!)
      * What if you wanted to create a second, completely different light pattern? Would you create a new function?
    right_content:
      - text: |
          **Challenge**: Modify the project to display a message on the screen. Create a *new* function that takes two parameters: the **text** to display and the **color** of the text.
      - text: |
          **Hint**: You'll need the <comp>WriteDraw</comp> component. Then, define a new function with parameters for the text and the color to handle writing the message on the screen.
    media: "src/videos/light_challenge.mp4"
---