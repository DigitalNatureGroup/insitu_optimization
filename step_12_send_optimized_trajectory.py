import math
import numpy as np
import pandas as pd
import datetime
import time
from pathlib import Path
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

system_mode = 1
fy = np.array(pd.read_csv('experiment_data\\step_11_optimize_record_28_N_2_focal_opt_y.csv', header=None)).T[0]
fz = np.array(pd.read_csv('experiment_data\\step_11_optimize_record_28_N_2_focal_opt_y.csv', header=None)).T[0]

if system_mode == 0:
## Set input voltage to 12 V
    focal_send(focal_point[0], focal_point[1], focal_point[2])
    print(focal_point)
else:
    for ll in range(10):
        for ii in range(len(fy)):
            focal_send(0.0, fy[ii], fz[ii])
            time.sleep(0.5)

