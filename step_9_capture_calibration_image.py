import cv2 as cv
import numpy as np
import pypuclib
from pypuclib import CameraFactory, Camera, XferData, Decoder
from pypuclib import Resolution, PUCException, PUC_DATA_MODE
from infini_cam_connect import *
from datetime import datetime
from eq_common_parameters import *
import time

## Log Begin Time and Date
text_file = open("experiment_data\\step_9_experiment_begin_time.txt", "w")
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
text_file.write(dt_string)
text_file.close()

y_offset_mm = 0.0
z_offset_mm = 0.120

while True:
    # Grab the single image data
    xferData = cam.grab()

    # Decode the data can be used as image
    array = decoder.decode(xferData)
    time.sleep(0.5)
    
    # Show the image
    #cv2.imshow("INFINICAM", array)
    color_img = cv.cvtColor(array,cv.COLOR_GRAY2BGR)
    circles_img = cv.HoughCircles(array,cv.HOUGH_GRADIENT,1,100,
                                param1=50,param2=30,minRadius=200,maxRadius=300)
    print(circles_img)
    circles_img = np.uint16(np.around(circles_img))

    for i in circles_img[0,:]:
        cv.circle(color_img,(i[0],i[1]),i[2],(0,255,0),2)
        cv.circle(color_img,(i[0],i[1]),2,(0,0,255),3)

    cv.imshow('Detected Circles',color_img)
    y_offset_pix = i[0] #in pixel
    z_offset_pix = i[1] #in pixel
    #print('Y offset ' + str(y_offset_pix))
    #print('Z offset ' + str(z_offset_pix))
    radius = i[2] # pix
    print('Z offset ' + str(radius))
    key = cv.waitKey(1)
    if key & 0xFF == 27: # Esc : quit application
        saveBMP(array)
        pix2mm = stylus_radius / radius # mm per pixel
        export_data = [y_offset_mm, z_offset_mm, y_offset_pix, z_offset_pix, pix2mm]
        np.savetxt("experiment_data\\step_9_calibrationdata.csv", export_data, delimiter=",")
        break

cv.destroyAllWindows()