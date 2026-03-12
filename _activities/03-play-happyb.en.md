---
layout: activity
title: "Play a Song"
image: src/03-playing-happy-birthday/03.tocando-melodia.svg
video: src/videos/03_happy_birthday.mp4
video_title: "What will we do?"
description: "Turn your device into a musical instrument! Learn to sequence notes and control their timing to play a familiar tune."
lang: en
permalink: /en/activities/play-a-song/
ref: activity_playing_happy_birthday

# ACTIVITY INFO
level: 1
computational_topics:
  - "Programming Fundamentals"
  - "Timing & Events"
general_topics:
  - "Art & Music"

tags: [Musical Notes, Sequencing, Timing, Sound, Speaker]

introduction: |
  Time to become a digital musician! This activity will turn your device into an instrument. You'll learn how to program a sequence of **musical notes** and use **timing** to control their rhythm, piecing together the classic 'Happy Birthday' song one block at a time.
  

teacher: |
  ### **Courses**
  * Grades 3-12

  ### **Materials**
  * Smartphone, tablet, or computer
  * Internet connection

  ### **Educational Objectives**
  * Understand the concepts of sequencing steps.
  * Create a technological object (prototype) using a device.
  * Identify relationships between technology and the surrounding world.
  * Evaluate personal and others’ work.
  * Engage in dialogue and reflection on improvement ideas.

  ### **Start (10 minutes) - The Science of Sound**
  1.  Welcome students and introduce the day’s activity: **"Today, we are going to learn how to create a prototype of a musical toy."**
  2.  Spark their curiosity with a question: **"How do you think your phone or headphones produce sound?"**
  3.  After a brief discussion, it's time to demystify the technology. Let's explore how a simple speaker can turn silent electrical signals into the music and sounds we hear every day.

  {{learn}}

  ### **Development (20-30 minutes) - Composing the Melody**
  1.  Now that everyone understands the basics of digital sound, let's start composing! The mission is to recreate the "Happy Birthday" song by programming the correct sequence of notes and delays.
  2.  Guide your students through **the step-by-step instructions for building the melody**, which are detailed in the hands-on section below.
  3.  The required sequence of notes is: **C4, C4, G4, G4, A4, A4, G4, F4, F4, E4, E4, D4, D4, C4**. Ensure they arrange the blocks in this precise order.

  ### **Closure (5-10 minutes) - Reflection and Remixing**
  1.  Once the students have a working song, challenge them to think like music producers. How could they change the tempo?
  2.  Pose the challenge: **"What if we want to play the song faster or slower?"** Use this question to lead into a discussion about how changing every single delay value can be tedious, setting the stage for more advanced concepts like variables. Use the final section to guide the conversation.

  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "How do devices produce sound?"
    type: "learn"
    icon: "book-reader"
    content: |
      Ever wonder how your phone can blast your favorite tunes? The magic happens in a tiny component called a **speaker**. Think of it as a device that converts electrical signals into sound waves. A magnet and a coil inside move when electricity passes through them, causing a cone to vibrate. These vibrations create the sound waves that travel through the air to our ears.
      Our brain interprets these waves as music, voices, or sound effects, allowing us to enjoy a movie or sing along to a song.
    media: "src/03-playing-happy-birthday/a-speaker.svg"

  - title: "Speakers are everywhere!"
    type: "learn"
    content: |
      You can find speakers in all sorts of devices! They're in your TV, inside your headphones, and of course, in your smartphone. If you've ever watched a video or listened to music on your phone, you've heard its speakers in action.
    media:
      - "src/03-playing-happy-birthday/a-tv.svg"
      - "src/03-playing-happy-birthday/a-headphones.svg"
      - "src/03-playing-happy-birthday/a-smartphone.svg"

  - id: "create"
    title: "Let's Play a Song"
    type: "create"
    icon: "cogs"
    heading_text: "We're going to create a prototype that plays 'Happy Birthday' on the phone. First, let's connect our device."
    steps:
      - "Click on <addbutton>Add device</addbutton> on the left sidebar."
      - "Select the component <comp>MusicalKeyboard</comp> to play notes on the smartphone."
      - "Scan the <qr> code with your smartphone or press <openwindow>Open in this window</openwindow>."

  - title: "Drag the notes!"
    type: "create"
    content: |
      To build a melody, you need to drag the note blocks into the workspace in the correct sequence.
    media: "src/03-playing-happy-birthday/a-dragnote.en.svg"
    
  - title: "How to control the duration of a note?"
    type: "create"
    content: |
      ### We use delays!

      A melody isn't just about notes; it's also about rhythm. To control how long a note plays, you need to add a pause before the next one starts.
      
      For example:
      * play a note
      * **wait 400 milliseconds**
      * play the next note
      * **wait 200 milliseconds**
      * … and so on.
    right_content:
      - text: |
          **Pro Tip:** The **delay** blocks that control these pauses are found in the <category>Timing</category> category. They are essential for creating the rhythm of your song!

  - title: "What is the sequence of notes and delays?"
    type: "create"
    content: |
      The main part of “Happy Birthday” has this sequence of notes with their respective delays, measured in milliseconds (ms).
    media: "src/03-playing-happy-birthday/a-noteduration.en.svg"

  - title: "Code Composition"
    type: "code-composition"
    icon: "code"
    content: |
      Click on the question mark icon to open the comments that explain the code.
    media: "[700]https://app.protobject.com/generate?a03-melody&en&dynamic&-1"

  - id: "reflect"
    title: "Reflect"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "You've coded a song, but what if you wanted a remix?"
    content: |
      To change the tempo, you need to adjust the delays. Right now, your song uses pauses of 200, 400, and 600 milliseconds.

      What if you wanted to play it twice as fast? You'd have to go back and change *every single delay block* by hand. That sounds like a lot of work! Is there a smarter, more efficient way to control the speed?
---