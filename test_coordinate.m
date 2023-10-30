clear all
close all
clc

phi = linspace(0, 2*pi, 25);
phi(end) = [];
radius = 3e-3;
mid_c = 0.095 - radius;
cy = radius*sin(phi);
cz = radius*cos(phi) + mid_c;

calib_data = readmatrix('experiment_data\step_9_calibrationdata.csv');
y_offset_mm = calib_data(1);
z_offset_mm = calib_data(2);
y_offset_pix = calib_data(3);
z_offset_pix = calib_data(4);
pix2mm = calib_data(5);

Ty = readmatrix('test_yyy.csv');
Tz = readmatrix('test_zzz.csv');
disp(calib_data)

y = y_offset_mm + ((Ty-y_offset_pix)*pix2mm);
z = z_offset_mm + ((z_offset_pix-Tz)*pix2mm);

figure
subplot(1,2,1)
plot(y)
hold on
plot(cy)

subplot(1,2,2)
plot(z)
hold on
plot(cz)