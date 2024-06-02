
# PointCloudEstimation

Estimates a point cloud from a single image/video
(If you downloaded builds from the releases skip to [Usage](#usage))


[![works on my machine badge](https://cdn.jsdelivr.net/gh/nikku/works-on-my-machine@v0.4.0/badge.svg)](https://github.com/nikku/works-on-my-machine)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
[![pytorch](https://img.shields.io/badge/PyTorch-1.6.0-EE4C2C.svg?style=flat&logo=pytorch)](https://pytorch.org)

## Features

- Generate depth maps from images/videos
- Create point clouds from images
- Animated point clouds (indev)



## Screenshots

![screen2](https://github.com/nexacopic/PointCloudEstimation/blob/readme/assets/screenshot2.png)
![screen1](https://github.com/nexacopic/PointCloudEstimation/blob/readme/assets/screenshot1.png)


## Installation

- Install [Python](https://www.python.org/downloads/)
- During the Installer make sure to select these options in Advanced Options
- ![image](https://github.com/nexacopic/PointCloudEstimation/assets/142146272/5c9f5001-2073-4afd-9340-d9b7e3ba148b)
- Run InitialSetup.bat As Admin



    
## Usage

```batch
img2points.bat [image path] [output model] [depth bias] [gpulevel]
--> [image path]
--> [output model]
--> [depth bias] // depth bias of 2 or 1 is recomended (varies from scene to scene)
--> [gpulevel] // 0-2 (0 is for speed/low-end hardware,1 is recomended, 2 is for higher quality/high-end systems)

vid2points.bat [image.png] [points.ply] // does not work at the moment
```

