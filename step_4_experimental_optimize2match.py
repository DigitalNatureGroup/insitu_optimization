from dataclasses import replace
import math
import numpy as np
import pandas as pd
import time
from pathlib import Path
import tensorflow as tf
from scipy.special import jv
import ctypes
import serial
import time
import os
import sys
import libtiepie
import matplotlib.pyplot as plt
from printinfo import *
from common_parameters import *
from init_handyscope import *
from functions4experiments import *
from datetime import datetime

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

def loss_func():
    part_A = Tr[0]
    trans_amplitude = tf.dtypes.complex(
        tf.cast(tf.ones(size), tf.float64), tf.cast(tf.zeros(size), tf.float64))
    trans_phase_copmlex = tf.dtypes.complex(
        tf.math.cos(part_A), tf.math.sin(part_A))

    phase = Tr[0].numpy()
    send_data(phase)
    # モデルの方を計算する
    point_Re = tf.reduce_sum(tf.math.real(trans_phase_copmlex) * tf.math.real(trans_amplitude* \
                             transducer_prop) - tf.math.imag(trans_phase_copmlex) * tf.math.imag(trans_amplitude*transducer_prop))
    point_Im = tf.reduce_sum(tf.math.real(trans_phase_copmlex) * tf.math.imag(trans_amplitude* \
                             transducer_prop) + tf.math.imag(trans_phase_copmlex) * tf.math.real(trans_amplitude*transducer_prop))
    point_amp = tf.math.sqrt(point_Re ** 2 + point_Im ** 2 )
    point_pha = tf.math.angle(tf.dtypes.complex(point_Re, point_Im))

    # 5.PICOからデータをGETする
    time_data, cap_data = get_data(scp)
    fourier_analyzed_data = tf.constant(t2f(time_data, cap_data, microphone_sensitivity, 2))
    capture_pha = fourier_analyzed_data[0]
    capture_amp = fourier_analyzed_data[1]

    capture_pha_record.append(capture_pha)
    capture_amp_record.append(capture_amp)
    
    replaced_pha = (point_pha + tf.stop_gradient(capture_pha - point_pha))
    replaced_amp = (point_amp + tf.stop_gradient(capture_amp - point_amp))

    if kk == 0:
        loss = (tf.math.cos(replaced_pha) - tf.math.cos(target_pha))**2 + (tf.math.sin(replaced_pha) - tf.math.sin(target_pha))**2
    elif kk == 1:
        loss = ((target_amp - replaced_amp)**2)
    elif kk == 2:
        loss = (replaced_amp*tf.math.cos(replaced_pha) - target_amp*tf.math.cos(target_pha))**2 + (replaced_amp*tf.math.sin(replaced_pha) - target_amp*tf.math.sin(target_pha))**2
    
    loss_record.append(loss)
    return loss

dropping_threshold = 100
transducer_prop = prop_matrix(tra_x, tra_y, tra_z, focal_point[0], focal_point[1], focal_point[2], P0, k, r0)

target_amplitude_list = tf.constant(np.genfromtxt('numerical_simulated_results\\step_2_target_amp_list.csv', delimiter=','))
target_phase_list = tf.constant(np.genfromtxt('numerical_simulated_results\\step_2_target_pha_list.csv', delimiter=','))
k_list = k_list = ['i', 'ii','iii']   

## Log Begin Time and Date
text_file = open("experiment_data\\step_4_experiment_begin_time.txt", "w")
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
text_file.write(dt_string)
text_file.close()

for ll in range(3):
    for kk in range(3):
        final_optimized_phase = []
        final_optimized_amplitude = []
        final_elapsed_time = []
        for ii in range(20):
            target_amp = target_amplitude_list[ii]
            target_pha = target_phase_list[ii]
            if kk == 0:
                print("Target Phase = " + str(target_pha))
            elif kk == 1:
                print("Target Amp = " + str(target_amp))
            elif kk == 2:
                print("Target Phase = " + str(target_pha))
                print("Target Amp = " + str(target_amp))
                
            init_solution = np.genfromtxt("numerical_simulated_results\\step2_target_A" + k_list[kk] + "_N_" + str(ii) + "_phase_export.csv", delimiter=',')
            st = time.time()
            Tr = tf.Variable([init_solution])
            opt = tf.keras.optimizers.Adam(learning_rate=0.05)
            step_count = 0
            loss_record = []
            capture_amp_record = []
            capture_pha_record = []
            
            while step_count < dropping_threshold:
                step_count = opt.minimize(loss_func, [Tr]).numpy()
            et = time.time()
            elapsed_time = et - st
            np.savetxt("experiment_data\\step4_optimize_match_target_A" + k_list[kk] + "_N_" + str(ii) + "_loss_record_" + str(ll) + "_try.csv", loss_record, delimiter=",")
            np.savetxt("experiment_data\\step4_optimize_match_target_A" + k_list[kk] + "_N_" + str(ii) + "_pat_phase_record_" + str(ll) + "_try.csv", Tr.numpy(), delimiter=",")

            time_data, data = get_data(scp)
            frequency_sp, fft_mic_half = t2f(time_data, data, microphone_sensitivity, 3)
            np.savetxt("experiment_data\\step4_optimize_match_target_A" + k_list[kk] + "_N_" + str(ii) + "_fft_freq_record_" + str(ll) + "_try.csv", frequency_sp, delimiter=",")
            np.savetxt("experiment_data\\step4_optimize_match_target_A" + k_list[kk] + "_N_" + str(ii) + "_fft_data_record_" + str(ll) + "_try.csv", fft_mic_half, delimiter=",")            
            temp_out = t2f(time_data, data, microphone_sensitivity, 2)
            final_optimized_phase.append(temp_out[0])
            final_optimized_amplitude.append(temp_out[1])
            final_elapsed_time.append(elapsed_time)
            
            if kk == 0:
                print("Optimized Phase = " + str(temp_out[0]))
            elif kk == 1:
                print("Optimized Amp = " + str(temp_out[1]))
            elif kk == 2:
                print("Optimized Phase = " + str(temp_out[0]))
                print("Optimized Amp = " + str(temp_out[1]))
                    
        np.savetxt("experiment_data\\step4_target_A" + k_list[kk] + "_optimized_final_amplitude_" + str(ll) + "_try.csv", final_optimized_amplitude, delimiter=",")
        np.savetxt("experiment_data\\step4_target_A" + k_list[kk] + "_optimized_final_phase_" + str(ll) + "_try.csv", final_optimized_phase, delimiter=",")
        np.savetxt("experiment_data\\step4_target_A" + k_list[kk] + "_optimized_final_elapsedtime_" + str(ll) + "_try.csv", final_elapsed_time, delimiter=",")