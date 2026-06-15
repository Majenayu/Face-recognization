# 🎭 Face Recognition System

<div align="center">

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/Python-100%25-blue?style=flat-square)
![OpenCV](https://img.shields.io/badge/OpenCV-Face_Recognition-green)
![License](https://img.shields.io/badge/license-MIT-green)

**A real-time face recognition system using OpenCV and machine learning for accurate facial detection and identification**

[Report Bug](https://github.com/Majenayu/Face-recognization/issues) • [Request Feature](https://github.com/Majenayu/Face-recognization/issues)

</div>

---

## 📋 Project Information

**Project Name:** Face Recognition System  
**Developer:** P G AYUSH RAI (majen) - [@Majenayu](https://github.com/Majenayu)  
**Build Date:** 2024 (8 months ago)  
**Project Type:** Computer Vision Application  
**Version:** 1.0.0  
**Language:** Python 100%  

---

## 🎯 About The Project

This Face Recognition System is a comprehensive computer vision application that implements real-time facial detection and recognition using OpenCV and machine learning algorithms. The system can train on custom face datasets, recognize faces from images and video streams, and provide accurate identification with confidence scores.

### Key Features

✨ **Real-Time Face Detection** - Detect faces in live video streams or video files  
🎓 **Custom Training** - Train the model on your own face dataset  
🔍 **Face Recognition** - Identify and label recognized faces with confidence scores  
📹 **Video Processing** - Process video files and generate annotated output  
📸 **Image-Based Training** - Train using multiple images per person  
💾 **Model Persistence** - Save and load trained models for reuse  
🏷️ **Label Mapping** - Maintain mappings between face IDs and names  
📊 **Confidence Scoring** - Display recognition confidence for each detection  
⚡ **Fast Processing** - Optimized for real-time performance  
🔧 **Easy Configuration** - Simple setup and training process  

---

## 🛠️ Technologies Used

### Core Technologies
- **Python** - Primary programming language (100%)
- **OpenCV (cv2)** - Computer vision library for face detection and recognition
- **NumPy** - Numerical computing for array operations
- **LBPH Face Recognizer** - Local Binary Patterns Histograms algorithm

### Key Libraries
- **cv2.face.LBPHFaceRecognizer** - Face recognition algorithm
- **cv2.CascadeClassifier** - Haar Cascade for face detection
- **NumPy Arrays** - Efficient data handling and storage
- **Python File I/O** - Model and label persistence

---

## 📂 Project Structure

```
Face-recognization/
│
├── train_faces.py                # Train face recognition model
├── recognize_faces.py            # Recognize faces from images
├── face_recognition_video.py     # Real-time video face recognition
│
├── trained_model.yml             # Trained LBPH face recognizer model
├── label_map.npy                 # NumPy file mapping IDs to names
│
├── images_of_me/                 # Training dataset directory
│   ├── person1/                  # Individual person's images
│   ├── person2/
│   └── ...
│
└── output.mp4                    # Processed video with face annotations
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.7+**
- **pip** (Python package manager)
- **Webcam** (optional, for real-time detection)
- Basic understanding of computer vision concepts

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Majenayu/Face-recognization.git
   cd Face-recognization
   ```

2. **Install required packages**
   ```bash
   pip install opencv-python opencv-contrib-python numpy
   ```

3. **Download Haar Cascade file** (if not included)
   ```bash
   # The haarcascade_frontalface_default.xml file is typically included with OpenCV
   # If not, download from: https://github.com/opencv/opencv/tree/master/data/haarcascades
   ```

---

## 📱 How to Use

### Step 1: Prepare Training Data

Create a directory structure for your training images:

```
images_of_me/
├── person1/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── image3.jpg
├── person2/
│   ├── image1.jpg
│   └── image2.jpg
└── person3/
    └── image1.jpg
```

**Tips for best results:**
- Use 10-20 images per person
- Include different angles and lighting conditions
- Ensure faces are clearly visible
- Use consistent image quality

### Step 2: Train the Model

Run the training script to create your face recognition model:

```bash
python train_faces.py
```

**What happens:**
- Scans the `images_of_me/` directory
- Detects faces in each image
- Extracts facial features
- Trains the LBPH face recognizer
- Saves the model to `trained_model.yml`
- Creates label mapping in `label_map.npy`

**Output:**
```
Training on images in: images_of_me/
Processing: person1
Processing: person2
Processing: person3
Training complete!
Model saved to: trained_model.yml
Labels saved to: label_map.npy
```

### Step 3: Recognize Faces from Images

To recognize faces in a single image:

```bash
python recognize_faces.py
```

**Modify the script to specify your input image:**
```python
img = cv2.imread('test_image.jpg')
```

**Output:**
- Displays the image with bounding boxes around detected faces
- Shows the recognized person's name
- Displays confidence score for each detection

### Step 4: Real-Time Video Recognition

For live webcam recognition:

```bash
python face_recognition_video.py
```

**Or process a video file:**
```python
# Modify the script to use a video file instead of webcam
cap = cv2.VideoCapture('input_video.mp4')
```

**Controls:**
- Press **'q'** to quit the video stream
- Faces are detected and labeled in real-time
- Confidence scores displayed on each detection

---

## 🔧 Code Overview

### train_faces.py

**Purpose:** Train the face recognition model on your dataset

**Key Functions:**
```python
# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Create LBPH face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Train the model
recognizer.train(faces, np.array(labels))

# Save the trained model
recognizer.save('trained_model.yml')
np.save('label_map.npy', label_map)
```

### recognize_faces.py

**Purpose:** Recognize faces from static images

**Key Functions:**
```python
# Load trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trained_model.yml')

# Load label mapping
label_map = np.load('label_map.npy', allow_pickle=True).item()

# Recognize face
label, confidence = recognizer.predict(face_roi)
name = label_map[label]
```

### face_recognition_video.py

**Purpose:** Real-time face recognition from video streams

**Key Functions:**
```python
# Open video capture
cap = cv2.VideoCapture(0)  # 0 for webcam, or video file path

# Process each frame
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(face_roi)
        name = label_map.get(label, "Unknown")
        
        # Draw bounding box and label
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, f"{name} ({confidence:.2f})", (x, y-10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
```

---

## 🎓 How It Works

### 1. Face Detection (Haar Cascade)

The system uses Haar Cascade Classifiers to detect faces:
- **Trained on thousands of positive and negative images**
- **Fast and efficient for real-time detection**
- **Detects faces at various scales and positions**

### 2. Face Recognition (LBPH Algorithm)

**Local Binary Patterns Histograms (LBPH):**
- Divides face into small regions
- Extracts texture patterns from each region
- Creates a histogram of patterns
- Compares histograms to identify faces

**Advantages:**
- ✅ Robust to lighting variations
- ✅ Handles different facial expressions
- ✅ Fast computation
- ✅ Works with grayscale images

### 3. Training Process

```
Training Images → Face Detection → Feature Extraction → Model Training → Saved Model
```

1. **Load Images:** Read images from training directory
2. **Detect Faces:** Use Haar Cascade to locate faces
3. **Extract Features:** Convert faces to LBPH features
4. **Train Model:** Create associations between features and labels
5. **Save Model:** Persist model and label mappings

### 4. Recognition Process

```
Input Image/Video → Face Detection → Feature Extraction → Model Prediction → Label + Confidence
```

1. **Capture Frame:** Get image from webcam or file
2. **Detect Faces:** Locate faces in the frame
3. **Extract Features:** Process each detected face
4. **Predict:** Compare features with trained model
5. **Display Result:** Show name and confidence score

---

## 📊 Performance Metrics

### Accuracy Factors

**Confidence Score:**
- **0-50:** High confidence (excellent match)
- **50-80:** Medium confidence (good match)
- **80-100:** Low confidence (possible match)
- **>100:** Very low confidence (likely incorrect)

**Tips for Better Accuracy:**
- Use diverse training images (different angles, lighting)
- Train with at least 10-15 images per person
- Ensure good image quality
- Keep consistent distance from camera
- Use good lighting conditions

---

## 🔧 Configuration Options

### Haar Cascade Parameters

```python
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,    # Image scale reduction (1.1 = 10% reduction)
    minNeighbors=5,     # Minimum neighbors for detection (higher = stricter)
    minSize=(30, 30)    # Minimum face size to detect
)
```

### LBPH Parameters

```python
recognizer = cv2.face.LBPHFaceRecognizer_create(
    radius=1,           # Radius for LBPH
    neighbors=8,        # Number of sample points
    grid_x=8,           # Horizontal cells
    grid_y=8            # Vertical cells
)
```

---

## 💡 Use Cases

### Security Applications
- 🏢 **Office Access Control** - Unlock doors with face recognition
- 🏠 **Home Security** - Identify visitors and family members
- 🔐 **Device Authentication** - Secure login systems

### Educational Applications
- 🎓 **Attendance Systems** - Automated student attendance
- 📚 **Library Access** - Member identification
- 🏫 **Campus Security** - Monitor authorized personnel

### Commercial Applications
- 🛒 **Retail Analytics** - Customer recognition and preferences
- 🏨 **Hotel Check-in** - Contactless guest identification
- 💳 **Payment Systems** - Secure transaction verification

### Personal Projects
- 📸 **Photo Organization** - Auto-tag people in photos
- 🎮 **Interactive Games** - Face-controlled gaming
- 🤖 **Smart Home** - Personalized automation

---

## 🐛 Known Issues & Troubleshooting

### Common Issues

**1. "Module 'cv2' has no attribute 'face'"**
- **Solution:** Install opencv-contrib-python
  ```bash
  pip install opencv-contrib-python
  ```

**2. Low recognition accuracy**
- **Solution:** 
  - Add more training images (15-20 per person)
  - Improve lighting conditions
  - Ensure faces are clearly visible
  - Adjust Haar Cascade parameters

**3. Face not detected**
- **Solution:**
  - Check camera/image quality
  - Adjust `scaleFactor` and `minNeighbors`
  - Ensure adequate lighting
  - Face should be frontal and clearly visible

**4. Multiple false positives**
- **Solution:**
  - Increase `minNeighbors` parameter (5-7)
  - Increase `minSize` for face detection
  - Improve training dataset quality

---

## 🚀 Future Enhancements

### Planned Features
- [ ] Deep learning-based recognition (FaceNet, ArcFace)
- [ ] Multi-face tracking in videos
- [ ] Age and gender detection
- [ ] Emotion recognition
- [ ] Face mask detection
- [ ] 3D face recognition
- [ ] Mobile app integration
- [ ] Cloud-based recognition API
- [ ] Database integration for large-scale systems
- [ ] Real-time performance optimization
- [ ] GUI application with tkinter/PyQt
- [ ] REST API for remote recognition

### Potential Improvements
- [ ] Add data augmentation during training
- [ ] Implement face alignment preprocessing
- [ ] Support for multiple face recognition algorithms
- [ ] Add confidence threshold configuration
- [ ] Create web interface with Flask/Django
- [ ] Implement face clustering
- [ ] Add face spoofing detection
- [ ] Support for batch processing
- [ ] Generate recognition reports and analytics
- [ ] Export recognized faces to database

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is available under the MIT License. See the LICENSE file for details.

---

## 👤 Developer

**P G AYUSH RAI (majen)**

- GitHub: [@Majenayu](https://github.com/Majenayu)
- Repository: [Face-recognization](https://github.com/Majenayu/Face-recognization)
- Role: Lead Developer & Maintainer

---

## 🙏 Acknowledgments

- **OpenCV Community** - For excellent computer vision tools and documentation
- **Python Community** - For powerful libraries and support
- **Haar Cascade Contributors** - For pre-trained face detection models
- **Computer Vision Researchers** - For LBPH and other algorithms

---

## 📚 References & Resources

### Documentation
- [OpenCV Documentation](https://docs.opencv.org/)
- [OpenCV Face Recognition Tutorial](https://docs.opencv.org/master/da/d60/tutorial_face_main.html)
- [LBPH Face Recognizer](https://docs.opencv.org/master/df/d25/classcv_1_1face_1_1LBPHFaceRecognizer.html)

### Research Papers
- Ahonen, T., Hadid, A., & Pietikäinen, M. (2006). "Face Description with Local Binary Patterns"
- Viola, P., & Jones, M. (2001). "Rapid Object Detection using a Boosted Cascade"

### Additional Learning
- [Face Recognition Handbook](https://github.com/ageitgey/face_recognition)
- [Computer Vision Algorithms](https://opencv.org/)
- [Deep Learning for Face Recognition](https://www.pyimagesearch.com/)

---

## 📞 Support

For issues, questions, or suggestions:
- Open an [Issue](https://github.com/Majenayu/Face-recognization/issues)
- Contact: P G AYUSH RAI (majen) [@Majenayu](https://github.com/Majenayu)

---

## 📈 Version History

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

---

<div align="center">

**Made with ❤️ for Computer Vision Enthusiasts by P G AYUSH RAI (majen)**

⭐ Star this repository if you find it helpful!

**Detect** | **Recognize** | **Identify**

</div>
