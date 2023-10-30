import math
import numpy as np
import pandas as pd
import datetime
import time
from pathlib import Path
import tensorflow as tf
from scipy.special import jv
import ctypes
import time
import os
import sys
import matplotlib.pyplot as plt
from common_parameters import *

def prop_matrix(array_x, array_y, array_z, x_p, y_p, z_p, P0, k, r0):
    prop = []
    dist_map = np.sqrt(np.power((array_x - x_p), 2) + np.power((array_y - y_p), 2) + np.power((array_z - z_p), 2) )

    sin_alpha_map = np.sqrt((np.power((array_x - x_p), 2) + np.power((array_y - y_p), 2)) ) / dist_map
    sin_alpha_map = np.where(
        sin_alpha_map == 0, np.finfo(float).tiny, sin_alpha_map)

    amplitude_map = (2 * jv(1, k*r0*sin_alpha_map) * P0 / (k*r0*(sin_alpha_map)*dist_map) )

    prop.append(tf.dtypes.complex( amplitude_map * tf.math.cos(k*dist_map), amplitude_map * tf.math.sin(k*dist_map) ).numpy() )

    prop = np.array(prop)
    prop = tf.constant(prop, shape=prop.shape)

    return prop


def performance_calc():
    part_A = Tr[0]
    trans_amplitude = tf.dtypes.complex(
        tf.cast(tf.ones(size), tf.float64), tf.cast(tf.zeros(size), tf.float64))
    trans_phase_copmlex = tf.dtypes.complex(
        tf.math.cos(part_A), tf.math.sin(part_A))

    # モデルの方を計算する
    point_Re = tf.reduce_sum(tf.math.real(trans_phase_copmlex) * tf.math.real(trans_amplitude* \
                             transducer_prop) - tf.math.imag(trans_phase_copmlex) * tf.math.imag(trans_amplitude*transducer_prop))
    point_Im = tf.reduce_sum(tf.math.real(trans_phase_copmlex) * tf.math.imag(trans_amplitude* \
                             transducer_prop) + tf.math.imag(trans_phase_copmlex) * tf.math.real(trans_amplitude*transducer_prop))
    point_amp = tf.math.sqrt(point_Re ** 2 + point_Im ** 2 )
    point_phase = tf.math.angle(tf.dtypes.complex(point_Re, point_Im))
    return point_amp, point_phase

def loss_func():
    point_amp, point_phase = performance_calc()
    
    loss = - (point_amp**2)
    return loss

def loss_func_with_target_A():
    point_amp, point_phase = performance_calc()

    if kk == 0:
        loss = (tf.math.cos(point_phase) - tf.math.cos(target_pha))**2 + (tf.math.sin(point_phase) - tf.math.sin(target_pha))**2
    elif kk == 1:
        loss = ((target_amp - point_amp)**2)
    elif kk == 2:
        loss = (point_amp*tf.math.cos(point_phase) - target_amp*tf.math.cos(target_pha))**2 + (point_amp*tf.math.sin(point_phase) - target_amp*tf.math.sin(target_pha))**2
    return loss


dropping_threshold = 250
transducer_prop = prop_matrix(tra_x, tra_y, tra_z, focal_point[0], focal_point[1], focal_point[2], P0, k, r0)

Tr_A = np.zeros(size)
Tr = tf.Variable([Tr_A])

opt = tf.keras.optimizers.Adam(learning_rate=0.05)

# Calculate maximum pressure with single focus
step_count = 0
loss_record = []
while step_count < dropping_threshold:
    step_count = opt.minimize(loss_func, [Tr]).numpy()
    loss_record.append(loss_func().numpy())

max_amp, point_phase = performance_calc()
max_amp = max_amp.numpy()
print(max_amp)
#create target amplitude lists
target_amp_list = np.linspace(0.1, 0.9, 20)*max_amp
np.savetxt("numerical_simulated_results\step_2_target_amp_list.csv", target_amp_list, delimiter=",")
target_pha_list = np.linspace(0,2*math.pi, 20)
np.savetxt("numerical_simulated_results\step_2_target_pha_list.csv", target_pha_list, delimiter=",")

k_list = ['i', 'ii','iii']   
for kk in range(3):
    simulated_results_amplitude = []
    simulated_results_phase = []
    for ii in range(len(target_amp_list)):
        target_amp = target_amp_list[ii]
        target_pha = target_pha_list[ii]

        Tr_A = np.zeros(size)
        Tr = tf.Variable([Tr_A])
        opt = tf.keras.optimizers.Adam(learning_rate=0.05)
        step_count = 0
        loss_record = []
        while step_count < dropping_threshold:
            step_count = opt.minimize(loss_func_with_target_A, [Tr]).numpy()
            loss_record.append(loss_func_with_target_A().numpy())
        point_amp, point_phase = performance_calc()
        simulated_results_amplitude.append(point_amp.numpy())
        simulated_results_phase.append(point_phase.numpy())
        np.savetxt("numerical_simulated_results\\step2_target_A" + k_list[kk] + "_N_" + str(ii) + "_phase_export.csv", Tr.numpy()[0], delimiter=",")
    np.savetxt("numerical_simulated_results\step_2_target_A" + k_list[kk] + "_performance_amp.csv", simulated_results_amplitude, delimiter=",")
    np.savetxt("numerical_simulated_results\step_2_target_A" + k_list[kk] + "_performance_pha.csv", simulated_results_phase, delimiter=",")

