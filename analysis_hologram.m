clear all
close all
clc

k_list= {'i','ii','iii'};
n_list = 0:19;
target_amplitude = readmatrix(['numerical_simulated_results\step_2_target_amp_list.csv'])';
target_phase = readmatrix(['numerical_simulated_results\step_2_target_amp_list.csv'])';
delta_all = zeros(256*3, 20);
for ii = 1:20
    numerical_phase = readmatrix(['numerical_simulated_results\step2_target_Aiii_N_' num2str(ii-1) '_phase_export.csv'])';
    exp_try1_phase = readmatrix(['experiment_data\step4_optimize_match_target_Aiii_N_' num2str(ii-1) '_pat_phase_record_0_try.csv']);
    exp_try2_phase = readmatrix(['experiment_data\step4_optimize_match_target_Aiii_N_' num2str(ii-1) '_pat_phase_record_1_try.csv']);
    exp_try3_phase = readmatrix(['experiment_data\step4_optimize_match_target_Aiii_N_' num2str(ii-1) '_pat_phase_record_2_try.csv']);
    
    delta = zeros(256, 3);
    
    delta(:,1) = abs(wrapToPi(numerical_phase - exp_try1_phase));
    delta(:,2) = abs(wrapToPi(numerical_phase - exp_try2_phase));
    delta(:,3) = abs(wrapToPi(numerical_phase - exp_try3_phase));
    
    delta_all(:,ii) = delta(:);
    % std_delta = std(delta, [], 2).*(180/pi);
    % mean_delta = mean(delta, 2).*(180/pi);
    %
    % errorbar(1:256, mean_delta, std_delta,'x')
   
end
boxplot(delta_all.*(180/pi), target_phase)
xlabel('Target Phase [rad]')
ylabel('Phase Difference between Numerically Optimum - Experimentally Optimum [deg]')
% set(gca,'XScale','log')