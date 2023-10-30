clear all
close all
clc

phi = linspace(pi, 3*pi, 30);
phi(end) = [];
radius = 3e-3;
mid_c = 0.119 + radius;
cy = radius*sin(phi);
cz = radius*cos(phi) + mid_c;

Ty = zeros(3, length(phi));
Tz = zeros(3, length(phi));
for ii = 1:3
    Ty(ii, :) = readmatrix(['experiment_data\step_10_rec_y_N_' num2str(ii-1) '_data.csv']);
    Tz(ii, :) = readmatrix(['experiment_data\step_10_rec_z_N_' num2str(ii-1) '_data.csv']);
end
Ty_mean = mean(Ty, 1);
Tz_mean = mean(Tz, 1);
Ty_std = std(Ty,[],1);
Tz_std = std(Tz,[],1);

Ty_opt = zeros(3, length(phi));
Tz_opt = zeros(3, length(phi));
for ii = 1:3
    Ty_opt(ii, :) = readmatrix(['experiment_data\step_11_rec_y_N_' num2str(ii-1) '_data.csv']);
    Tz_opt(ii, :) = readmatrix(['experiment_data\step_11_rec_z_N_' num2str(ii-1) '_data.csv']);
end
Ty_opt_mean = mean(Ty_opt, 1);
Tz_opt_mean = mean(Tz_opt, 1);
Ty_opt_std = std(Ty_opt,[],1);
Tz_opt_std = std(Tz_opt,[],1);


figure('units','centimeters','outerposition',[0 0 30 30])
hold on
errorbar([Ty_mean Ty_mean(1)].*1e03, [Tz_mean Tz_mean(1)].*1e03, -[Ty_std Ty_std(1)].*1e03,[Ty_std Ty_std(1)].*1e03, -[Tz_std Tz_std(1)].*1e03, [Tz_std Tz_std(1)].*1e03,'LineWidth',3)
errorbar([Ty_opt_mean Ty_opt_mean(1)].*1e03, [Tz_opt_mean Tz_opt_mean(1)].*1e03, -[Ty_opt_std Ty_opt_std(1)].*1e03,[Ty_opt_std Ty_opt_std(1)].*1e03, -[Tz_opt_std Tz_opt_std(1)].*1e03, [Tz_opt_std Tz_opt_std(1)].*1e03,'LineWidth',3)
plot([cy cy(1)].*1e03, [cz cz(1)].*1e03,'k-','LineWidth',3)
axis equal
grid on
grid minor
xlabel('Y Axis [mm]')
ylabel('Z Axis [mm]')
legend('Exp w/o Opt', 'Exp w Opt','Target')
set(gca,'FontSize', 24)
set(gca,'Position',[0.1300 0.1100 0.7750 0.8150])
exportgraphics(gcf,'G:\My Drive\tagami_hologram\testing_ver2\fig_gen\eq_pos.pdf', 'ContentType', 'vector');
exportgraphics(gcf,'G:\My Drive\tagami_hologram\testing_ver2\fig_gen\eq_pos.png');


error_non_opt_y = rms(sqrt((cy-Ty_mean).^2));
error_non_opt_z = rms(sqrt((cz-Tz_mean).^2));
error_opt_y = rms(sqrt((cy-Ty_opt_mean).^2));
error_opt_z = rms(sqrt((cz-Tz_opt_mean).^2));
disp('RMS Performance')
disp(['Experimental Y: ' num2str(error_non_opt_y.*1e3, 3)])
disp(['Experimental Z: ' num2str(error_non_opt_z.*1e3, 3)])
disp(['Optimization Z: ' num2str(error_opt_y.*1e3, 3)])
disp(['Optimization Z: ' num2str(error_opt_z.*1e3, 3)])


X = categorical({'Y w/o opt', 'Y w/ opt', 'Z w/o opt', 'Z w/ opt'});
X = reordercats(X,{'Y w/o opt', 'Y w/ opt', 'Z w/o opt', 'Z w/ opt'});

figure('units','centimeters','outerposition',[0 0 30 20])
bar(X,[error_non_opt_y, error_opt_y, error_non_opt_z, error_opt_z].*1000)
ylabel('RMS Error (mm)')
grid on
grid minor
set(gca,'FontSize', 24)
set(gca,'Position',[0.1300 0.1100 0.7750 0.8150])
exportgraphics(gcf,'G:\My Drive\tagami_hologram\testing_ver2\fig_gen\eq_pos_error.pdf', 'ContentType', 'vector');
exportgraphics(gcf,'G:\My Drive\tagami_hologram\testing_ver2\fig_gen\eq_pos_error.png');
