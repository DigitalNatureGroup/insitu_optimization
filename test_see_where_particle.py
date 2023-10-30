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

system_mode = 0

if system_mode == 0:
## Set input voltage to 12 V
    focal_send(focal_point[0], focal_point[1], focal_point[2])
    print(focal_point)
else:
    y, z, img= takepic_analyze()
    print(z)

