# Personal Space Detector (Computer Vision Project)

## About this project

This project is based on a simple idea: checking how close people are by using a webcam.

People in places such as a classroom or lab often stand too close to each other without even realizing it. So, I tried to develop a small system that can detect faces and display whether the distance between the faces is safe or not.

The code is not very large, but it works well enough for testing purposes.

## Problem I noticed

It is not very easy to check the distance between people in a real-world scenario by hand.

People are moving all the time, making it hard to check who is standing close to whom. So, in this case, a program can help us more.

## What I actually did

The program uses a webcam to detect faces by using OpenCV. Then it attempts to calculate the distance between the faces.
If the value goes below a certain limit, it shows **"Too Close"**. Otherwise it shows **"Safe Distance"**.

If only one person is visible, it just shows that.

At first, the results were not correct, so I had to test different values for distance and adjust it multiple times.

---

## Features

-Detects faces in real time  
-Calculates distance between people  
-Shows result on screen  

Sometimes detection is a bit slow depending on lighting.

---

## Tech used

Python
OpenCV
NumPy

---

## Requirements

Python 3.8 or above
Webcam (laptop camera works fine)
Works on Windows / Linux / Mac

---

## How to run

Clone the repo first:

git clone https://github.com/your-username/your-repo-name

Go inside the folder:

cd personal-space-detector

Create virtual environment:

python -m venv venv

Activate it:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

Install dependencies:

pip install opencv-python numpy

Make sure this file is present:
haarcascade_frontalface_default.xml

Run the program:

python main.py

---

## How it works (basic idea)

Webcam captures video continuously.

Each frame is first converted to grayscale (this makes detection easier).

Then Haar Cascade is used to detect faces.

After that, center points are taken and distance is calculated between them.

If distance is small → "Too Close"
Otherwise → "Safe Distance"

If only one face is there, it shows "Only one person".

---

## Issues I faced

Initially, the webcam was not opening properly, so I had to debug that.

Also, choosing the correct distance value was confusing. I tested using my phone and laptop camera to check results.

Sometimes it randomly stopped detecting faces, so I had to restart and test again.

Lighting also affects detection sometimes, especially in low light.

I've tested this mostly with my laptop camera, so this may not work on other devices.

---

## Future improvements

Better models, e.g., YOLO
Convert pixel distance to real distance
Add sound alert
Handle more people (not tested yet)