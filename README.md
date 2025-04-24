# 🤚🔊 Hand Gesture Volume Control for Mac (and Windows)

Control your system volume using just your hand gestures through your webcam!  
This project uses computer vision to detect hand gestures and adjust the volume accordingly.

## 🚀 Features
- Adjust volume with simple hand gestures.
- Real-time gesture recognition using webcam.
- Built-in support for **macOS**.
- Optional support for **Windows** using `pypaw`.

## 🖥️ macOS: How to Run

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/gesture-volume-control.git
cd gesture-volume-control
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the main file:**

```bash
python volumeHandControl.py
```

That’s it! The script will activate your webcam, detect your hand gestures, and adjust the system volume accordingly.

## 🪟 Windows: How to Run

To run on Windows, you'll need to install [`pypaw`](https://pypi.org/project/pypaw/), a Python library for controlling system volume on Windows.

> ⚠️ Windows code is not included in this repository.  
> If you need the Windows-compatible version of this project, you can request it by emailing me:

📧 **pragyanadhikari961@gmail.com**

## 📆 Requirements

Dependencies are listed in the `requirements.txt` file and include:
- `opencv-python`
- `mediapipe`
- `pyobjc-framework-CoreAudio` (macOS only)
- `pypaw` (Windows only)

Install them with:

```bash
pip install -r requirements.txt
```

## 🧠 How It Works

This project uses:
- **OpenCV** for video capture and image processing.
- **Mediapipe** for hand tracking and gesture detection.
- System volume control libraries:
  - `pyobjc-framework-CoreAudio` on macOS.
  - `pypaw` on Windows.

The distance between the thumb and index finger determines the volume level dynamically.

## 📨 Contact

Have feedback, need help, or want the Windows version? Feel free to contact me:

**Pragyan Adhikari**  
📧 pragyanadhikari961@gmail.com

---

⭐ **Star this repo** if you like the project and want to support future improvements!

