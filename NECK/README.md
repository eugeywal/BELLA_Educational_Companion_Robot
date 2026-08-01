Markdown
# 🤖 BELLA's_Arduino_Vision_Servo_Control_System

An edge-level Computer Vision and Embedded Robotics system that tracks physical objects in real-time using Python (OpenCV) and maps their screen coordinates to physical angles on an Arduino Uno driving a Servo Motor over low-latency Serial communication.


![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?style=flat&logo=opencv)
![Arduino](https://img.shields.io/badge/Arduino-UNO-00979D?style=flat&logo=arduino)
![C++](https://img.shields.io/badge/C%2B%2B-Embedded-red?style=flat&logo=cplusplus)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)


📌 Features

* Real-Time Color Tracking: Utilizes HSV color space thresholding and morphological filtering (Erosion/Dilation) for stable object tracking.
* Low Latency Communication: Optimized Serial protocol running at 115200 Baud Rate for ultra-responsive hardware reaction.
* Noise Filtering & Optimization: Implements Gaussian Blur and threshold filtering (`ANGLE_THRESHOLD`) to prevent jitter and minimize redundant Serial writes.
* Hardware Abstraction: Safe fallback logic allowing the computer vision script to run offline if the Arduino board is disconnected.


🛠️ System Architecture & Workflow

[ Webcam Feed ] ──> [ OpenCV Frame Processing ] ──> [ Coordinate Mapping ]
│
(Serial @ 115200)
│
[ Servo Motor ] <─── [ Arduino Uno Execution ] <─────────────┘

1. Perception: Webcam captures video frames at $640 \times 480$ resolution.
2. Feature Extraction: Converts BGR to HSV color space, isolates target mask, and computes minimum enclosing circle centroid $(X, Y)$.
3. Kinematic Interpolation: Maps $X$-axis pixel coordinates ($0 \to \text{width}$) linearly to mechanical servo angles ($180^\circ \to 0^\circ$).
4. Hardware Control: Sends encoded target angles over UART to the Arduino Uno to actuate the physical Servo motor instantly.

💻 Hardware Components

| Component | Quantity | Notes |
| : | : | : |
| Arduino Uno | 1 | Microcontroller board |
| Servo Motor (SG90 / MG996R) | 1 | Connected to Pin D9 |
| USB Webcam | 1 | Standard 720p/1080p Web Camera |
| USB Type-A to B Cable | 1 | For PC-Arduino Serial connection |


🔌 Hardware Wiring Diagram

Arduino Uno                 Servo Motor
───────────                 ───────────
5V        ────────────►   VCC (Red)
GND       ────────────►   GND (Brown/Black)
Pin 9     ────────────►   Signal (Yellow/Orange)


🚀 Getting Started & Installation

 1. Prerequisites
        Ensure you have Python 3.8+ installed on your machine.

 2. Install Required Python Libraries
        Clone the repository and install dependencies:
        bash
        git clone [https://github.com/your-username/vision-guided-servo-tracker.git](https://github.com/your-username/vision-guided-servo-tracker.git)
        cd vision-guided-servo-tracker
        pip install opencv-python numpy pyserial


 3. Flash Arduino Firmware

    1. Open `servo_control.ino` using the Arduino IDE.
    2. Select your board (Arduino Uno) and the correct COM Port.
    3. Upload the code to the board.

 4. Run the Vision Tracking Script

Update the `COM` port in `Vision_Servo_Control.py` to match your system settings, then run:

bash
python main_tracker.py

📂 Repository Structure
.
├── servo_control.ino    # Firmware code for Arduino Uno (C++)
├── Vision_Servo_Control.py      # Vision processing & serial tracking script (Python)
├── README.md            # Project documentation
└── .gitignore           # Git ignore rules for Python & Arduino build files

📜 License
This project is open-source and available under the [MIT License]