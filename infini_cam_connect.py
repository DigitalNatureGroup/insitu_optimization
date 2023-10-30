import pypuclib
from pypuclib import CameraFactory, Camera, XferData, Decoder
from pypuclib import Resolution, PUCException, PUC_DATA_MODE
import cv2 as cv

stylus_radius = 4e-03 # it's an 8 mm diameter Renishaw A-5000-7557

# To connect the camera first detected
cam = CameraFactory().create()
cam.setFramerateShutter(250,250)
# Set filepath to save image
savePath = "experiment_data\\calibrating_image.png"
# To decode image, get decoder obj from camera
decoder = cam.decoder()
# Function : Save single image as BMP 
def saveBMP(img):
    cv.imwrite(savePath, img)
    print("saved a PNG image")
    