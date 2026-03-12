---
layout: activity
title: "The Two-Key Safe Box"
image: src/21-safe-box-with-alarm/21.caja-seguridad.svg
video: src/videos/21_safe_box.mp4
video_title: "What will we do?"
description: "Explore cybersecurity concepts and logical operators ('AND') to build a high-security alarm that requires two buttons to be pressed simultaneously."
lang: en
permalink: /en/activities/the-two-key-safe-box/
ref: activity_safe_box_with_alarm

# ACTIVITY INFO
level: 2
computational_topics:
  - "Conditionals & Logic"
  - "Sensors & Input"
general_topics:
  - "Everyday Life"

tags: [Logical Operators (AND), Nested Conditionals, Cybersecurity, Two-Factor Authentication, Multi-device, Tilt Sensor]

introduction: |
  How do banks and your favorite games protect your account from hackers? Often, they use more than just a password. In this mission, you'll dive into the world of **cybersecurity** and logical operators. You'll learn how the **'AND' operator** works by building a high-security safe box that only deactivates if two different keys (buttons) are pressed at the exact same time—just like a real two-factor authentication system!

teacher: |
  ### **Courses**
  * Grades 6-12

  ### **Materials**
  * 3 cellphones, tablets, or computers
  * Internet connection
  * A box (like a shoe box or pizza box) to act as the physical safe
  * An object to be the "treasure" inside

  ### **Educational Objectives**
  * Understand the concept of the logical AND operator and nested conditionals.
  * Create a technological object (prototype) using multiple devices.
  * Identify relationships between technology, security, and the surrounding world.
  * Evaluate personal and peer work.
  * Engage in dialogue and reflection on ideas for improvement.

  ### **Start (10 minutes) - The Digital Lock and Key**
  1.  Welcome students and introduce the day’s activity: **"Today, we are going to create a high-security safe box with a special two-key alarm."**
  2.  Kick off the lesson with a high-interest question: **"Have you ever heard of Cybersecurity? What do you think it is?"**
  3.  Use this discussion to introduce concepts like protecting data and strong passwords. Then, introduce **Two-Factor Authentication (2FA)** as an extra layer of security. Explain that our safe box will use this same principle, requiring two 'keys' to be used at once. This is the perfect moment to introduce the logical **AND** operator.

  {{learn}}

  ### **Development (20-30 minutes) - Building the High-Security Safe**
  1.  Now that the students understand the logic of the 'AND' operator and its connection to cybersecurity, it's time to build the safe.
  2.  Lead them through **the instructions for setting up the three devices and programming the security logic**, as detailed in the hands-on section below. This is a great opportunity for teamwork, with different students managing the safe and each of the two "keys."

  ### **Closure (5-10 minutes) - Thinking Like a Security Expert**
  1.  Once the safes are built and tested, it's time to reflect on the real-world importance of the concepts they've just used.
  2.  Use the final section to guide a discussion about cybersecurity as a field and to encourage them to think about other ways to protect digital information.
  
  {{reflect}}

