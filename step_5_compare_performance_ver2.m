clear all
close all
clc

cd numerical_simulated_results\

target_amp = table2array(readtable('step_2_target_amp_list.csv'));
target_pha = wrapToPi(table2array(readtable('step_2_target_pha_list.csv')));
target_index = 1:20;

a_i_per_pha = table2array(readtable('step_2_target_Ai_performance_pha.csv'));
a_ii_per_amp = table2array(readtable('step_2_target_Aii_performance_amp.csv'));
a_iii_per_pha = table2array(readtable('step_2_target_Aiii_performance_pha.csv'));
a_iii_per_amp = table2array(readtable('step_2_target_Aiii_performance_amp.csv'));
cd ..
cd experiment_data\

a_i_per_pha_exp= zeros(20, 3);
a_ii_per_amp_exp= zeros(20, 3);
a_iii_per_pha_exp= zeros(20, 3);
a_iii_per_amp_exp= zeros(20, 3);
a_i_per_pha_exp_optimized= zeros(20, 3);
a_ii_per_amp_exp_optimized= zeros(20, 3);
a_iii_per_pha_exp_optimized= zeros(20, 3);
a_iii_per_amp_exp_optimized= zeros(20, 3);

for ii = 1:3
    a_i_per_pha_exp_temp = table2array(readtable(['step3_compare_Ai_numerical2experiment_pha_' num2str(ii-1) '_try.csv']));
    a_ii_per_amp_exp_temp = table2array(readtable(['step3_compare_Aii_numerical2experiment_amp_' num2str(ii-1) '_try.csv']));
    a_iii_per_pha_exp_temp = table2array(readtable(['step3_compare_Aiii_numerical2experiment_pha_' num2str(ii-1) '_try.csv']));
    a_iii_per_amp_exp_temp = table2array(readtable(['step3_compare_Aiii_numerical2experiment_amp_' num2str(ii-1) '_try.csv']));

    a_i_per_pha_exp_temp = wrapToPi(a_i_per_pha_exp_temp - a_i_per_pha_exp_temp(1));
    a_iii_per_pha_exp_temp = wrapToPi(a_iii_per_pha_exp_temp - a_iii_per_pha_exp_temp(1));

    a_i_per_pha_exp_optimized_temp = wrapToPi(table2array(readtable(['step4_target_Ai_optimized_final_phase_' num2str(ii-1) '_try.csv'])));
    a_ii_per_amp_exp_optimized_temp = table2array(readtable(['step4_target_Aii_optimized_final_amplitude_' num2str(ii-1) '_try.csv']));
    a_iii_per_pha_exp_optimized_temp = wrapToPi(table2array(readtable(['step4_target_Aiii_optimized_final_phase_' num2str(ii-1) '_try.csv'])));
    a_iii_per_amp_exp_optimized_temp = table2array(readtable(['step4_target_Aiii_optimized_final_amplitude_' num2str(ii-1) '_try.csv']));

    a_i_per_pha_exp(:,ii) = a_i_per_pha_exp_temp;
    a_ii_per_amp_exp(:,ii) = a_ii_per_amp_exp_temp;
    a_iii_per_pha_exp(:,ii) = a_iii_per_pha_exp_temp;
    a_iii_per_amp_exp(:,ii) = a_iii_per_amp_exp_temp;

    a_i_per_pha_exp_optimized(:,ii) = a_i_per_pha_exp_optimized_temp;
    a_ii_per_amp_exp_optimized(:,ii) = a_ii_per_amp_exp_optimized_temp;
    a_iii_per_pha_exp_optimized(:,ii) = a_iii_per_pha_exp_optimized_temp;
    a_iii_per_amp_exp_optimized(:,ii) = a_iii_per_amp_exp_optimized_temp;
end
a_i_per_pha_exp_mean = atan2(mean(sin(a_i_per_pha_exp),2), mean(cos(a_i_per_pha_exp),2));
a_ii_per_amp_exp_mean = mean(a_ii_per_amp_exp, 2);
a_iii_per_pha_exp_mean = atan2(mean(sin(a_iii_per_pha_exp),2), mean(cos(a_iii_per_pha_exp),2));
a_iii_per_amp_exp_mean = mean(a_iii_per_amp_exp, 2);

