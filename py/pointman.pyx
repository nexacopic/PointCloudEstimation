from vispy.color import *
import pointrendering
import numpy as np
cimport numpy as np
from cpython cimport array
import array
np.import_array()
def CreatePointsFast(int w, int h, np.ndarray LiteralDepth, np.ndarray BeforeFrame):
    # loop over the image, pixel by pixel
    for y in range(0, h):
        for x in range(0, w):
            CreatePoint((x, LiteralDepth[y, x] * 750, -y), ((BeforeFrame[(y)*2, (x)*2][0]/255, BeforeFrame[(y)*2, (x)*2][1]/255, BeforeFrame[(y)*2, (x)*2][2]/255)))


from vispy.color import *
cimport vispy
cimport vispy.color
import vispy.scene
from vispy.scene import visuals
points = []
colors = []
cdef int WinWidth = 0
cdef int WinHeight = 0
def CreatePoint(tuple point, tuple col) -> int:
    print("Creating point " + str(point))
    points.append(point)
    colors.append(col)
    return len(colors)

def MovePoint(int idx, tuple pos):
    points[idx] = pos
    ActualPoints[idx].position = pos

def BeginRendering():
    # canvas = vispy.scene.SceneCanvas(keys='interactive', show=True)
    # view = canvas.central_widget.add_view()
    # scatter = visuals.Markers()
    # print(np.array(points))
    # scatter.set_data(np.array(points), edge_width=0, face_color=(1, 1, 1, 1), size=10)
    # view.camera = 'arcball'
    # axis = visuals.XYZAxis(parent=view.scene)
    
    #
    # Make a canvas and add simple view
    #
    canvas = vispy.scene.SceneCanvas(keys='interactive', show=True)
    view = canvas.central_widget.add_view()
    symbols = np.full(len(points), 'o')
    scatter = visuals.Markers()
    scatter.antialias = 0
    scatter.set_data(np.array(points), edge_width=0, face_color=np.array(colors), size=10, symbol=symbols)

    view.add(scatter)

    view.camera = 'turntable'  # or try 'arcball'

    # add a colored 3D axis for orientation
    axis = visuals.XYZAxis(parent=view.scene)
    vispy.app.run()
    