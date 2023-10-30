import math
from turtle import pd
import numpy as np
import pandas as pd
import cv2 as cv
import pypuclib
from pypuclib import CameraFactory, Camera, XferData, Decoder
from pypuclib import Resolution, PUCException, PUC_DATA_MODE
from infini_cam_connect import *

calibration_data = pd.read_csv('experiment_data\\step_9_calibrationdata.csv', header=None).T
y_offset_mm = calibration_data[0]
z_offset_mm = calibration_data[1]
y_offset_pix = calibration_data[2]
z_offset_pix = calibration_data[3]
pix2mm = calibration_data[4]
#[y_offset_mm, z_offset_mm, y_offset_pix, z_offset_pix, pix2mm]

def pix2coord(y_pix, z_pix):
    y = y_offset_mm + ((y_pix-y_offset_pix)*pix2mm)
    z = z_offset_mm + ((z_offset_pix-z_pix)*pix2mm)
    return y, z

def takepic_analyze():
    # Grab the single image data
    xferData = cam.grab()

    # Decode the data can be used as image
    array = decoder.decode(xferData)

    # Show the image
    #cv2.imshow("INFINICAM", array)
    color_img = cv.cvtColor(array,cv.COLOR_GRAY2BGR)
    circles_img = cv.HoughCircles(array,cv.HOUGH_GRADIENT,1,100,
                                param1=50,param2=30,minRadius=10,maxRadius=80)
    print(circles_img)
    circles_img = np.uint16(np.around(circles_img))[0,:]
    #print(circles_img)
    y_pix = circles_img[0,0] #in pixel
    z_pix = circles_img[0,1] #in pixel
    radius = circles_img[0,2] # pix
    y, z = pix2coord(y_pix, z_pix)
    
    
    return y, z, color_img