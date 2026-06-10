# 😊 Facial Expression Recognition System

> A Machine Learning-based Facial Expression Recognition System that detects human emotions from facial images using **Principal Component Analysis (PCA)** and **Support Vector Machine (SVM)** classification techniques.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-green)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-SVM-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 📌 Project Overview

Facial expressions are one of the most powerful forms of non-verbal communication. This project automatically identifies and classifies human emotions from facial images using machine learning techniques.

The system can detect emotions from:

* 📷 Uploaded Images
* 🎥 Live Webcam Feed

The application first detects a face using OpenCV's Haar Cascade Classifier, extracts features, applies PCA for dimensionality reduction, and finally predicts the emotion using a trained SVM model.

---

## ✨ Features

✅ Real-time emotion recognition using webcam

✅ Emotion prediction from uploaded images

✅ Face detection using Haar Cascade Classifier

✅ PCA-based feature extraction

✅ SVM-based emotion classification

✅ User-friendly GUI using Tkinter

✅ Automatic image preprocessing

✅ Seven emotion categories supported

---

## 🎭 Emotion Categories

The system can recognize the following emotions:

| Label | Emotion   |
| ----- | --------- |
| 😠    | Angry     |
| 🤢    | Disgusted |
| 😨    | Fearful   |
| 😄    | Happy     |
| 😐    | Neutral   |
| 😢    | Sad       |
| 😲    | Surprised |

---

## 🧠 Machine Learning Workflow

```text
Input Image
     │
     ▼
Face Detection (OpenCV)
     │
     ▼
Face Cropping
     │
     ▼
Resize to 32x32
     │
     ▼
Feature Extraction
     │
     ▼
PCA Transformation
     │
     ▼
SVM Classification
     │
     ▼
Predicted Emotion
```

---

## 📊 Dataset Information

The model was trained using a facial expression dataset containing:

* 📂 Total Images: **28,726**
* 🖼️ Image Size: **32 × 32 × 3**
* 🎭 Emotion Classes: **7**
* 📦 Format: NumPy Arrays (`.npy`)

Dataset Files:

```text
model/
├── X.txt.npy
└── Y.txt.npy
```

---

## 🛠️ Technology Stack

### Programming Language

* 🐍 Python

### Libraries & Frameworks

* OpenCV
* NumPy
* Scikit-Learn
* Tkinter
* Pillow
* Pickle

### Machine Learning Techniques

* Principal Component Analysis (PCA)
* Support Vector Machine (SVM)

---

## 📂 Project Structure

```text
FacialExpression_Recognization/
│
├── model/
│   ├── X.txt.npy
│   ├── Y.txt.npy
│   └── model.txt
│
├── screenshots/
│   ├── home.png
│   ├── upload.png
│   └── result.png
│
├── haarcascade_frontalface_default.xml
├── Main.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/facial-expression-recognition-system.git
```

```bash
cd facial-expression-recognition-system
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the Application

```bash
python Main.py
```

---

## 💻 Usage

### 📤 Upload Image

1. Launch the application.
2. Click on **Upload Image**.
3. Select a facial image.
4. The system detects the face and predicts the emotion.

### 🎥 Live Detection

1. Open the application.
2. Click on **Live Detection**.
3. Allow webcam access.
4. The detected emotion will be displayed in real time.

---

## 📸 Screenshots

### 🏠 Home Screen

![Home Screen](screenshots/home.png)

---

### 📤 Upload Image

![Upload Image](screenshots/upload.png)

---

### 🎯 Prediction Result

![Prediction Result](screenshots/result.png)

---

## ⚙️ Model Details

### PCA (Principal Component Analysis)

PCA is used to:

* Reduce dimensionality
* Remove redundant information
* Improve training efficiency
* Speed up prediction

### SVM (Support Vector Machine)

The final emotion classification is performed using a trained SVM model stored in:

```text
model/model.txt
```

SVM was chosen because of its effectiveness in handling high-dimensional image data and classification tasks.

---

## 🎯 Applications

* 🤖 Human-Computer Interaction
* 🏥 Healthcare Monitoring
* 🎓 Smart Learning Systems
* 🛡️ Surveillance Systems
* 📈 Customer Sentiment Analysis
* 🧠 Emotion-Aware Applications

---

## 🔮 Future Enhancements

* Deep Learning-based CNN Models
* Higher Accuracy Emotion Recognition
* Multi-Face Detection
* Mobile Application Support
* Real-Time Analytics Dashboard
* FER2013 Dataset Integration
* Cloud Deployment

---

## ⚠️ Limitations

* Performance may vary under poor lighting conditions.
* Best suited for frontal face images.
* Traditional machine learning models may be less accurate than modern deep learning approaches.
* Emotion recognition can be affected by image quality and facial occlusions.

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a Pull Request

---

## 👨‍💻 Author

**SUSHANTH BANDARUPALLI**

📧 Email: [sushanthbandarupalli4444@gmail.com](mailto:sushanthbandarupalli4444@gmail.com)

💼 LinkedIn: [https://linkedin.com/in/sushanth](https://www.linkedin.com/in/sushanth-bandarupalli-18019b259/)

🐙 GitHub: [https://github.com/sushanthbandarupalli](https://github.com/sushanthbandarupalli)

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.

---

## 📜 License

This project is intended for educational and research purposes.
