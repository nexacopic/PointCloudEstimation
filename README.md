
# PointCloudEstimation

Estimates a point cloud from a single image/video


[![works on my machine badge](https://cdn.jsdelivr.net/gh/nikku/works-on-my-machine@v0.4.0/badge.svg)](https://github.com/nikku/works-on-my-machine)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
[![pytorch](https://img.shields.io/badge/PyTorch-1.6.0-EE4C2C.svg?style=flat&logo=pytorch)](https://pytorch.org)
[![tensorflow](https://img.shields.io/badge/TensorFlow-1.12-FF6F00.svg?style=flat&logo=tensorflow)](https://www.tensorflow.org)

## Features

- Generate depth maps from images/videos
- Create point clouds from images
- Animated point clouds (indev)



## Screenshots

![screen2](https://github.com/nexacopic/PointCloudEstimation/blob/readme/assets/screenshot2.png)
![screen1](https://github.com/nexacopic/PointCloudEstimation/blob/readme/assets/screenshot1.png)


## Installation

- Install [Python](https://www.python.org/downloads/)
- Run WindowsSetup.bat



    
## Usage

```batch
img2points.bat [image path] [output model] [depth bias] // depth bias of 2 or 1 is recomended (varies from scene to scene)
vid2points.bat [image.png] [points.ply] // does not work at the moment
```

