---
layout: activity
title: "Light and Sound Show"
image: src/04-melody-of-happy-birthday-with-lights/04.melodia-con-luces.svg
video: src/videos/04_birthday_light.mp4
video_title: "What will we do?"
description: "Combine lights and music in perfect sync and learn how to use variables to easily control your code's speed."
lang: en
permalink: /en/activities/light-and-sound-show/
ref: activity_melody_of_happy_birthday_with_lights

# ACTIVITY INFO
level: 1
computational_topics:
  - "Variables & Data"
  - "Timing & Events"
general_topics:
  - "Art & Music"

tags: [Variables, Synchronization, Timing, Multi-device Control, Lights, Sound]

introduction: |
  Ready to be the director of your own light and sound show? We're going to combine music and lights to create a perfectly synchronized performance. But what happens when you want to change the tempo? Editing dozens of delay blocks one-by-one is a nightmare. In this mission, you'll learn a pro-level secret to solve this: **variables**. They act as a master remote control for your code, letting you change the speed of your entire show with a single edit.
  

teacher: |
  ### **Courses**
  * Grades 3-12

  ### **Materials**
  * Cellphone, tablet, or computer
  * Internet connection

  ### **Educational Objectives**
  * Understand the concept of a variable and its use.
  * Create a technological object (prototype) using a device.
  * Identify relationships between technology and the surrounding world.
  * Evaluate personal and others’ work.
  * Discuss and reflect on ideas for improvement.

  ### **Start (10 minutes) - The Director's Challenge**
  1.  Welcome students and introduce the day’s activity: **"Today, we will learn how to prototype a synchronized light and music show that's easy to control."**
  2.  Spark the discussion by asking: **"Think about a live concert. What makes it so exciting?"** Guide them toward the idea of lights and visuals all moving in perfect time with the music (synchronization).
  3.  Then, pose the core challenge for today: **"Now, imagine you're the director of that show. You've programmed 50 notes and 50 light flashes. What happens if you suddenly want to make the whole song go faster for the finale? You'd have to find and change 100 different delay blocks!"** This highlights a big problem: inefficiency. Now, you can introduce the elegant solution that programmers use.

  {{learn}}

  ### **Development (20-30 minutes) - Building an Adjustable Show**
  1.  Now that the students understand that variables are the solution to building a smart, adjustable program, it's time to put them to use.
  2.  Guide them through **the process for creating their synchronized prototype**, as detailed in the hands-on section below. Constantly remind them to notice how the single `time` variable is used over and over again, acting as the master control for the show's speed.

  ### **Closure (5-10 minutes) - The Power of a Single Change**
  1.  Once the prototypes are working, the "wow" moment comes from seeing the variable in action.
  2.  Instruct them to **change only the number in the initial `set time to...` block**. Have them try a large number and then a small number to see how dramatically the entire show's tempo changes. This demonstrates the power and efficiency of their new tool. Use the final section to challenge them to expand their creation.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "The Challenge: Sync and Speed"
    type: "learn"
    icon: "book-reader"
    content: |
      The first goal of a good light show is **synchronization**—making sure every light flash happens at the exact same moment as a musical note. This creates a professional and exciting effect.
      But there's a second, bigger challenge: **control**. Imagine you build your whole sequence, but then decide you want it to run faster. You would have to go back and manually change the delay value for *every single note* and *every single light*. For a long song, that could be hundreds of changes! This is slow and a recipe for mistakes.
    media: "src/04-melody-of-happy-birthday-with-lights/a-light.notes_.svg"

  - title: "The Solution: A Variable as Master Control"
    type: "learn"
    content: |
      To solve the problem of having to change many values at once, programmers use **variables**!
      A **variable** is like a box with a label on it. You can store a single piece of information—like a number—inside this box. The powerful part is that you can then use this box in many places throughout your code.
      If you want to change the number, you only have to change it **inside the box one time**. Everywhere you used the box, the value will update automatically. It's like a master control for your code!
    media: "src/04-melody-of-happy-birthday-with-lights/b-variable.notes.en.svg"

  - id: "create"
    title: "Make a Musical Light Show"
    type: "create"
    icon: "cogs"
    heading_text: "Let’s create a prototype that plays ♪ Happy Birthday ♪ with perfectly synchronized—and adjustable—lights."
    content: |
      First, we’ll add the two components we need: one for sound and one for light.
    steps:
      - "Press <addbutton>Add Device</addbutton> and select <comp>MusicalKeyboard</comp>."
      - "Press <addbutton>Add Device</addbutton> again and select <comp>Lamp</comp>."
      - "Remember that if you don’t have smartphones to scan the <qr> codes, you can press <openwindow>Open in this window</openwindow>."
    right_content:
      - text: |
          **Suggestion**: In Protobject, you can add more components on the same smartphone by pressing the SCAN button as many times as you need.
      - media: "src/general-scan-button.svg"

  - title: "Code Composition"
    type: "code-composition"
    icon: "code"
    content: |
      Click on the question mark icon to open the comments that explain the code. Notice how the `time` variable is defined once at the beginning and then used for all the delays. The multiplication blocks are in the <category>Mathematics</category> category.
    media: "[700]https://app.protobject.com/generate?a04-melody-light&en&dynamic&-1"
    right_content:
      - text: |
          **Experiment**: The magic happens here! Try changing the single value of the "time" variable at the top of the code. Set it to `100` to see it go super fast, or `500` to see it go slow.

  - id: "reflect"
    title: "Reflect"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "You've built a smart, adjustable show. What's next?"
    content: |
      You've seen how powerful a single variable can be. What if you wanted to make your show even bigger? How would you add a second lamp that flashes along with the music, maybe on a different phone or with a different color?
    right_content:
      - text: |
          Think about how you would add a new <comp>Lamp</comp> component and connect it to the same master `time` variable.
---