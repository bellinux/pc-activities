---
layout: activity
title: "A Flashing Warning"
image: src/06-traffic-light-with-flashing-yellow-light/06.semaforo-luz-intermitente.svg
video: src/videos/06_intermittent_traffic_light.mp4
video_title: "What will we do?"
description: "Dive deeper into automation by nesting loops to create a realistic, flashing yellow traffic light."
lang: en
permalink: /en/activities/a-flashing-warning/
ref: activity_traffic_light_with_flashing_yellow_light

# ACTIVITY INFO
level: 1
computational_topics:
  - "Loops"
  - "Timing & Events"
general_topics:
  - "Everyday Life"

tags: [Nested Loops, Main Loop, Automation, Flashing Sequence, Timing]

introduction: |
  Ready to make your automations even smarter? Real-world traffic lights don't just change color—they often give a flashing yellow warning. To code this effect without creating a mess, you'll learn an advanced technique: **nested loops**. Get ready to place a loop *inside* another loop to build more complex and powerful programs.

teacher: |
  ### **Courses**
  * Grades 3-12

  ### **Materials**
  * Cellphone, tablet, or computer
  * Internet connection

  ### **Educational Objectives**
  * Understand the concept of "loop," both general and nested.
  * Develop a technological object (prototype) using a device.
  * Identify relationships between technology and the surrounding environment.
  * Evaluate one's own work and that of others, both individually and in teams.
  * Participate in dialogues and reflections to propose improvements.

  ### **Start (10 minutes) - The Flashing Challenge**
  1.  Welcome students and introduce the day’s activity: **"Today, we are going to learn how to create a more advanced and realistic traffic light."**
  2.  Ask the class to think about real-world traffic lights: **"What does the yellow light often do right before it turns red to get your attention?"** Guide them to the idea of a flashing warning.
  3.  Pose the programming challenge: **"How would we code that? We could copy-paste the ON/OFF blocks for the yellow light, but our code would get long and messy very fast!"** This introduces the problem of repetition.
  4.  Explain that to solve this efficiently, we need a new kind of loop—one that can run a specific number of times *inside* our main "forever" loop. This is the perfect introduction to the concept of nested loops.

  {{learn}}

  ### **Development (20-30 minutes) - Building with Nested Loops**
  1.  Now that they've grasped the concept of nesting one loop inside another, it's time to build the advanced traffic light.
  2.  Lead them through **the instructions for modifying the traffic light sequence**, showing them exactly where to add the new numbered loop to create the flashing yellow effect. This will be their first time creating a loop within a loop.

  ### **Closure (5-10 minutes) - Seeing Loops Everywhere**
  1.  Once everyone has a working, flashing traffic light, broaden the discussion to think about where else this powerful concept applies.
  2.  Use the final section to spark a creative discussion about loops in everyday life and challenge them with an even more complex traffic simulation.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "How can we program a flashing light?"
    type: "learn"
    icon: "book-reader"
    content: |
      Imagine we've built an automated traffic light that cycles through its colors inside a "repeat forever" loop. It's a great start, but we can make it more realistic.
      What if we wanted the **yellow light to flash** a few times before turning red? This would be a much better and safer warning for drivers.
    media: "src/06-traffic-light-with-flashing-yellow-light/a.traffic-interm.svg"

  - title: "So, do we just add more blocks?"
    type: "learn"
    content: |
      To make the light flash, we'd need to add a sequence like this to our main loop:
      **Green → Yellow ON → OFF → Yellow ON → OFF → Yellow ON → OFF → Red**
      This works, but it's just repeating the **“Yellow ON → OFF”** sequence. Once again, **our code would become very long and repetitive!** There must be a smarter way.
    media: "src/06-traffic-light-with-flashing-yellow-light/a.loop.large.en.svg"

  - title: "Why Not Another 'Forever' Loop?"
    type: "learn"
    content: |
      You can't have two captains on one ship, and you can't have more than one "repeat forever" (Main Loop) in a program! If you did, the computer wouldn’t know which one is the main program or what to run. It would get confused!
    media: "src/06-traffic-light-with-flashing-yellow-light/a.pc_.confused.svg"

  - title: "The Solution: A Loop Inside a Loop!"
    type: "learn"
    content: |
      This is where a different kind of **loop** comes in handy! We can use a loop that repeats a specific number of times (in the image, 3 times). This is perfect for the flashing part.
      Even better, we can **nest loops**. This means putting one loop *inside* another. Repetitions within repetitions!
    media: "src/06-traffic-light-with-flashing-yellow-light/a.general.loop-2.en.svg"

  - title: "Flashing Yellow: A Nested Loop"
    type: "learn"
    content: |
      By using a numbered loop, we can repeat the **“Yellow ON → OFF”** blocks as many times as we need. By putting this smaller loop *inside* our main "forever" loop, we create a powerful and efficient program:
      Main Loop ( **Green →** *Inner Loop* ( **Yellow ON → OFF** [x4] ) **→ Red** )
    media: "src/06-traffic-light-with-flashing-yellow-light/a.general.loop-inside-2.en.svg"

  - id: "create"
    title: "Let's build our flashing traffic light!"
    type: "create"
    icon: "cogs"
    heading_text: "Let’s create our advanced traffic light."
    steps:
      - "Press <addbutton>Add Device</addbutton> and select <comp>Lamp</comp>."
      - "Scan the <qr> code."
      - "Remember that if you don’t have a smartphone, you can press <openwindow>Open in this window</openwindow>."
    ready_message: "We are ready to start prototyping!"

  - title: "Code Composition"
    type: "code-composition"
    icon: "code"
    content: |
      Click on the question mark icon to open the comments that explain the code.
      The “repeat forever” and the numbered loop blocks are both located in the <category>Basic</category> category.
    media: "[700]https://app.protobject.com/generate?a06-trafficlighflashing&en&dynamic&-1"

  - id: "reflect"
    title: "Reflect"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "You've now mastered nested loops! Ask yourself:"
    content: |
      * Loops aren't just for code; they're everywhere. Where can you see repeating patterns or cycles in everyday life (think music, daily routines, nature)?
      * What other cool prototype could you build using a loop inside a loop?
    right_content:
      - text: |
          **Challenge**: Let’s make 2 traffic lights at an intersection work in sync!
          
          *When one is red, the other should be green and vice versa.*
      - media: "src/06-traffic-light-with-flashing-yellow-light/traffic-challenge.svg"
---