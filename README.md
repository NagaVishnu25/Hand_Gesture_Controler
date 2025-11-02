# 🖐️ AI Hand Gesture Mouse Controller

Control your computer’s mouse with simple hand gestures using **Python**, **MediaPipe**, and **OpenCV**.  
This project tracks your hand in real-time to move the cursor, click, and scroll — all using your webcam.

---

## 🚀 Features

- Move mouse with your **index finger**
- Perform **single click** by touching **index + thumb**
- Perform **double click** by touching **index + middle finger**
- Scroll **up** with **index + middle finger up**
- Scroll **down** with **ring + pinky finger up**
- Real-time hand tracking using **MediaPipe**
- Works on any standard webcam

---

## 🎮 Gesture Controls

| Gesture | Action |
|----------|--------|
| Index finger only | Move the mouse pointer |
| Index + Thumb touch | Single click |
| Index + Middle touch | Double click |
| Two fingers up | Scroll up |
| Ring + Pinky up | Scroll down |
| Press `ESC` | Exit the program |

---

## 🧩 Requirements

- Python 3.8 or above  
- OpenCV  
- MediaPipe  
- PyAutoGUI  
- Keyboard  

---

## ⚙️ Installation

1. **Install required libraries**
   ```bash
   pip install opencv-python mediapipe pyautogui keyboard
Run the script

bash
Copy code
python gesture_mouse.py
🧠 How It Works
The webcam captures the live video feed.

MediaPipe detects your hand and identifies key points (landmarks).

Based on finger positions, the program performs corresponding mouse actions using PyAutoGUI.

⚠️ Notes
Keep your hand clearly visible to the camera.

Use in good lighting conditions for better accuracy.

Press ESC to close the application.

👨‍💻 Author
Naga Vishnu Ch
Frontend & Python Developer
