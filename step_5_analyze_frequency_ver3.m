clear all
close all
clc

cd numerical_simulated_results
target_amp = table2array(readtable('step_2_target_amp_list.csv'));
cd ..
cd experiment_data\

thd_iii = zeros(3,20);
thd_ii = zeros(3,20);

t2_ii = zeros(3,20);
t2_iii = zeros(3,20);
t3_ii = zeros(3,20);
t3_iii = zeros(3,20);
t4_ii = zeros(3,20);
t4_iii = zeros(3,20);

for ii = 1:20
    for jj = 1:3
        amp_freq = table2array(readtable(['step3_optimize_match_target_Aiii_N_' num2str(ii-1) '_fft_freq_record_' num2str(jj-1) '_try.csv']));
        fileID = fopen(['step3_optimize_match_target_Aiii_N_' num2str(ii-1) '_fft_data_record_'  num2str(jj-1) '_try.csv']);
        data = textscan(fileID, '%s');
        data =data{1}(:);
        data = abs(cellfun(@(x)str2double(x(2:end-1)), data));
        
        [~,Idx] = max(data);
        freq_fundamental = amp_freq(Idx);

        f_1 = interpn(amp_freq, data, freq_fundamental);
        f_2 = interpn(amp_freq, data, 2*freq_fundamental);
        f_3 = interpn(amp_freq, data, 3*freq_fundamental);
        thd_iii(jj, ii) = sqrt(f_2.^2 +f_3.^2)/f_1;
        t2_iii(jj, ii) = f_2;
        t3_iii(jj,ii) = f_3;
%         t4_iii(jj,ii) = f_4;
        
        amp_freq = table2array(readtable(['step3_optimize_match_target_Aii_N_' num2str(ii-1) '_fft_freq_record_' num2str(jj-1) '_try.csv']));
        fileID = fopen(['step3_optimize_match_target_Aii_N_' num2str(ii-1) '_fft_data_record_'  num2str(jj-1) '_try.csv']);
        data = textscan(fileID, '%s');
        data =data{1}(:);
        data = abs(cellfun(@(x)str2double(x(2:end-1)), data));

        [~,Idx] = max(data);
        freq_fundamental = amp_freq(Idx);

        f_1 = interpn(amp_freq, data, freq_fundamental);
        f_2 = interpn(amp_freq, data, 2*freq_fundamental);
%         f_3 = interpn(amp_freq, data, 3*freq_fundamental);
        thd_ii(jj, ii) = sqrt(f_2.^2)/f_1;
        t2_ii(jj, ii) = f_2;
%         t3_ii(jj,ii) = f_3;
%         t4_ii(jj,ii) = f_4;
    end
end

a_i_per_pha_exp= zeros(20, 3);
a_ii_per_amp_exp= zeros(20, 3);
a_iii_per_pha_exp= zeros(20, 3);
a_iii_per_amp_exp= zeros(20, 3);
a_i_per_pha_exp_optimized= zeros(20, 3);
a_ii_per_amp_exp_optimized= zeros(20, 3);
a_iii_per_pha_exp_optimized= zeros(20, 3);
a_iii_per_amp_exp_optimized= zeros(20, 3);

for ii = 1:3
    a_ii_per_amp_exp_temp = table2array(readtable(['step3_compare_Aii_numerical2experiment_amp_' num2str(ii-1) '_try.csv']));
    a_iii_per_amp_exp_temp = table2array(readtable(['step3_compare_Aiii_numerical2experiment_amp_' num2str(ii-1) '_try.csv']));

    a_ii_per_amp_exp_optimized_temp = table2array(readtable(['step4_target_Aii_optimized_final_amplitude_' num2str(ii-1) '_try.csv']));
    a_iii_per_amp_exp_optimized_temp = table2array(readtable(['step4_target_Aiii_optimized_final_amplitude_' num2str(ii-1) '_try.csv']));

    a_ii_per_amp_exp(:,ii) = a_ii_per_amp_exp_temp;
    a_iii_per_amp_exp(:,ii) = a_iii_per_amp_exp_temp;

    a_ii_per_amp_exp_optimized(:,ii) = a_ii_per_amp_exp_optimized_temp;
    a_iii_per_amp_exp_optimized(:,ii) = a_iii_per_amp_exp_optimized_temp;
end
a_ii_per_amp_exp_mean = mean(a_ii_per_amp_exp, 2);
a_iii_per_amp_exp_mean = mean(a_iii_per_amp_exp, 2);

a_ii_per_amp_exp_optimized_mean = mean(a_ii_per_amp_exp_optimized, 2);
a_iii_per_amp_exp_optimized_mean = mean(a_iii_per_amp_exp_optimized, 2);

delta_ii = abs(a_ii_per_amp_exp_mean - target_amp);
delta_iii = abs(a_iii_per_amp_exp_mean - target_amp);

figure('units','centimeters','outerposition',[0 0 30 30])
hold on
errorbar(target_amp, mean(thd_ii,1).*100, std(thd_ii,1).*100, 'kx', 'LineWidth',2)
% errorbar(target_amp, mean(thd_iii,1).*100, std(thd_iii,1).*100, 'rx', 'LineWidth',2)
ylabel('Total Harmonic Distortion [%]')
xlabel('Target Amplitude [Pa]')
set(gca,'FontSize',24)
ylim([0 20])
grid on
grid minor
legend('Aii','Aiii')
exportgraphics(gcf,'G:\My Drive\tagami_hologram\testing_ver2\fig_gen\discussion_harmonic_distortion_ver3.png');

% figure('units','centimeters','outerposition',[0 0 30 30])
% hold on
% scatter(target_amp, delta_ii, 'LineWidth',2)
% scatter(target_amp, delta_iii, 'LineWidth',2)
% ylabel('Error (Target - Experiment)[Pa]')
% xlabel('Target Amplitude [Pa]')
% set(gca,'FontSize',24)
% % ylim([0 20])
% grid on
% grid minor
% legend('Aii','Aiii')
% exportgraphics(gcf,'G:\My Drive\tagami_hologram\testing_ver2\fig_gen\discussion_error.png');

figure('units','centimeters','outerposition',[0 0 30 30])
hold on
errorbar(target_amp, mean(t2_ii,1), std(t2_ii,1), 'ko', 'LineWidth',2)
errorbar(target_amp, mean(t2_iii,1), std(t2_iii,1), 'ro', 'LineWidth',2)
% errorbar(target_amp, mean(t3_ii,1), std(t3_ii,1), 'k+', 'LineWidth',2)
% errorbar(target_amp, mean(t3_iii,1), std(t3_iii,1), 'r+', 'LineWidth',2)
% scatter(target_amp, mean(t4_ii,1), 'k*', 'LineWidth',2)
% scatter(target_amp, mean(t4_iii,1), 'k*', 'LineWidth',2)
ylabel('Amplitude of Harmonics [Pa]')
xlabel('Target Amplitude [Pa]')
set(gca,'FontSize',24)
grid on
grid minor
ylim([0 160])
legend('F2 Aii','F2 Aiii', 'Location','best')
exportgraphics(gcf,'G:\My Drive\tagami_hologram\testing_ver2\fig_gen\discussion_second_harmonic_ver3.png');


