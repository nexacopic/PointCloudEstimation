import cv2
import matplotlib.pyplot as plt
import numpy as np
import torch
import sys
import pointrendering
from vispy.color import *
import gc 
import pointman as pm
import numpy as np
import pandas as pd

from pyntcloud import PyntCloud



#model_type = "DPT_Large"     # MiDaS v3 - Large     (highest accuracy, slowest inference speed)
model_type = "DPT_Hybrid"   # MiDaS v3 - Hybrid    (medium accuracy, medium inference speed)
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
pm.CreatePointsFast(width/2, height/2, LiteralDepth, BeforeFrame)
pm.WinWidth = width
pm.WinHeight = height

print("Writing points")
cloud = PyntCloud(pd.DataFrame(
    # same arguments that you are passing to visualize_pcl
    data=np.hstack((pm.points, pm.colors)),
    columns=["x", "y", "z", "red", "green", "blue"])
)

cloud.to_file(sys.argv[2])
print("Done")

pm.BeginRendering()
# cv2.waitKey(1)
cv2.destroyAllWindows() 