a_i_per_pha_exp_optimized_mean = atan2(mean(sin(a_i_per_pha_exp_optimized),2), mean(cos(a_i_per_pha_exp_optimized),2));
a_ii_per_amp_exp_optimized_mean = mean(a_ii_per_amp_exp_optimized, 2);
a_iii_per_pha_exp_optimized_mean = atan2(mean(sin(a_iii_per_pha_exp_optimized),2), mean(cos(a_iii_per_pha_exp_optimized),2));
a_iii_per_amp_exp_optimized_mean = mean(a_iii_per_amp_exp_optimized, 2);

a_i_per_pha_exp_std = std(a_i_per_pha_exp, [], 2);
a_ii_per_amp_exp_std = std(a_ii_per_amp_exp, [], 2);
a_iii_per_pha_exp_std = std(a_iii_per_pha_exp, [], 2);
a_iii_per_amp_exp_std = std(a_iii_per_amp_exp, [], 2);

a_i_per_pha_exp_optimized_std = std(a_i_per_pha_exp_optimized, [], 2);
a_ii_per_amp_exp_optimized_std = std(a_ii_per_amp_exp_optimized, [], 2);
a_iii_per_pha_exp_optimized_std = std(a_iii_per_pha_exp_optimized, [], 2);
a_iii_per_amp_exp_optimized_std = std(a_iii_per_amp_exp_optimized, [], 2);

line_width = 5;
fontsize = 30;
%% A-i
figure('units','centimeters','outerposition',[0 0 30 30])
hold on
plot(target_index, target_pha,'k-','LineWidth',line_width)
scatter(target_index, a_i_per_pha, 250, 'rx','LineWidth',line_width)
errorbar(target_index, a_i_per_pha_exp_mean,a_i_per_pha_exp_std,'b-','LineWidth',line_width)
errorbar(target_index, a_i_per_pha_exp_optimized_mean, a_i_per_pha_exp_optimized_std,'g--','LineWidth',line_width)
% title('Phase A-i')
xlabel('Sample [-]')
ylabel('Phase [rad]')
set(gca,'FontSize', fontsize)
grid on
grid minor
legend('Target','Simulated','Exp (w/o opt)','Exp (w opt)')
set(gca,'Position',[0.1300 0.1100 0.7750 0.8150])
exportgraphics(gcf,'G:\My Drive\tagami_hologram\testing_ver2\fig_gen\A_i.pdf', 'ContentType', 'vector');
exportgraphics(gcf,'G:\My Drive\tagami_hologram\testing_ver2\fig_gen\A_i.png');
clf
hold on
plot(target_index, target_amp,'k-','LineWidth',line_width)
scatter(target_index, a_ii_per_amp,250, 'rx','LineWidth',line_width)
errorbar(target_index, a_ii_per_amp_exp_mean,a_ii_per_amp_exp_std,'b-','LineWidth',line_width)
errorbar(target_index, a_ii_per_amp_exp_optimized_mean,a_ii_per_amp_exp_optimized_std,'g--','LineWidth',line_width)
% title('Amp A-ii')
xlabel('Sample [-]')
ylabel('Pressure [Pa]')
set(gca,'FontSize', fontsize)
grid on
grid minor
% legend('Target','Simulated','Exp (w/o opt)','Exp (w opt)')
set(gca,'Position',[0.1300 0.1100 0.7750 0.8150])
exportgraphics(gcf,'G:\My Drive\tagami_hologram\testing_ver2\fig_gen\A_ii.pdf', 'ContentType', 'vector');
exportgraphics(gcf,'G:\My Drive\tagami_hologram\testing_ver2\fig_gen\A_ii.png');

