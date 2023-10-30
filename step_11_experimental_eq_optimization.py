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
import matplotlib.pyplot as plt
import tensorflow as tf
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


#focal_send(focal_point[0], focal_point[1], focal_point[2])
#exit()

fy_fit_coef = np.array(pd.read_csv('numerical_simulated_results\\step_7_fyfzey_coeff.csv', header=None))[0]
fz_fit_coef = np.array(pd.read_csv('numerical_simulated_results\\step_7_fyfzez_coeff.csv', header=None))[0]

def fit_fy(te_y, te_z):
    return fy_fit_coef[0] + fy_fit_coef[1]*te_y + fy_fit_coef[2]*te_z

def fit_fz(te_y, te_z):
    return fz_fit_coef[0] + fz_fit_coef[1]*te_y + fz_fit_coef[2]*te_z + fz_fit_coef[3]*(te_y**2) + fz_fit_coef[4]*te_y*te_z

def loss_func():
    tf2a = f_e_temp.numpy()[0]
    print(tf2a)
    focal_send(tf2a[0],tf2a[1], tf2a[2])
    time.sleep(2.5)
    sim_y = fit_fy(f_e_temp[0][1], f_e_temp[0][2])
    sim_z = fit_fz(f_e_temp[0][1], f_e_temp[0][2])
    
    y, z, img= takepic_analyze()
    replaced_y = (sim_y + tf.stop_gradient(y - sim_y))
    replaced_z = (sim_z + tf.stop_gradient(z - sim_z))
    
    loss = tf.sqrt((target_point[1] - replaced_y)**2 + (target_point[2] - replaced_z)**2)
    loss_record.append(loss)
    return loss
    
#exit()

## Set input voltage to 12 V
focal_send(focal_point[0], focal_point[1], focal_point[2])

dropping_threshold = 25
phi = np.linspace(math.pi, 3*math.pi, 30)
phi = phi[0:len(phi)-1]
radius = 3e-3
mid_c = focal_point[2] + radius
cy = radius*np.sin(phi)
cz = radius*np.cos(phi) + mid_c

a_step = 1e-03
data_y = []
data_z = []
focal_opt_y = []
focal_opt_z = []

ll = 2 #number of attempt

for ii in range(len(phi)):
    target_point = [0.0, cy[ii], cz[ii]]
    if ii == 0:
        f_e_temp = tf.Variable([target_point])
    opt = tf.keras.optimizers.Adam(learning_rate=0.0005) #

    step_count = 0
    loss_record = []
    prev_f_e = f_e_temp
    while step_count < dropping_threshold:
        step_count = opt.minimize(loss_func, f_e_temp).numpy()
        delta_f = f_e_temp - prev_f_e
        # Define max-min move per step
        if tf.abs(delta_f[0][1])>a_step:
            f_e_temp[1] = prev_f_e[1] + a_step*tf.sign(delta_f[1])
        if tf.abs(delta_f[0][2])>a_step:
            f_e_temp[2] = prev_f_e[2] + a_step*tf.sign(delta_f[2])
        prev_f_e = f_e_temp
        
    y, z, img= takepic_analyze()
    data_y.append(y)
    data_z.append(z)
    
    focal_opt_y.append(f_e_temp[0][1].numpy())
    focal_opt_z.append(f_e_temp[0][2].numpy())
    cv.imwrite("experiment_data\\step_11_optimized_position_" + str(ii)  + "_N_" + str(ll) + "_img.jpg", img)
    np.savetxt("experiment_data\\step_11_optimize_record_" + str(ii) + "_N_" + str(ll) + "_loss.csv", loss_record, delimiter=",")
    
np.savetxt("experiment_data\\step_11_optimize_record_" + str(ii) + "_N_" + str(ll) + "_focal_opt_y.csv", focal_opt_y, delimiter=",")
np.savetxt("experiment_data\\step_11_optimize_record_" + str(ii) + "_N_" + str(ll) + "_focal_opt_z.csv", focal_opt_z, delimiter=",")
np.savetxt("experiment_data\\step_11_rec_y_N_" + str(ll) + "_data.csv", data_y, delimiter=",")
np.savetxt("experiment_data\\step_11_rec_z_N_" + str(ll) + "_data.csv", data_z, delimiter=",")