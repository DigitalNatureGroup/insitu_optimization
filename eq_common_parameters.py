import math
from turtle import pd
import numpy as np
import pandas as pd

focal_point = [0.0, 0.0, 0.119]
size = [256]
r0 = 0.005
voltage = 5 # 5V
P0 = (0.31001)*voltage
c0 = 346.0
l_ambda = c0 / 40000.0
k = 2.0*math.pi/l_ambda
phase_resolution = (2*math.pi)/32.0
board_id_1 = np.array([192], dtype='uint8')
board_id_2 = np.array([193], dtype='uint8')
comm_init = np.array([254], dtype='uint8')
comm_end = np.array([253], dtype='uint8')
microphone_sensitivity = 1.0 #mV/Pa
tra_x = pd.read_csv('trans_x_512.csv', header=None)
tra_y = pd.read_csv('trans_y_512.csv', header=None)
tra_z = pd.read_csv('trans_z_512.csv', header=None)

tra_x = tra_x.values.T[0][:512]
tra_y = tra_y.values.T[0][:512]
tra_z = tra_z.values.T[0][:512]
