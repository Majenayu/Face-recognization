import cv2
import os
import numpy as np

# Directory containing your face images
dataset_path = "images_of_me"
recognizer = cv2.face.LBPHFaceRecognizer_create()
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

faces = []
labels = []
label_map = {}
current_label = 0

for filename in os.listdir(dataset_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        path = os.path.join(dataset_path, filename)
        gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        detected = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in detected:
            faces.append(gray[y:y+h, x:x+w])
            name = filename.split('_')[0]
            if name not in label_map:
                label_map[name] = current_label
                current_label += 1
            labels.append(label_map[name])

recognizer.train(faces, np.array(labels))
recognizer.save("trained_model.yml")
np.save("label_map.npy", label_map)
print("✅ Training complete! Model saved as 'trained_model.yml'.")
