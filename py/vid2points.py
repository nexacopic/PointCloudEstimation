import os
import matplotlib
import cv2
import matplotlib.pyplot as plt
import numpy as np
import torch
import sys
import point3d
from PIL import Image


model_type = "DPT_Large"     # MiDaS v3 - Large     (highest accuracy, slowest inference speed)
#model_type = "DPT_Hybrid"   # MiDaS v3 - Hybrid    (medium accuracy, medium inference speed)
#model_type = "MiDaS_small"  # MiDaS v2.1 - Small   (lowest accuracy, highest inference speed)

print("Loading model " + model_type)
midas = torch.hub.load("intel-isl/MiDaS", model_type) # load model

print("Creating GPU Device")
# create gpu device and move model to the device (if available)
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
midas.to(device)
midas.eval()

print("Loading Transforms")
midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms") # load midas transforms to use on loaded images

if model_type == "DPT_Large" or model_type == "DPT_Hybrid":
    transform = midas_transforms.dpt_transform
else:
    transform = midas_transforms.small_transform

# define a video capture object 
vid = cv2.VideoCapture(sys.argv[1])

frame_idx = 0
while(vid.isOpened()): 
    frame_idx += 1
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 
    if(not ret):
        break
    
        # Display the resulting frame 
    cv2.imshow('Normal', frame) 
    BeforeFrame = frame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    height, width = frame.shape[:2]
    frame = cv2.resize(frame, ( int(width/2), int(height/2) ), interpolation= cv2.INTER_LINEAR)
    input_batch = transform(frame).to(device)

    with torch.no_grad():
        print("Estimating depth")
        prediction = midas(input_batch)
        prediction = torch.nn.functional.interpolate(
            prediction.unsqueeze(1),
            size=frame.shape[:2],
            mode="bicubic",
            align_corners=False,
        ).squeeze()

    print("Getting output")
    output = prediction.cpu().numpy()
    depth = output / output.max()
    cv2.imshow('Depth', depth) 
    LiteralDepth = 1 - depth
    cv2.imshow('Actual depth', LiteralDepth) 
    print("Writing to \"" + sys.argv[2] + "\\out\\depth_" + str(frame_idx) + ".png\"")
    cv2.imwrite(sys.argv[2] + "\\out\\depth_" + str(frame_idx) + ".png", LiteralDepth * 255)
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
os.system("ffmpeg -framerate " + str(vid.get(cv2.CAP_PROP_FPS)) + " -i depth_%d.png -c:v libx264 -r 30 depth.mp4")
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 


