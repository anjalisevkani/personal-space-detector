Personal Space Detector Using Computer Vision

Introduction

A single person might stand too near another without realizing. The screen shows faces as soon as the camera sees them. When two people come within a certain range, the system gives a signal. Instead of guessing, it measures space between heads using live video. From startup onward, it works nonstop as long as the program runs. Someone could walk into view at any moment - then get included automatically.

Problem Statement

A classroom, say, or an office - watch closely and it becomes clear how hard it is to know if folks maintain distance. Spaces fill up, movement blurs patterns, gaps shrink without notice. Someone steps forward while another lingers too close; awareness slips. Even in plain sight, spacing fades into background noise.

Solution

Right there in the footage, it spots faces one by one. As folks move around, their positions get updated constantly through tracking. Distance between each pair is calculated on the fly using frame data. When gaps shrink past a certain point, the alert triggers automatically. Above that line, everything stays quiet without interruption.

Features

Real-Time Face Detection Using Haar Cascade
- Calculates distance between several faces
- Shows status for each frame:
- Safe Distance
- Too Close
- Only one person in frame
About how far something is, shown using pixel numbers.
Starts right in the terminal - skip the window clutter. Runs without a visual interface - just type and go. Needs nothing more than keyboard input - avoiding extra layers. Operates purely through typed commands - no buttons required. Lives inside the shell - bypasses menus completely. Functions straight from text entries - keeps it lean

Technologies Used

- Python 3.x
- OpenCV
- NumPy

System Requirements

Last time we checked, it runs on Python 3.8 at minimum. Anything older won’t work - version matters here. Newer releases fit just fine too
- A webcam (built-in or external)
Any Terminal Windows Linux Mac

Setup and run

1. Clone the project

Start at your computer, type into the command window:

git clone https://github.com/your-username/your-repo-name
cd personal-space-detector

2. Set up a virtual environment

python -m venv venv

3. Start up the virtual environment

On Windows:
venv\Scripts\activate

On Mac or Linux
source venv/bin/activate

4. Install dependencies

pip install opencv-python numpy

5. Look inside to find the needed file

Check that the file named haarcascade_frontalface_default.xml sits inside your project directory.
Might need a trip to OpenCV’s GitHub if it’s gone - toss the file right into your folder’s base when found.

6. Run the project

python main.py

Project Structure

personal-space-detector/
|- main.py
|- haarcascade_frontalface_default.xml
|- README.md

How It Works

Out of the camera comes a live feed, feeding frames one after another. Grayscale takes over each image just before detection begins. Faces emerge through the Haar Cascade method without delay. From every detected face, its middle point is pulled out carefully. Distance between these points forms using straight-line math across space. When gaps shrink below normal range, words shift to “Too Close”. Spacing stays wide enough? Then “Safe Distance” appears instead. One lone figure triggers a different message altogether - just stating presence alone.

Future Improvements

- Switch to deep learning models like YOLO or SSD
- Calibrate the system to show real-world distances, not just pixels
- Add sound alerts when people get too close
- Expand to count crowds and analyze group density

Conclusion

Picture a tool that watches space between people, built using basic vision tech. Running it takes just one line typed into your computer. Efficiency comes first here - no delays, no clutter slowing things down. Ready when you are, sitting there waiting without extra setup. Simple steps lead directly to results. No need to tweak settings before starting up. The whole thing operates quietly in the background. Expect smooth performance every time it runs.