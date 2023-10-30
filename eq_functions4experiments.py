import numpy as np
import serial
import time
import math
from eq_common_parameters import *

class ControlPat:
    def __init__(self, port, boudrate, timeout):
        self.ser = serial.Serial()
        self.ser.port = port
        self.ser.baudrate = boudrate
        self.ser.open()

    def output(self, values):
        self.ser.write(values)

def get_data(scp):
    # Start measurement:
    scp.start()

    # Wait for measurement to complete:
    while not scp.is_data_ready:
        time.sleep(0.01)  # 10 ms delay, to save CPU time

    # Get data:
    data = scp.get_data()
    time_data = np.array(np.arange(0,len(data[1]))) / scp._get_sample_frequency() 
    return time_data, data

pat_controller = ControlPat(port='COM4', boudrate=230400, timeout=10)

def send_data(phase):
    phase = np.mod(phase, 2*math.pi)
    temp = np.round(phase / phase_resolution)  # if 32 is off singal
    temp = np.where(temp == 32, 0, temp)
    data = np.array(np.concatenate([comm_init, board_id_1, temp[0:256], board_id_2, temp[256:512], comm_end]), dtype='uint8')
    values = data.tobytes()
    pat_controller.output(values=values)
    
def focal_send(fx, fy, fz):
    focal_phi = -((2*math.pi*40e03)/c0)*(np.sqrt((fx-tra_x)**2+(fy-tra_y)**2+(fz-tra_z)**2) - np.sqrt(fx**2 + fy**2 + fz**2))
    focal_phi = np.where(tra_z >0.01, focal_phi + math.pi, focal_phi)
    send_data(focal_phi)
    