---
layout: activity
title: "Control Light Intensity"
image: src/13-lamp-with-variable-intensity/13.lampara-intensidad-variable.svg
video: src/videos/13_light_intensity.mp4
video_title: "What will we do?"
description: "Explore the world of color and light by using a knob to gradually change a lamp's brightness from black to white."
lang: en
permalink: /en/activities/control-light-intensity/
ref: activity_lamp_with_variable_intensity

# ACTIVITY INFO
level: 1
computational_topics:
  - "Sensors & Input"
  - "Timing & Events"
general_topics:
  - "Science & Technology"

tags: [Potentiometer, Events, Analog Input, Color, Grayscale, Light Intensity]

introduction: |
  We've used a knob to control volume; now let's use that same analog power to control light! In this mission, you'll dive into the science of digital color (RGB) and learn how your screen creates every shade from pure black to brilliant white. You'll then build your own dimmer switch, using a **potentiometer** to smoothly control the intensity of a virtual lamp.

teacher: |
  ### **Courses**
  * Grades 3-12

  ### **Materials**
  * Cellphone, tablet, or computer
  * Internet connection

  ### **Educational Objectives**
  * Understand the concepts of events and potentiometers.
  * Create a technological object (prototype) using a device.
  * Identify relationships between technology and the surrounding world.
  * Evaluate personal work and that of others.
  * Engage in dialogue and reflection on improvement ideas.

  ### **Start (10 minutes) - The Science of Screen Color**
  1.  Welcome students and introduce the day’s activity: **"Today, we will learn how to prototype a lamp with variable intensity—a dimmer switch."**
  2.  Ask a guiding question: **"Have you ever noticed that the colors in a printed magazine look different from the same image on a screen? Why do you think that is?"**
  3.  This question is the perfect gateway to explaining the difference between **subtractive color** (ink/paint) and **additive color** (light/screens). Explain that screens use the additive RGB (Red, Green, Blue) model. Then, introduce the tool for gradual control: the **potentiometer**, which will act as our dimmer.

  {{learn}}

  ### **Development (20-30 minutes) - Building the Dimmer**
  1.  Now that the students understand the theory of additive color and how a potentiometer can control it, it's time to build the dimmer switch.
  2.  Lead them through **the instructions for creating the lamp and programming the intensity control**, as detailed in the hands-on section below. Make sure they see how the knob's single value is fed into all three color channels (R, G, and B) to create a grayscale effect.

  ### **Closure (5-10 minutes) - Reflection on Color and Control**
  1.  Once everyone has a working dimmer switch, it's time to reflect on the color theory they've just put into practice.
  2.  Use the final section to guide a discussion about controlling individual colors (a great teaser for the next activity) and to challenge them to combine light and sound in their project.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "Print vs. Screen Colors"
    type: "learn"
    icon: "book-reader"
    content: |
      **Subtractive color** (like ink on paper) starts with a white surface and *subtracts* light. Mixing all the primary ink colors (Cyan, Magenta, Yellow) results in black.
      **Additive color** (like a phone screen) starts with a black surface and *adds* light. The primary colors are Red, Green, and Blue (RGB). Mixing all three at full intensity creates pure white light. This is the model we use in Protobject!
    media: "src/13-lamp-with-variable-intensity/a-additive-substactive.en.svg"

  - title: "Additive Color and Shades of Gray"
    type: "learn"
    content: |
      In the additive RGB model, we can create different shades of gray by mixing **equal amounts** of red, green, and blue light.
      * A **low intensity** of all three colors results in a **dark gray**.
      * A **high intensity** of all three results in a **light gray**.
      * **Black** is the total absence of light (all colors off), while **white** is all three colors at their maximum intensity.
    media: "src/13-lamp-with-variable-intensity/b-opacity.svg"

  - title: "Using a Potentiometer to Control Intensity"
    type: "learn"
    content: |
      To control the brightness of our light, we need an analog input. The **potentiometer** is the perfect tool for this! It's a component, usually controlled with a knob, that provides a smooth range of values.
      We can use the value from the potentiometer to set the brightness for the red, green, and blue pixels on the screen all at once. By turning the knob, we can make the screen display any shade from black all the way to white.
    media: "src/13-lamp-with-variable-intensity/b-opacity-knob.svg"
  
  - title: "Let's get to work!"
    type: "learn"
    content: |
      We will use the potentiometer to modify the intensity of our lamp. As we turn the knob, our program will read its value and convert that into a brightness level for the lamp, adjusting it in real-time.
    media: "src/a.working.svg"

  - id: "create"
    title: "Make the Variable Lamp"
    type: "create"
    icon: "cogs"
    heading_text: "Let’s create the prototype to control the light's intensity."
    content: |
      First, we'll add two components: one to act as our lamp and another to be our dimmer knob.
    steps:
      - "Press <addbutton>Add Device</addbutton>, select <comp>Lamp</comp>, and press <openwindow>Open in This Window</openwindow>."
      - "Press <addbutton>Add Device</addbutton> again, select <comp>Knob</comp>, and scan the <qr> code with your smartphone."
    ready_message: "We're ready to start prototyping!"

  - title: "Code Composition"
    type: "code-composition"
    icon: "code"
    content: |
      Click on the question mark icon to open the comments that explain the code.
      The color blocks can be found in the <category>Color</category> category.
      **Remember**: You can build this using an **event** (more efficient) or a **main loop**.
    media: "[700]https://app.protobject.com/generate?a13.knobluz&en&dynamic&-1"

  - id: "reflect"
    title: "Reflect"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "You've controlled the intensity of white light!"
    content: |
      You did this by sending the *same* value from the knob to the Red, Green, and Blue channels.
      *But what if you sent *different* values? How would you program the knob to only adjust the intensity of the red light, while green and blue stay off?*
    right_content:
      - text: |
          **Challenge**: Modify the project so that when the light intensity (the knob's value) goes above 80, a song starts to play.
      - text: |
          **Hint**: You'll need the <comp>AudioPlayer</comp> component. Inside your event or loop, you can use a conditional: **IF** the knob's value is greater than 80, **THEN** play the song, **ELSE** stop the song.
---