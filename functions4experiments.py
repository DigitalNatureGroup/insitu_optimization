import libtiepie
import numpy as np
import serial
import time
import math
from common_parameters import *

class ControlPat:
    def __init__(self, port, boudrate, timeout):
        self.ser = serial.Serial()
        self.ser.port = port
        self.ser.baudrate = boudrate
        self.ser.open()

    def output(self, values):
        self.ser.write(values)

def t2f(time_data, cap_data, microphone_sensitivity, options):
    frquency_of_interest = 40e3
    trig_signal = np.array(cap_data[0])
    mic_signal = (np.array(cap_data[1])*1000.0) / microphone_sensitivity # capdata measured in Volts. sensitivity in mV/Pa
    
    # Get full waves from trig data
    temp_trig = np.diff(np.sign(mic_signal))
    full_cycle_index = np.where(temp_trig==2.0)[0]
    number_of_cycles = 1000
    b_t = full_cycle_index[0]
    e_t = full_cycle_index[number_of_cycles]
    
    cut_t = time_data[b_t:e_t]
    cut_trig = trig_signal[b_t:e_t]
    cut_mic = mic_signal[b_t:e_t]
    
    #fig, ax = plt.subplots()
    #ax.plot(cut_t, cut_mic)
    #plt.show()
    # Calculate FFT
    fp = 1/(cut_t[-1]-cut_t[0])
    N = len(cut_t)
    frequency_sp = fp*np.arange(0, N-1)
    frequency_sp = frequency_sp[0:int(N/2)]
    
    fft_trig = np.fft.fft(cut_trig-np.mean(cut_trig), N) / N * 2
    fft_trig_half = fft_trig[0:int(N/2)]
    
    fft_mic = np.fft.fft(cut_mic, N) / N * 2
    fft_mic_half = fft_mic[0:int(N/2)]
    
    if options == 0: # Phase Only
        temp_out = np.angle(np.interp(frquency_of_interest, frequency_sp, fft_trig_half)) - np.angle(np.interp(frquency_of_interest, frequency_sp, fft_mic_half))
        return temp_out
    elif options == 1:  #Amplitude Only
        temp_out = np.interp(frquency_of_interest, frequency_sp, np.abs(fft_mic_half))
        return temp_out
    elif options == 2: # Phase and Amplitude
        temp_out = np.zeros(2)
        temp_out[0] = np.angle(np.interp(frquency_of_interest, frequency_sp, fft_trig_half)) - np.angle(np.interp(frquency_of_interest, frequency_sp, fft_mic_half))
        temp_out[1] = np.interp(frquency_of_interest, frequency_sp, np.abs(fft_mic_half))
        return temp_out
    elif options == 3: # Return fft results
        return frequency_sp, fft_mic_half

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

pat_controller = ControlPat(port='COM3', boudrate=230400, timeout=10)

def send_data(phase):
    phase = np.mod(phase, 2*math.pi)
    temp = np.round(phase / phase_resolution)  # if 32 is off singal
    temp = np.where(temp == 32, 0, temp)
    data = np.array(np.concatenate([comm_init, board_id_1, temp, comm_end]), dtype='uint8')
    values = data.tobytes()
    pat_controller.output(values=values)