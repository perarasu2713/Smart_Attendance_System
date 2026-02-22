<h1 align="center">🎓 AI Smart Attendance System</h1>

<p align="center">
  🚀 Real-Time Face Recognition Based Attendance System  
  💡 Built Using Deep Learning & Computer Vision  
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv"/>
  <img src="https://img.shields.io/badge/Deep%20Learning-Face%20Recognition-red?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge"/>
</p>

---

## 📌 Project Overview

This project is an **AI-powered Smart Attendance System** that uses **Face Recognition Technology** to automatically detect and mark attendance in real-time.

It captures live video from a webcam, recognizes faces using deep learning embeddings, and stores attendance with date & time in a CSV file.

---

## ✨ Features

✅ Real-Time Face Detection  
✅ Deep Learning Face Recognition  
✅ Confidence Score Display  
✅ Unknown Person Detection  
✅ Automatic Attendance Logging  
✅ Professional UI Bounding Boxes  
✅ Git Version Controlled  

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| 🐍 Python | Core Programming |
| 👁 OpenCV | Face Detection & Video Processing |
| 🧠 face_recognition (dlib CNN) | Face Encoding |
| 📊 NumPy | Mathematical Computation |
| 🗂 Git & GitHub | Version Control |

---

## 📂 Project Structure

```
Smart_Attendance_System/
│
├── dataset/              # Known face images
├── main.py               # Main Application File
├── attendance.csv        # Attendance Log
├── requirements.txt      # Required Libraries
├── README.md             # Project Documentation
└── .gitignore            # Ignored Files
```

---

## 🚀 How To Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/perarasu2713/Smart_Attendance_System.git
```

### 2️⃣ Navigate to Project Folder

```bash
cd Smart_Attendance_System
```

### 3️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python main.py
```

Press **ENTER** to exit the camera window.

---

## 🧠 How It Works

1. Images from the dataset are encoded into 128-d facial embeddings.
2. Live webcam feed captures faces.
3. Face distance is calculated using Euclidean metric.
4. If distance < threshold → Recognized.
5. Attendance is logged with timestamp.

---

## 📸 Sample Output

🟢 Recognized Face → Green Box + Confidence %  
🔴 Unknown Face → Red Box  

---

## 🎯 Project Objective

To automate the traditional attendance system using Artificial Intelligence, reducing manual errors and improving efficiency.

---

## 📈 Future Enhancements

🔹 GUI Dashboard  
🔹 Database Integration (MySQL)  
🔹 Cloud Deployment  
🔹 Mask Detection Integration  
🔹 Web-Based Version  

---

## 👨‍💻 Developed By

**Arasu (PERARASU M)**  
🚀 Passionate Python & AI Developer  

---

<p align="center">
  ⭐ If you like this project, give it a star on GitHub!
</p>