# DYNAMIC SECTIONS AS ARRAY
content_sections:

  - id: "learn"
    title: "What is Cybersecurity?"
    type: "learn"
    icon: "book-reader"
    content: |
      Cybersecurity is like a digital shield. It's the practice of protecting computers, phones, and important data from malicious people online who want to steal or damage them. Just like you might have a lock on your diary or your room, your online accounts need protection too.
    media: "src/21-safe-box-with-alarm/a-cybersecurity.svg"

  - title: "White Hats vs. Black Hats"
    type: "learn"
    content: |
      On the internet, there are "Black Hats"—malicious hackers who use computer viruses and tricks to steal information. But there are also "White Hats"—cybersecurity experts who work to build defenses and protect data and systems from these attacks. They are the digital superheroes.
    media: 
      - "src/21-safe-box-with-alarm/b-hackers.svg"
      - "src/21-safe-box-with-alarm/b-securityexpert.svg"

  - title: "Your First Line of Defense: Passwords"
    type: "learn"
    content: |
      One of the best ways to protect yourself is by using strong, unique passwords. A strong password is one that nobody can easily guess. If your password is too simple, like "123456" or "password," someone could easily break into your "digital safe" without your permission.
    media: "src/21-safe-box-with-alarm/c-strongpassword.svg"

  - title: "What if your password is stolen?"
    type: "learn"
    content: |
      Even with a strong password, you need a backup plan. That's where **Two-Factor Authentication (2FA)** comes in. It’s like needing a second secret key. For example, after entering your password, a site might send a special code to your phone that you also have to enter. Without that second code, no one can get in, even if they know your password.
    media: "src/21-safe-box-with-alarm/d-two-factor.svg"
  
  - title: "Our Two-Factor Safe!"
    type: "learn"
    content: |
      The safe we’re building today uses the same 2FA principle. To turn off the alarm, you need two keys (our two buttons) to be pressed at the same time. If a thief steals Martin’s button, they still can’t deactivate the alarm without also having Juan’s button. This makes the treasure much safer!
    media: "src/21-safe-box-with-alarm/e-onebutton.svg"

  - title: "Booleans and The AND Operator"
    type: "learn"
    content: |
      Remember that **Booleans** are a simple data type with only two possible values: **TRUE** or **FALSE**. When a button is pressed, its state could be TRUE. When it's not pressed, its state is FALSE.
      The logical **AND** operator is like a strict bouncer who needs to see two forms of ID. It only returns **TRUE** if *all* the conditions it checks are true. If even one is false, the whole result is false.
    media: "src/21-safe-box-with-alarm/f-boolean.en.svg"

  - title: "How AND Secures Our Box"
    type: "learn"
    content: |
      Here's how the logic works for our safe:
      * If Button 1 is pressed (TRUE) **AND** Button 2 is pressed (TRUE) --> The result is **TRUE**, and the alarm is off.
      * If Button 1 is pressed (TRUE) **AND** Button 2 is NOT pressed (FALSE) --> The result is **FALSE**, and the alarm is active.
      * If neither is pressed, the result is also **FALSE**. Both keys are required at the same time!
    media: 
      - "src/21-safe-box-with-alarm/l-box-false-false.en.svg"
      - "src/21-safe-box-with-alarm/m-box-true-false.en.svg"
      - "src/21-safe-box-with-alarm/n-box-true-true.en.svg"

  - id: "create"
    title: "Make the Safe Box"
    type: "create"
    icon: "cogs"
    heading_text: "For this activity, we need 3 devices."
    steps:
      - "On the first device (the safe itself), add <comp>WriteDraw</comp>, <comp>Inclination</comp>, and <comp>AudioPlayer</comp>."
      - "On the second device, add a <comp>TouchButton</comp> (this is Martin’s key)."
      - "On the third device, add another <comp>TouchButton</comp> (this is Juan’s key)."
    right_content:
      - text: |
          **Tip**: You can add multiple components to the same smartphone by pressing the *SCAN* button again after adding the first one.
      - media: "src/general-scan-button.svg"
    ready_message: "We are ready to start prototyping!"

  - title: "Code Composition"
    type: "code-composition"
    icon: "code"
    content: |
      Click on the question mark icon to open comments that explain the code.
    media: "[700]https://app.protobject.com/generate?a21-alarmbuttons&en&dynamic&-1"

  - id: "reflect"
    title: "Reflect"
    type: "reflect"
    icon: "lightbulb"
    heading_text: "You've just used a core cybersecurity principle!"
    content: |
      * Did you find this topic interesting? Cybersecurity is one of the fastest-growing and most important fields in technology. Is it something you could see yourself doing in the future?
      * What other methods do you know to protect your online accounts and data?
    right_content:
      - text: |
          Always remember the importance of **cybersecurity** in our digital world!
---