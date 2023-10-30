clear all
close all
clc

load('numerical_simulated_results\step_6_eq_store.mat')

e_y = eq_store(:,2);
e_z = eq_store(:,3);

%% 近似: '新規近似 1'。
[xData, yData, zData] = prepareSurfaceData( FY, FZ, e_y );

% 近似タイプとオプションを設定します。
ft_ey = fittype( 'poly11' );

% モデルをデータに近似します。
[fitresult_y, gof_y] = fit( [xData, yData], zData, ft_ey );

format long
disp(gof_y)
disp(fitresult_y)
writematrix(coeffvalues(fitresult_y), 'numerical_simulated_results\step_7_fyfzey_coeff.csv')

%% 近似: '新規近似 1'。
[xData, yData, zData] = prepareSurfaceData( FY, FZ, e_z );

% 近似タイプとオプションを設定します。
ft_z = fittype( 'poly21' );

% モデルをデータに近似します。
[fitresult_z, gof_z] = fit( [xData, yData], zData, ft_z );

disp(gof_z)
disp(fitresult_z)

writematrix(coeffvalues(fitresult_z), 'numerical_simulated_results\step_7_fyfzez_coeff.csv')