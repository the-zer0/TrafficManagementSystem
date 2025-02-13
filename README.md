📌 **AI-Powered Smart Traffic Management System** 

🚦 Traffic Management System is an AI-powered traffic management system that uses YOLOv8 for real-time vehicle detection and EasyOCR for license plate recognition. It intelligently  controls traffic signals based on vehicle density, improving traffic flow and reducing congestion.

🔥 **Features**
🚗 Real-time vehicle detection using YOLOv8
🔍 License plate recognition using EasyOCR
🚦 Smart traffic light control based on vehicle count
🎥 Supports live webcam feed & video input
🖼️ Saves processed frames for analysis

🛠️ **Technologies Used**
-- Python
-- YOLOv8 (Ultralytics) - Object detection
-- OpenCV - Image processing
-- EasyOCR - License plate recognition
-- Matplotlib - Frame visualization

🚀 **Installation & Setup**
1️⃣ Install Dependencies
  -> pip install ultralytics opencv-python easyocr matplotlib
2️⃣ Clone the Repository
  -> git clone https://github.com/the-zer0/TrafficManagementSystem.git
  -> cd TrafficManagementSystem
3️⃣ Run the Project
  Option 1: Use Webcam
    -> python traffic_management.py --source 0
  Option 2: Use a Video File
    -> python traffic_management.py --source traffic_video.mp4

🎯 **How It Works**
1️⃣ Detects vehicles using YOLOv8
2️⃣ Counts vehicles in the frame
3️⃣ Adjusts traffic light:

Green if traffic is heavy
Yellow for moderate traffic
Red for low traffic
4️⃣ Recognizes license plates (optional)

🏗️ **Future Improvements**
📡 Cloud-based real-time monitoring
🚦 Integration with smart city IoT systems
🧠 AI-powered traffic prediction
🎯 Issuance of challans

✨ **Connect with Me**
📧 Email: manomannem.2346@gmail.com
🔗 LinkedIn: linkedin.com/in/mannem-manobharath-771a18183
💻 GitHub: github.com/the-zer0
