---
layout: activity
title: "The Switch: On or Off?"
image: src/09-turn-on-the-light/09.enciende-luz.svg
video: src/videos/09_light_switch.mp4
video_title: "What will we do?"
description: "Explore more advanced logic with 'If-Then-Else' conditionals to create a fully functional light switch."
lang: en
permalink: /en/activities/the-switch-on-or-off/
ref: activity_turn_on_the_light

# ACTIVITY INFO
level: 1
computational_topics:
  - "Conditionals & Logic"
  - "Loops"
general_topics:
  - "Mathematics & Logic"

tags: [Conditionals, If-Then-Else, Main Loop, Switch, User Interface]

introduction: |
  So far, we've told our programs 'IF this happens, THEN do that.' But what about the 'otherwise'? In the real world, actions often have two sides: on or off, locked or unlocked, true or false. In this mission, you'll level up your logic skills with the **'IF... THEN... ELSE'** conditional. Get ready to build a fully functional light switch that knows exactly what to do, whether the switch is on *or* off.

teacher: |
  ### **Courses**
  * Grades 3-12

  ### **Materials**
  * Cellphone, tablet, or computer
  * Internet connection

  ### **Educational Objectives**
  * Understand the concepts of "if/then/else" conditionals.
  * Create a technological object (prototype) using a device.
  * Identify relationships between technology and the world around them.
  * Evaluate personal and peer work.
  * Engage in dialogue and reflection on improvement ideas.

  ### **Start (10 minutes) - The Power of 'Otherwise'**
  1.  Welcome students and introduce the day’s activity: **"Today we will learn how to build a fully functional light switch with Protobject."**
  2.  Start by recapping the simple 'IF/THEN' conditional. Then, introduce a more complex problem with an analogy: **"Imagine you go to the store for your favorite snack. IF they have it, THEN you buy it. But what if they *don't* have it? What do you do ELSE (otherwise)?"**
  3.  This introduces the need for an alternative action. Explain that this 'IF/THEN/ELSE' logic is crucial for creating interactive programs, like the light switch we'll build today.

  {{learn}}

  ### **Development (20-30 minutes) - Programming a Choice**
  1.  Now that the students understand the logic of choosing between two different actions, it's time to program their digital switch.
  2.  Lead them through **the instructions for building the 'IF/THEN/ELSE' program**, as detailed in the hands-on section below. Pay special attention to how the 'TURN ON' block goes in the 'DO' slot and the 'TURN OFF' block goes in the 'ELSE' slot, representing the two choices.

  ### **Closure (5-10 minutes) - Seeing 'IF/ELSE' Everywhere**
  1.  Once everyone has a working switch, encourage them to think about how this two-part logic applies to the world around them.
  2.  Use the final section to spark a brainstorming session on other 'IF/THEN/ELSE' scenarios and to challenge them to upgrade their current project with sound.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Leveling Up Our Logic"
    type: "learn"
    icon: "book-reader"
    content: |
      We've seen how a simple conditional works: **IF** a condition is true, **THEN** an action happens. But what if the condition is *false*? Usually, the program just does nothing.
      To make our code smarter, we can add a second part: an **ELSE**.
      The full structure, “if, then, else,” gives the computer a complete set of instructions: “**if** something is true, **then** do this; **else** (otherwise), do something completely different.”
    media: "src/09-turn-on-the-light/a-if-else-condition.en.svg"

  - title: "IF pressed, THEN on, ELSE off."
    type: "learn"
    content: |
      A light switch is a perfect example of this. The logic is simple: “**if** the switch is active, **then** turn on the light; **else**, turn off the light.”
      This means that if the program detects that the switch is active, it will execute the action in the "then" (or "do") part. But if the switch is *not* active, it will execute the action in the "else" part instead.
      And how do we make our program check the switch constantly? With the **main loop**, of course!
    media: "src/09-turn-on-the-light/a-if-else-condition-lamp.en.svg"

  - id: "create"
    title: "Make a Lamp with a Switch"
    type: "create"
    icon: "cogs"
    heading_text: "Let’s create a prototype that lets us turn on a light by pressing a button."
    content: |
      First, we'll add two components: one to act as our switch, and a second to be our light.
    steps:
      - "Press <addbutton>Add Device</addbutton> and select <comp>Lamp</comp>."
      - "Press <addbutton>Add Device</addbutton> again and select <comp>Switch</comp>."
      - "Remember that if you don’t have smartphones to scan the <qr> codes, you can press <openwindow>Open in this window</openwindow> to open the components on the same computer."
    right_content:
      - text: |
          **Tip**: In Protobject, you can add more components on the same smartphone by pressing the *SCAN* button as many times as you need.
      - media: "src/general-scan-button.svg"

  - title: "Code Composition"
    type: "code-composition"
    icon: "code"
    content: |
      Click on the question mark icon to open the comments that explain the code.
    media: "[700]https://app.protobject.com/generate?a09-lampswitch&en&dynamic&-1"

  - id: "reflect"
    title: "Reflect"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "You've built a program that can make a choice!"
    content: |
      This 'IF/THEN/ELSE' logic is one of the most important concepts in all of programming.
      *Think about your daily life or your favorite apps. Where do you see this kind of two-part choice being made? (e.g., IF a password is correct, THEN log in, ELSE show an error message).*
    right_content:
      - text: |
          **Challenge**: Upgrade this project by adding music that plays *only* when the light is turned on.
      - text: |
          **Hint**: You'll need the <comp>AudioPlayer</comp> component. Where in your IF/ELSE block would you put the 'play sound' and 'stop sound' commands?
---