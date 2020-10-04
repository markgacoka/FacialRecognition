# FaceRecognition
Highly Robust Facial Recognition Software in Python <br/>
* Structured application for training and testing face models as well as opening files and videos to detect and recognize faces.

## Dependencies:
* [OpenCV](https://docs.opencv.org/)
* [Time](https://docs.python.org/3/library/time.html) 
* [Numpy](https://docs.scipy.org/doc/numpy/reference/)

#### Install OpenCv Library
```
pip install opencv-python
```

If that does not wor, you can try installing the unofficial models from contributors

```
pip install opencv-contrib-python 
pip install --upgrade pip
```

#### File Directories on GitHub
```bash
|-- README.md
|-- LICENSE
|-- Media Manipulation
    |-- open_camera.py (Opens the camera)
    |-- open_image.py (Opens any image chosen)
    |-- open_video.py (Opens any video)
    |-- take_photo.py (Opens the camera and takes a photo)
    |-- take_video.py (Opens a video and takes a video until you cancel it)
|-- Detecing Faces
    |-- photo.JPG
    |-- facial_recognition.py
    |-- haarcascade_frontalface_default.xml
```

### PROJECT UNDERWAY:
* Finished drafting the UI and app flow
* Finished coding the subsystems for the full app

### TODO:
* Code the UI and connect the screens
* Add train feature in the software
* Compile to .exe
