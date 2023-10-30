import math
import numpy as np
import pandas as pd
import datetime
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

k_list = k_list = ['i', 'ii','iii']   

## Log Begin Time and Date
text_file = open("experiment_data\\step_3_experiment_begin_time.txt", "w")
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
text_file.write(dt_string)
text_file.close()

for ll in range(3):
    for kk in range(3):
        experimental_measured_amp = []
        experimental_measured_pha = []
        for ii in range(20):
            phase = np.genfromtxt("numerical_simulated_results\\step2_target_A" + k_list[kk] + "_N_" + str(ii) + "_phase_export.csv", delimiter=',')
            send_data(phase)
            time.sleep(2)
            time_data, data = get_data(scp)
            temp_out = t2f(time_data, data, microphone_sensitivity, 2)
            experimental_measured_pha.append(temp_out[0])
            experimental_measured_amp.append(temp_out[1])
            
            frequency_sp, fft_mic_half = t2f(time_data, data, microphone_sensitivity, 3)
            np.savetxt("experiment_data\\step3_optimize_match_target_A" + k_list[kk] + "_N_" + str(ii) + "_fft_freq_record_" + str(ll) + "_try.csv", frequency_sp, delimiter=",")
            np.savetxt("experiment_data\\step3_optimize_match_target_A" + k_list[kk] + "_N_" + str(ii) + "_fft_data_record_" + str(ll) + "_try.csv", fft_mic_half, delimiter=",") 
        np.savetxt("experiment_data\\step3_compare_A" + k_list[kk] + "_numerical2experiment_amp_" + str(ll) + "_try.csv", experimental_measured_amp, delimiter=",")
        np.savetxt("experiment_data\\step3_compare_A" + k_list[kk] + "_numerical2experiment_pha_" + str(ll) + "_try.csv", experimental_measured_pha, delimiter=",")