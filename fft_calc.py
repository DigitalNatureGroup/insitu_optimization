# fft_calc.py
import numpy as np

def t2f(time_data, cap_data, microphone_sensitivity):
    frquency_of_interest = 40e3
    trig_signal = np.array(cap_data[0])
    mic_signal = (np.array(cap_data[1])*1000.0) / microphone_sensitivity # capdata measured in Volts. sensitivity in mV/Pa
    
    # Get full waves from trig data
    temp_trig = np.diff(np.sign(mic_signal))
    full_cycle_index = np.where(temp_trig==2.0)[0]
    number_of_cycles = 20
    b_t = full_cycle_index[0]+1
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
    
    return frequency_sp, fft_mic_half