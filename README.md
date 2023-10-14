# LaneDetection

# Table of Contents
- Introduction
- Features
- Requirements
- How it Works

# Introduction
Welcome to the Self-Driving Car Lane Detection System readme! This repository contains a lane detection system designed for self-driving cars. The system uses computer vision techniques to detect and analyze lanes on the road, helping autonomous vehicles navigate safely.

Lane Detection System in Action

# Features
Real-time lane detection: Detect and track lane markings in real-time.
Lane departure warning: Alert the driver or the autonomous system if the car drifts out of the lane.
Lane centering: Assist the car in staying centered within the lane.

# Requirements
Before using the Self-Driving Car Lane Detection System, ensure you have the following requirements met:

- Python 3.x
- OpenCV
- NumPy
- Matplotlib (for visualization)
- A camera or video feed for input (such as a webcam or a video file)

# How it Works
The Self-Driving Car Lane Detection System uses computer vision techniques to process images or video frames from a camera source. 
The main steps include:

1. Capturing a frame from the camera.
2. Preprocessing the image to enhance lane visibility (grayscale, blur, and edge detection).
3. Applying a region of interest mask to focus on the road area.
4. Detecting lane lines using the Hough Transform.
5. Calculating the lane curvature and the vehicle's offset from the lane center.
6. Overlaying the detected lanes onto the original image.


Happy driving! 🚗🤖🛣️
