clear all
close all
clc

T1 = readmatrix('export\loss_1_optima.csv');
T2 = readmatrix('export\loss_2_optima.csv');
T3 = readmatrix('export\loss_3_optima.csv');
T4 = readmatrix('export\loss_4_optima.csv');

init = readmatrix('export\optima_init.csv');

init(isnan(T4)) = [];
T1(isnan(T4)) = [];
T2(isnan(T4)) = [];
T3(isnan(T4)) = [];
T4(isnan(T4)) = [];

left_init = find(init<10);
right_init = find(init>=10);

num2str(mean(T4(left_init)),3)
num2str(std(T4(left_init)),3)
num2str(mean(T4(right_init)),3)
num2str(std(T4(right_init)),3)


x = linspace(-2*pi, 6*pi, 50);
vT1 = readmatrix('export\loss_1_visual.csv');
vT2 = readmatrix('export\loss_2_visual.csv');
vT3 = readmatrix('export\loss_3_visual.csv');
vT4 = readmatrix('export\loss_4_visual.csv');
vgT1 = readmatrix('export\loss_1_grad.csv');
vgT2 = readmatrix('export\loss_2_grad.csv');
vgT3 = readmatrix('export\loss_3_grad.csv');
vgT4 = readmatrix('export\loss_4_grad.csv');

figure
subplot(1,2,1)
hold on
title('Loss Function')
plot(x, vT1,'k-','LineWidth',2)
plot(x, vT2,'r-','LineWidth',2)
plot(x, vT3,'gx','LineWidth',2)
grid on
grid minor
xlabel('x [-]')
ylabel('y [-]')
subplot(1,2,2)
hold on
title('Loss Function')
plot(x, vgT1,'k-','LineWidth',2)
plot(x, vgT2,'r-','LineWidth',2)
plot(x, vgT3,'gx','LineWidth',2)
plot(x, vgT4,'k-','LineWidth',2)
grid on
grid minor
set(gca,'YScale','log')
xlabel('x [-]')
ylabel('y [-]')