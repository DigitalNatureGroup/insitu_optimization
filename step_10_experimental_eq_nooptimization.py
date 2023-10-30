import math
import numpy as np
import pandas as pd
import datetime
import time
from pathlib import Path
from scipy.special import jv
import ctypes
import serial
import time
import os
import sys
import libtiepie
import matplotlib.pyplot as plt
from printinfo import *
from eq_common_parameters import *
from eq_functions4experiments import *
from datetime import datetime
import cv2 as cv
import pypuclib
from pypuclib import CameraFactory, Camera, XferData, Decoder
from pypuclib import Resolution, PUCException, PUC_DATA_MODE
from infini_cam_connect import *
from eq_calc_based_on_calib import *


## Set input voltage to 12 V
phi = np.linspace(math.pi, 3*math.pi, 30)
phi = phi[0:len(phi)-1]
radius = 3e-3
mid_c = focal_point[2] + radius
cy = radius*np.sin(phi)
cz = radius*np.cos(phi) + mid_c


for ll in range(3):
    data_y = []
    data_z = []
    for ii in range(len(phi)):
        target_point = [0.0, cy[ii], cz[ii]]
        f_e_temp = target_point
        
        focal_send(f_e_temp[0],f_e_temp[1], f_e_temp[2])
        time.sleep(2.5)
        
        y, z, img= takepic_analyze()
        
        data_y.append(y)
        data_z.append(z)
        cv.imwrite("experiment_data\\step_10_position_" + str(ii)  + "_N_" + str(ll) + "_img.jpg", img)

    np.savetxt("experiment_data\\step_10_rec_y_N_" + str(ll) + "_data.csv", data_y, delimiter=",")
    np.savetxt("experiment_data\\step_10_rec_z_N_" + str(ll) + "_data.csv", data_z, delimiter=",")