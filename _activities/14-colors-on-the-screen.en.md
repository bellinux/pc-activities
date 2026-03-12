---
layout: activity
title: "Mixing RGB Colors"
image: src/14-colors-on-the-screen/14.colores-pantalla2.svg
video: src/videos/14_color_mix.mp4
video_title: "What will we do?"
description: "Become a digital artist! Use three knobs to control the Red, Green, and Blue channels and mix any color you can imagine."
lang: en
permalink: /en/activities/mixing-rgb-colors/
ref: activity_colors_on_the_screen

# ACTIVITY INFO
level: 1
computational_topics:
  - "Sensors & Input"
  - "Loops"
general_topics:
  - "Art & Music"
  - "Science & Technology"

tags: [Color Theory, RGB, Potentiometer, Main Loop, Analog Input, Color Mixing]

introduction: |
  How does your phone or TV screen create millions of different colors when it only uses three types of tiny lights? By mixing them! In this mission, you'll become a digital artist and color scientist. You'll take control of the three primary colors of light—**Red**, **Green**, and **Blue (RGB)**—using three separate knobs to mix any color you can imagine and master the digital rainbow.

teacher: |
  ### **Courses**
  * Grades 3-12

  ### **Materials**
  * Cell phone, tablet, or computer
  * Internet connection

  ### **Educational Objectives**
  * Understand the concept of color and how it is represented digitally (RGB).
  * Create a technological object (prototype) using a device.
  * Identify relationships between technology and the surrounding world.
  * Evaluate personal and others’ work individually or in a team.
  * Engage in dialogue and reflection on ideas for improvement.

  ### **Start (10 minutes) - The Science of Color**
  1.  Welcome students and introduce the day’s activity: **"Today, we will learn how screens create every color you've ever seen."**
  2.  Ask a guiding question: **"How do you think your eyes see the color of an apple? And how is that different from how a screen *creates* color?"**
  3.  This discussion will naturally lead to the idea of reflected light versus emitted light. Explain that screens work by *adding* light together, which is the perfect time to introduce the two main color models: Additive (for screens) and Subtractive (for print).

  {{learn}}

  ### **Development (20-30 minutes) - Mixing the Rainbow**
  1.  Now that the students have a solid understanding of RGB color theory, it's time to put it into practice and become digital color mixers.
  2.  Lead them through **the instructions for setting up their three-knob controller and programming the color-mixing logic**, as detailed in the hands-on section below. This is a great exercise in managing multiple real-time inputs at once.

  ### **Closure (5-10 minutes) - Becoming a Color Expert**
  1.  Once everyone is experimenting with creating different colors, bring the group back together for a final reflection on what they've learned.
  2.  Use the final section to reinforce the core concepts of color theory and to challenge them to create a lamp that changes color automatically, without any knobs at all.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "How do we see colors?"
    type: "learn"
    icon: "book-reader"
    content: |
      When light hits an object, like an apple, the object's surface absorbs most of the light but reflects some of it. Our eyes see this reflected light.
      If we see a **red** apple, it means its skin is absorbing all colors *except* for red. The red light bounces off, reaches our eyes, and our brain says, "That's red!"
    media: "src/14-colors-on-the-screen/a.reflection2.svg"

  - title: "How do we mix colors?"
    type: "learn"
    content: |
      To create colors with light, we have to mix different **rays of light**. If we mix **all** the colors of light together, we get pure **white light**. The total absence of light is **black**.
      You can see this in nature! After it rains, tiny water droplets in the air can act like prisms and **separate** white sunlight into all its component colors, creating a **rainbow**!
    media: "src/14-colors-on-the-screen/b.color_.freedom2.svg"

  - title: "Subtractive Synthesis (Paint & Ink)"
    type: "learn"
    content: |
      In this model, the color of an object depends on the light it **reflects**. The primary colors are Cyan, Magenta, and Yellow. Because this model works by *subtracting* (absorbing) light, mixing all three colors results in **Black**. This model is used for things that don't emit their own light, like photo printing, dyes, and paints.
    media: "src/14-colors-on-the-screen/c-sustractive.en.svg"
  
  - title: "Additive Synthesis (Screens & Light)"
    type: "learn"
    content: |
      In this model, color is created by **adding** different lights together. The primary colors are **Red, Green, and Blue (RGB)**.
      - **Red + Green** = **Yellow**
      - **Green + Blue** = **Cyan**
      - **Red + Blue** = **Magenta**
      Since we are mixing pure light, combining all three at full intensity results in **White Light**. This model is used for all screens, like TVs, phones, and computer monitors.
    media: "src/14-colors-on-the-screen/d-additive.en.svg"

  - title: "How does a monitor use RGB?"
    type: "learn"
    content: |
      Your screen is made of millions of tiny dots called pixels. Each pixel is actually a team of three even tinier LEDs: one **R**ed, one **G**reen, and one **B**lue.
      To create a specific color for that one pixel—say, purple—the screen tells the red and blue LEDs to light up brightly, and the green one to stay dim. Multiply that process by millions of pixels, and you get a full, rich image!
    media: "src/14-colors-on-the-screen/e-pixels.svg"

  - id: "create"
    title: "Let's Play with Colors!"
    type: "create"
    icon: "cogs"
    heading_text: "Let’s create a prototype that allows us to mix and create any color of light."
    content: |
      We'll need 4 components: 1 lamp to show the color, and 3 knobs to control each primary color (Red, Green, and Blue).
    steps:
      - "Press <addbutton>Add device</addbutton>, select <comp>Lamp</comp>, and press <openwindow>Open in this window</openwindow>."
      - "Press <addbutton>Add device</addbutton>, select <comp>Knob</comp>, and scan the <qr> code with a smartphone to control the **red** color."
      - "Add two more <comp>Knob</comp> components on two other smartphones to control the **green** and **blue** colors."
    ready_message: "We are ready to start prototyping!"

  - title: "Code Composition"
    type: "code-composition"
    icon: "code"
    content: |
      Click on the question mark icon to open the comments that explain the code.
    media: "[700]https://app.protobject.com/generate?a14-colors&en&dynamic&-1"

  - id: "reflect"
    title: "Reflect"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "You are now a master of the digital rainbow!"
    content: |
      * What are the RGB 'recipes' for some of your favorite colors, like orange, pink, or teal? Experiment and find out!
      * When you're editing a photo on an app, are you using the Additive or Subtractive color model? What about when you're mixing paint for an art project?
    right_content:
      - text: |
          **Challenge**: Let’s create a lamp that gradually cycles through all the colors of the rainbow on its own, without being controlled by knobs!
      - text: |
          **Hint**: You could use loops and variables to slowly increase and decrease the values for Red, Green, and Blue over time.
---