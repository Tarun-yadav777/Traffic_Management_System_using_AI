# Traffic Management System using AI (Object Detection)

![Project Image](https://github.com/Tarun-yadav777/Traffic_Management_System_using_AI/blob/main/static/test1.PNG width="500" height=800")


> This is a ReadMe template to help save you time and effort.

---

### Table of Contents
You're sections headers will be used to reference location of destination.

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)
- [References](#demo)
- [License](#license)
- [Author Info](#author-info)

---

## Description

As the name suggest this is the GUI(Graphic User Interface ) application which can be used for traffic management system using AI specifically speaking Computer vision i.e object Detection.In this GUI application we can do Object Detection on Pictures,Videos and Video Camera plus Object Tracking on Video and Video Camera.
 

#### Technologies

- Computer Vision
- Object Detection
- Object Tracking
- Deep Sort
- YOLO (You Look Only Once)
- GUI Development
- PyQt5

[Back To The Top](#read-me-template)

---

## How To Use

#### Installation
1. Create a environment using either pip or conda and install all the required package using below mention commands.
2. OPTIONAL (If you using gpu tensorflow make sure you have updated drivers with supported cuddn library and cuda tool kit installed)
3. Download pre trained weights or train your own custom yolo notebook is shared for the same.
    YOLOv4 comes pre-trained and able to detect 80 classes. For easy demo purposes we will use the pre-trained weights.
    Download pre-trained yolov4.weights file: https://drive.google.com/open?id=1cewMfusmPjYWbrnuJRuKhPMwRe_b9PaT
    
    Copy and paste yolov4.weights from your downloads folder into the 'data' folder of this repository.

    If you want to use yolov4-tiny.weights, a smaller model that is faster at running detections but less accurate, download file here: https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights
4. You can run detection and tracking using command promt commands



#### API Reference

###### Environment Setup and Requirement Installation
##### Conda (Recommended)

```bash
# Tensorflow CPU
conda env create -f conda-cpu.yml
conda activate yolov4-cpu

# Tensorflow GPU
conda env create -f conda-gpu.yml
conda activate yolov4-gpu
```

##### Pip
```bash
# TensorFlow CPU
pip install -r requirements.txt

# TensorFlow GPU
pip install -r requirements-gpu.txt
```

###### Command for Promt Commands For running Object Detection and Object Tracking

```bash
# Convert darknet weights to tensorflow
## yolov4
python save_model.py --weights ./data/yolov4.weights --output ./checkpoints/yolov4-416 --input_size 416 --model yolov4 

# yolov4-tiny
python save_model.py --weights ./data/yolov4-tiny.weights --output ./checkpoints/yolov4-tiny-416 --input_size 416 --model yolov4 --tiny

# custom yolov4
python save_model.py --weights ./data/custom.weights --output ./checkpoints/custom-416 --input_size 416 --model yolov4 

# Run yolov4 tensorflow model
python detect.py --weights ./checkpoints/yolov4-416 --size 416 --model yolov4 --images ./data/images/kite.jpg

# Run yolov4-tiny tensorflow model
python detect.py --weights ./checkpoints/yolov4-tiny-416 --size 416 --model yolov4 --images ./data/images/kite.jpg --tiny

# Run custom yolov4 tensorflow model
python detect.py --weights ./checkpoints/custom-416 --size 416 --model yolov4 --images ./data/images/car.jpg

# Run yolov4 on video
python detect_video.py --weights ./checkpoints/yolov4-416 --size 416 --model yolov4 --video ./data/video/video.mp4 --output ./detections/results.avi

# Run custom yolov4 model on video
python detect_video.py --weights ./checkpoints/custom-416 --size 416 --model yolov4 --video ./data/video/cars.mp4 --output ./detections/results.avi

# Run yolov4 on webcam
python detect_video.py --weights ./checkpoints/yolov4-416 --size 416 --model yolov4 --video 0 --output ./detections/results.avi
```
[Back To The Top](#read-me-template)

---

## Demo 
- Picture of the Final GUI of Object Detection<br>

![Project Image](https://github.com/Tarun-yadav777/Traffic_Management_System_using_AI/blob/main/static/test1.PNG)

- Picture of GUI in action<br>

![Project Image](https://github.com/Tarun-yadav777/Traffic_Management_System_using_AI/blob/main/static/test2.PNG)

- Picture of Detection on pic

![Project Image](https://github.com/Tarun-yadav777/Traffic_Management_System_using_AI/blob/main/static/detectionpic.png)

- Detection on Video

![Project Image](https://github.com/Tarun-yadav777/Traffic_Management_System_using_AI/blob/main/static/detectionvid.gif)

- Tracking on Video

![Project Image](https://github.com/Tarun-yadav777/Traffic_Management_System_using_AI/blob/main/static/tracking.gif)

[Back To The Top](#read-me-template)

---


## References
[Back To The Top](#read-me-template)

---

## License

MIT License

Copyright (c) [2017] [James Q Quick]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#read-me-template)

---

## Author Info

- Twitter - [@taronic777](https://twitter.com/taronic777)
- LinkedIn - [Tarun Yadav](https://www.linkedin.com/in/tarun-yadav-47442112b/)

[Back To The Top](#read-me-template)
