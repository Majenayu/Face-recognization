# Face-recognization

A small Python/OpenCV webcam demo with two recognition pipelines:

1. `train_faces.py` trains an OpenCV LBPH recognizer from image files in
   `images_of_me/` and writes `trained_model.yml` plus `label_map.npy`.
2. `recognize_faces.py` loads those artifacts, reads webcam frames, detects
   faces with OpenCV's bundled Haar cascade, and labels predictions below a
   confidence threshold.
3. `face_recognition_video.py` uses the `face_recognition` library instead,
   encodes the images in `images_of_me/`, annotates webcam frames, and writes
   `output.mp4`.

## Requirements

There is no dependency manifest in this repository. Install compatible builds
of Python 3, NumPy, OpenCV with the `cv2.face` contrib module, and (for the
third script) `face_recognition`:

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install numpy opencv-contrib-python face_recognition
```

The scripts expect to be run from the repository root and require a working
camera/display for the interactive windows.

## Usage

```bash
python train_faces.py
python recognize_faces.py
python face_recognition_video.py
```

`train_faces.py` currently treats each filename prefix before `_` as a person
name; images are files directly inside `images_of_me/`, not per-person
subdirectories. Press `q` to stop the webcam loops.

## Repository layout

```text
train_faces.py             # LBPH training
recognize_faces.py         # OpenCV webcam recognition
face_recognition_video.py  # face_recognition webcam + MP4 writer
images_of_me/              # local training images
trained_model.yml          # serialized LBPH model
label_map.npy              # numeric label to name mapping
output.mp4                 # generated video artifact
CHANGELOG.md               # project history
```

## Accuracy, privacy, and limitations

The OpenCV script treats LBPH confidence values below 80 as recognized; this is
an application threshold, not a calibrated probability. The alternative
pipeline takes the first encoding returned for each image and assumes that
every file contains a detectable face. There is no liveness detection,
database, authentication, or consent workflow. Keep biometric images and
generated models private, obtain consent before collection, and do not use
this demo for high-impact identification decisions.

No automated test suite or deployment configuration is included.
