print("Loading OpenCV")
import cv2
print("Loading NumPy")
import numpy as np
print("Loading PyTorch")
import torch
print("Loading sys")
import sys
print("Loading ViSpy")
from vispy.color import *
print("Loading GC")
import gc 
print("Loading PointMan")
import pointman as pm
print("Loading Pandas")
import pandas as pd

print("Loading PyntCloud")
from pyntcloud import PyntCloud


match (sys.argv[3]):
    case "0":
        print("Using gpulevel 0")
        model_type = "MiDaS_small"
    case "1":
        print("Using gpulevel 1")
        model_type = "DPT_Hybrid"
    case "2":
        print("Using gpulevel 2")
        model_type = "DPT_Large"
    case _:
        print("GPU Level can not be greater then 2!")
        exit()

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
    print("Using Large Transform")
    transform = midas_transforms.dpt_transform
else:
    print("Using Small Transform")
    transform = midas_transforms.small_transform

print("Loading image")
frame = cv2.imread(sys.argv[1])

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
del midas
del midas_transforms
gc.collect()
depth = output / output.max()
cv2.imshow('Depth', depth) 
LiteralDepth = 1 - depth
cv2.imshow('Literal Depth', LiteralDepth) 

h = height/2
w = width/2
BeforeFrame = cv2.cvtColor(BeforeFrame, cv2.COLOR_BGR2RGB)
pm.CreatePointsFast(width/2, height/2, LiteralDepth/int(sys.argv[3]), BeforeFrame)
pm.WinWidth = width
pm.WinHeight = height

print("Writing points")
cloud = PyntCloud(pd.DataFrame(
    # same arguments that you are passing to visualize_pcl
    data=np.hstack((pm.points, pm.colors)),
    columns=["x", "y", "z", "red", "green", "blue"])
)

cloud.to_file(sys.argv[2])
print("Saved Pointclound to \"" + sys.argv[2] + "\"")
print("Done")

pm.BeginRendering()
# cv2.waitKey(1)
cv2.destroyAllWindows() 