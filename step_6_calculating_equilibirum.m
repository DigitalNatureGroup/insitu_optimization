clear all
close all
clc
%% Pressure and Acostic Radiation Force Calculation Code
% (C) Tatsuki Fushimi
% 2022/09/23
%% Air
rho_0 = 1.21; % [kg m-3] Density of Air
c0 = 346; % m/s
%% Levitated Particle Properties
r_p = 0.7e-03; % [m] radius of particles
rho_p = 40; % [kg m-3] density of expanded polystyrene (EPS)
c_p = 900; % [m s-1] estimate of speed of sound in EPS

%% Transducer Properties
voltage = 12;
p_0 = (1.61309/9)*voltage;
f0 = 40e03; % Hz
lambda = c0/f0;
k = 2*pi*f0/c0;
a = 5e-03; % Transducer Radius
Tx = readmatrix('trans_x_512.csv');
Ty = readmatrix('trans_y_512.csv');
Tz = readmatrix('trans_z_512.csv');
%% Force calculation
kapa=1/(rho_0*(c0^2));
kapa_p=1/(rho_p*(c_p^2));
k_tilda=kapa_p/kapa;
f_1=1-k_tilda;
roh_tilda=rho_p/rho_0;
f_2=(2*(roh_tilda-1)) / ((2*roh_tilda)+1);
vol=(4/3)*pi*(r_p^3);
F_grav = 9.81*vol*rho_p;
%% Focus Scan
simulation_space = lambda;
grid_spc = lambda / 20;
base_z = 0.119;
h = lambda/100;

focus_scan_spc = lambda/5;
fy = -lambda:focus_scan_spc:lambda;
fz = -lambda+base_z:focus_scan_spc:lambda+base_z;
[FY, FZ] = ndgrid(fy,fz);
FY = FY(:);
FZ = FZ(:);

%% Specify Trap Type
trap_type = 1; % 0 for focus, 1 for twin trap in single sided levitator, 2 for twin trap in double sided acosutic levitator
switch trap_type
    case 0
        trap =  zeros(length(Tx), 1);
    case 1
        trap = zeros(length(Tx), 1);
        trap(Tx>0) = pi;
    case 2
        trap = zeros(length(Tx), 1);
        trap(Tz>0) = pi;
end
%%

x =-simulation_space:grid_spc:simulation_space; 
y = min(fy)-simulation_space:grid_spc:max(fy)+simulation_space;
z = min(fz)-simulation_space:grid_spc:max(fz)+simulation_space;
[XX, YY, ZZ] = ndgrid(x, y, z);
pre_calc = zeros(length(FY), length(x), length(y), length(z));
for tr = 1:length(Tx)
    trans_x = [Tx(tr) Ty(tr) Tz(tr)];
    trans_q = [0,0,1];
    
    if Tz(tr) > 0
        trans_q(3) = -1;
    end
    
    r_prep_x = XX-Tx(tr);
    r_prep_y = YY-Ty(tr);
    r_prep_z = ZZ-Tz(tr);
    
    R = sqrt((r_prep_x).^2 + (r_prep_y).^2 + (r_prep_z).^2);
    dotproduct = r_prep_x.*trans_q(1) + r_prep_y.*trans_q(2) + r_prep_z.*trans_q(3);
    theta = acos(dotproduct./R./sqrt(trans_q(1).^2+trans_q(2).^2+trans_q(3).^2));
    D = directivity_fun(k, a, theta);
    pre_calc(tr,:,:,:) = (p_0./R) .* D .* exp(1j.*(k.*R+trap(tr)));
    %+focal_phi(tr)
end

eq_store = zeros(length(FY), 3);
for ii = 1:length(FY)
    %% Specify Levitation Points
    focal_point = [0,FY(ii),FZ(ii)];
    focal_phi = -(2*pi*f0/c0).*(sqrt((focal_point(1)-Tx).^2+(focal_point(2)-Ty).^2+(focal_point(3)-Tz).^2) ...
        - sqrt(focal_point(1).^2 + focal_point(2).^2 + focal_point(3).^2));
    
    p1 = zeros(length(x),length(y),length(z));
    for tr = 1:length(Tx)
        p1 = p1 + squeeze(pre_calc(tr,:,:,:)).* exp(1j.*(focal_phi(tr)));
    end
    
%     
%     visualzie_pressure_field = 1;
%     if visualzie_pressure_field
%         figure
%         pcolor(x, z, abs(squeeze(interpn(x,y,z, p1, x, 0, z)))');
%         shading interp
%         colormap hot
%         xlabel('X Axis [m]')
%         ylabel('Z Axis [m]')
%         axis equal
%         colorbar % units in Pa
%     end
    
    [vel_y, vel_x, vel_z]=gradient((1/(1i*rho_0*(2*pi*f0))).*(p1), grid_spc); %grad is meshgrid function, thus becomes y x
    amp_vel=sqrt((abs(vel_x)).^2 + (abs(vel_y)).^2 +(abs(vel_z)).^2);
    U = (vol.*f_1*0.5*kapa).*(0.5.*(abs(p1).^2)) - ((vol.*f_2*(3/4)*rho_0).*(0.5.*(abs(amp_vel).^2))); %Gorkov Potential
    %% Finds acoustic radiation force
    [ga_dy_F, ga_dx_F, ga_dz_F] = gradient(-1.*U, grid_spc); % as before
    
    %% Find equilibrium points
    fun_fx = @(ex, ey, ez) interpn(x,y,z,ga_dx_F, ex, ey, ez,'spline');
    fun_fy = @(ex, ey, ez) interpn(x,y,z,ga_dy_F, ex, ey, ez,'spline');
    fun_fz = @(ex, ey, ez) interpn(x,y,z,ga_dz_F, ex, ey, ez,'spline') - F_grav;
    grad_fun_fx = @(ex, ey, ez) ([fun_fx(ex+h, ey, ez), fun_fx(ex, ey+h, ez), fun_fx(ex, ey, ez+h)] - fun_fx(ex, ey, ez))./h;
    grad_fun_fy = @(ex, ey, ez) ([fun_fy(ex+h, ey, ez), fun_fy(ex, ey+h, ez), fun_fy(ex, ey, ez+h)] - fun_fy(ex, ey, ez))./h;
    grad_fun_fz = @(ex, ey, ez) ([fun_fz(ex+h, ey, ez), fun_fz(ex, ey+h, ez), fun_fz(ex, ey, ez+h)] - fun_fz(ex, ey, ez))./h;
    
    x_e = [focal_point(1), focal_point(2), focal_point(3)]'; % initial guess near focal point
    correction = 1;
    while sum(abs(correction)) > 0.1e-03
        Jacobian = [grad_fun_fx(x_e(1), x_e(2), x_e(3)); grad_fun_fy(x_e(1), x_e(2), x_e(3)); grad_fun_fz(x_e(1), x_e(2), x_e(3))];
        loss = [fun_fx(x_e(1), x_e(2), x_e(3)), fun_fy(x_e(1), x_e(2), x_e(3)), fun_fz(x_e(1), x_e(2), x_e(3))]';
        correction = - pinv(Jacobian)*loss;
        x_e = x_e + correction;
    end
    eq_store(ii, :) = x_e;
end

figure
quiver(FY, FZ, eq_store(:,2)-FY, eq_store(:,3)-FZ)
axis equal

save('numerical_simulated_results\step_6_eq_store.mat','FY','FZ','eq_store')
