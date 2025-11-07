# Real-Time Face Recognition System

## Description

This project aims to develop a **Real-Time Face Recognition system** using Python and OpenCV.  
The primary problem it solves is **automated and secure access control or attendance tracking**.

**Target Users:** Small businesses, universities, or developers needing a basic biometric security layer.  
**Expected Outcome:** A functional, stable application that can recognize and label known faces from a live webcam feed and classify unknown faces.

---

## Objectives

1. Successfully implement a **real-time video stream capture** from a webcam using OpenCV.
2. Develop a **robust face encoding function** to accurately map and store known facial features.
3. Achieve **face recognition accuracy** in varied lighting conditions for known faces.
4. Create a **simple, user-friendly interface** to display the results (bounding box and name/label).

---

## Team Members and Roles

| Team Member    | GitHub Account | Role                         | Responsibilities                                                                                                                |
| -------------- | -------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Abdallah Ragab | Abdallah       | Initial Setup and Core Logic | Environment setup, known faces data collection, implementing face encoding and comparison logic, managing the GitHub repository |
| Mohamed Wael   | Mohamed        | Development and Testing      | Implementing webcam stream capture (OpenCV), drawing bounding boxes/labels, system integration, unit and integration testing    |

---

## Tools and Usage

| Tool/Library     | Purpose                        | Usage Details                                                                   |
| ---------------- | ------------------------------ | ------------------------------------------------------------------------------- |
| Python 3         | Core programming language      | All project scripting and application development                               |
| Face_recognition | Facial encoding and comparison | Used for load_image_file(), face_encodings(), face_locations(), compare_faces() |
| OpenCV (cv2)     | Video capture and display      | Used for VideoCapture(), imshow(), rectangle(), putText()                       |
| NumPy            | High-performance array ops     | Used by face_recognition for manipulating image data and encodings              |
| IDE (VS Code)    | Code writing and debugging     | Writing and debugging Python scripts for the entire system                      |

---

## 4-Week Plan

| Week   | Milestones                      | Deliverables                                                                                      | Assigned                      |
| ------ | ------------------------------- | ------------------------------------------------------------------------------------------------- | ----------------------------- |
| Week 1 | Planning and Setup              | Fully functional environment setup; webcam test script; known face images collected and organized | Abdallah Ragab & Mohamed Wael |
| Week 2 | Development Phase 1             | Script for encoding/storing known faces; detect & draw box on a static image                      | Abdallah Ragab                |
| Week 3 | Development Phase 2 and Testing | Integrated real-time script; label known faces & "Unknown"; initial test report                   | Mohamed Wael                  |
| Week 4 | Finalization and Presentation   | Refined UI/UX, code cleanup, documentation, error handling; final demo & presentation slides      | Abdallah Ragab & Mohamed Wael |

---

## Checklist for Detailed Tasks

- ✅ Install Python, OpenCV, and Face_recognition library.
- ✅ Collect 5-10 high-quality images of known people for training.
- ✅ Write script to capture and display live webcam feed.
- ✅ Write function to encode the known faces.
- ✅ Implement face detection in the live stream.
- ✅ Implement face comparison (matching) logic.
- ✅ Display results (bounding box and name/label) in real-time.
- ✅ Conduct testing with known and unknown faces.
- ✅ Prepare the final code and project presentation.
