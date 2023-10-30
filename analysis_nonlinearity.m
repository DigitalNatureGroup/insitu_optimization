clear all
close all
clc

k_list= {'i','ii','iii'};
n_list = 0:19;
target_amplitude = readmatrix(['numerical_simulated_results\step_2_target_amp_list.csv'])';
target_phase = readmatrix(['numerical_simulated_results\step_2_target_amp_list.csv'])';

for ii = 1:20
    fft_data = readcell(['experiment_data\step4_optimize_match_target_Aii_N_' num2str(ii-1) '_fft_data_record_0_try.csv'])';
    fft_data(1,:) = [];
    fft_data = cellfun(@(x) str2num(x), fft_data);
    fft_freq = readmatrix(['experiment_data\step4_optimize_match_target_Aii_N_' num2str(ii-1) '_fft_freq_record_0_try.csv'])';
    

    plot(fft_freq, abs(fft_data))
    
end
boxplot(delta_all.*(180/pi), target_phase)
xlabel('Target Phase [rad]')
ylabel('Phase Difference between Numerically Optimum - Experimentally Optimum [deg]')
% set(gca,'XScale','log')