clf
hold on
plot(target_index, target_pha,'k-','LineWidth',line_width)
scatter(target_index, a_iii_per_pha,250, 'rx','LineWidth',line_width)
errorbar(target_index, a_iii_per_pha_exp_mean,a_iii_per_pha_exp_std,'b-','LineWidth',line_width)
errorbar(target_index, a_iii_per_pha_exp_optimized_mean,a_iii_per_pha_exp_optimized_std,'g--','LineWidth',line_width)
% title('Phase A-iii')
xlabel('Sample [-]')
ylabel('Phase [rad]')
set(gca,'FontSize', fontsize)
grid on
grid minor
% legend('Target','Simulated','Exp (w/o opt)','Exp (w opt)')
set(gca,'Position',[0.1300 0.1100 0.7750 0.8150])
exportgraphics(gcf,'G:\My Drive\tagami_hologram\testing_ver2\fig_gen\A_iii_phase.pdf', 'ContentType', 'vector');
exportgraphics(gcf,'G:\My Drive\tagami_hologram\testing_ver2\fig_gen\A_iii_phase.png');

clf
hold on
plot(target_index, target_amp,'k-','LineWidth',line_width)
scatter(target_index, a_iii_per_amp,250,'rx','LineWidth',line_width)
errorbar(target_index, a_iii_per_amp_exp_mean,a_iii_per_amp_exp_std,'b-','LineWidth',line_width)
errorbar(target_index, a_iii_per_amp_exp_optimized_mean,a_iii_per_amp_exp_optimized_std,'g--','LineWidth',line_width)
% title('Amp A-iii')
% legend('Target','Diff-PAT(numerical)','Experimental (N/O)','Experimental (Optimized)')
xlabel('Sample [-]')
ylabel('Pressure [Pa]')
set(gca,'FontSize', fontsize)
grid on
grid minor
% legend('Target','Simulated','Exp (w/o opt)','Exp (w opt)')
set(gca,'Position',[0.1300 0.1100 0.7750 0.8150])
exportgraphics(gcf,'G:\My Drive\tagami_hologram\testing_ver2\fig_gen\A_iii_amp.pdf', 'ContentType', 'vector');
exportgraphics(gcf,'G:\My Drive\tagami_hologram\testing_ver2\fig_gen\A_iii_amp.png');

%% Performance
n = length(target_pha);
performance_num_ai_phase = sum((target_pha - a_i_per_pha).^2) ./n;
performance_num_aiii_phase = sum((target_pha - a_iii_per_pha).^2)./n;
performance_exp_ai_phase = sum((target_pha - a_i_per_pha_exp_mean).^2)./n;
performance_exp_aiii_phase = sum((target_pha - a_iii_per_pha_exp_mean).^2)./n;
performance_opt_ai_phase = sum((target_pha - a_i_per_pha_exp_optimized_mean).^2)./n;
performance_opt_aiii_phase = sum((target_pha - a_iii_per_pha_exp_optimized_mean).^2)./n;
disp('Phase Performance')
disp(['Numerical A:i: ' num2str(performance_num_ai_phase, 3)])
disp(['Numerical A:iii: ' num2str(performance_num_aiii_phase, 3)])
disp(['Experimental A:i: ' num2str(performance_exp_ai_phase, 3)])
disp(['Experimental A:iii: ' num2str(performance_exp_aiii_phase, 3)])
disp(['Optimized A:i: ' num2str(performance_opt_ai_phase, 3)])
disp(['Optimized A:iii: ' num2str(performance_opt_aiii_phase, 3)])

performance_num_aii_amp = sum((target_amp - a_ii_per_amp).^2)./n;
performance_num_aiii_amp = sum((target_amp - a_iii_per_amp).^2)./n;
performance_exp_aii_amp = sum((target_amp - a_ii_per_amp_exp_mean).^2)./n;
performance_exp_aiii_amp = sum((target_amp - a_iii_per_amp_exp_mean).^2)./n;
performance_opt_aii_amp = sum((target_amp - a_ii_per_amp_exp_optimized_mean).^2)./n;
performance_opt_aiii_amp = sum((target_amp - a_iii_per_amp_exp_optimized_mean).^2)./n;
disp('Amplitude Performance')
disp(['Numerical A:ii: ' num2str(performance_num_aii_amp, 3)])
disp(['Numerical A:iii: ' num2str(performance_num_aiii_amp, 3)])
disp(['Experimental A:ii: ' num2str(performance_exp_aii_amp, 3)])
disp(['Experimental A:iii: ' num2str(performance_exp_aiii_amp, 3)])
disp(['Optimized A:ii: ' num2str(performance_opt_aii_amp, 3)])
disp(['Optimized A:iii: ' num2str(performance_opt_aiii_amp, 3)])


