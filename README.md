# YOLO-Based-Real-Time-3D-Object-Detection

## 🤖 YOLO Object Detection with RealSense & ROS

This project uses YOLO and an Intel RealSense camera to detect objects, find their 3D positions, and publish them as navigation goals in ROS. It helps a robot see objects in real time and navigate toward them.

## 🚀 What It Does
- Detects objects in RGB images using a YOLO model (`best.pt`)
- Captures aligned RGB and depth data from the Intel RealSense camera
- Calculates the 3D positions of detected objects using depth information
- Publishes the closest object's 3D position as a navigation goal (`PoseStamped`) to the `navigation_goal` topic in ROS
- Shows live video with detected objects and their 3D positions using OpenCV

## 🛠 Requirements
- ROS installed and running
- Intel RealSense camera with the RealSense SDK
- YOLO model weights file (`best.pt`) — included in this repo
- Python libraries: `torch`, `opencv-python`, `pyrealsense2`

Install the Python dependencies:
```bash
pip install torch opencv-python pyrealsense2
```

## ▶️ How to Run
1. Connect your Intel RealSense camera.
2. Start your ROS master:
   ```bash
   roscore
   ```
3. In a new terminal, run the detection script:
   ```bash
   python detection.py
   ```
4. A live video window will open showing detected objects with their 3D positions overlaid.
5. The 3D position of the closest detected object is published to the `navigation_goal` ROS topic, which other nodes (e.g. a navigation stack) can subscribe to.

## 📁 Project Structure
- `detection.py` — main script: runs YOLO detection, computes 3D positions from depth data, publishes to ROS
- `best.pt` — trained YOLO model weights

## Status
Built as a robotics/computer vision project combining object detection with depth sensing for real-time robot navigation.
