# In-situ Optimization of Acoustic Hologram with Digital Twin

## Authors

- Tatsuki Fushimi¹ ²
- Daichi Tagami³
- Kenta Yamamoto³
- Yoichi Ochiai¹ ² ⁴

### Affiliations
1. Institute of Library, Information and Media Science, University of Tsukuba, Kasuga Campus Kasuga 1-2, Tsukuba, 305-8550, Ibaraki, Japan.
2. R&D Center for Digital Nature, University of Tsukuba, Kasuga Campus Kasuga 1-2, Tsukuba, 305-8550, Ibaraki, Japan.
3. Graduate School of Comprehensive Human Sciences, University of Tsukuba, Kasuga Campus Kasuga 1-2, Tsukuba, 305-8550, Ibaraki, Japan.
4. Pixie Dust Technologies, Inc., Misakicho 2-20-5, Chiyoda, 101-0061, Tokyo, Japan.

**Corresponding Author(s)**: tfushimi(at)slis.tsukuba.ac.jp

---

## Abstract

The need for accurate generation of acoustic holograms has increased with the prevalence of acoustophoresis methods like ultrasonic haptic sensation, acoustic levitation, and displays. However, experimental results indicate that the actual acoustic field may differ from the simulated field. This work introduces a digital twin approach that combines feedback from experimental measurements with numerically obtained derivatives of the loss function to optimize the hologram efficiently.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Installation and Requirements](#installation-and-requirements)
3. [Data and Code Structure](#data-and-code-structure)
4. [License](#license)
5. [Citation](#citation)

---

## Introduction

Detailed description and context.

---

## Installation and Requirements

### MATLAB Requirements
- MATLAB: 9.11
- Antenna Toolbox: 5.1
- Deep Learning HDL Toolbox: 1.2
- Fixed-Point Designer: 7.3
- Image Processing Toolbox: 11.4
- Mapping Toolbox: 5.2
- MATLAB Coder: 5.3
- RF Toolbox: 4.2
- Robotics System Toolbox: 3.4
- Signal Processing Toolbox: 8.7
- Simulink: 10.4
- Stateflow: 10.5
- Wavelet Toolbox: 6.0
- Curve Fitting Toolbox: 3.6

### Python Packages
- tensorflow: 2.10.0
- scipy: 1.9.1
- numpy: 1.23.2
- pyOptoSigma: 0.1
- libtiepie: -
- pypuclib: 0.0.2
- cv2: 4.6.0

---

## Data and Code Structure

### Main Directory
Experiment 1: Acoustic Pressure Optimization
- `step_1_exp_prep_move_mic.py`: Script for moving the microphone to the initial position for pressure measurements/optimization using OptoSigma XYZ Stage.
- `step_2_numerical_optimize.py`: Script for finding numerical optimima using Diff-PAT.
- `step_3_experimental_test_numerically_optimized.py`: Script for experimentally testing the numerically optimized acoustic field. Measurements using digital oscilloscope (TiePie Handyscope). 
- `step_4_experimental_optimize2match.py`: Script for performing in-situ optimization based on the experimental measurements. 
- `step_5_analyze_frequency_ver3.m`: MATLAB script for frequency analysis.
- `step_5_compare_performance_ver2.m`: MATLAB script for performance comparison between experimental and numerical optimization results.

Experiment 2: Acoustic Levitation - Equilibrium Point Optimization
- `step_6_calculating_equilibirum.m`: MATLAB script for calculating the equilibrium position of the levitated particle.
- `step_7_fit_equilibrium.m`: MATLAB script for fitting the calculated equilibrium state (Refer to manuscript for reasonings).
- `step_8_exp_prep_move_calibrator.py`: Script for preparing the experiment, including moving the optical calibrator to the initial position using XYZ stage.
- `step_9_capture_calibration_image.py`: Script for capturing images for calibration.
- `step_10_experimental_eq_nooptimization.py`: Script for experimental results without optimization.
- `step_11_experimental_eq_optimization.py`: Script for performing in-situ optimizaition using camera, and measure performance of optimization.

### Subfolders

- `discussion`: This folder contains discussion points and supplementary material.
- `experiment_data`: This folder contains all the raw and processed data from the experiments.
- `fig_gen`: This folder contains generated figures for the paper.
- `numerical_simulated_results`: This folder contains the results of the numerical simulations.

### Generated CSV Files by Step 2

The script `step_2_numerical_optimize.py` is responsible for generating multiple CSV files containing numerically obtained optimization results. These files are stored in the `numerical_simulated_results` directory. Below are the details of these files:

- `step_2_target_amp_list.csv`: 
  - **Directory**: `numerical_simulated_results`
  - **Description**: This file contains a list of target amplitudes, linearly spaced from 0.1 to 0.9 times the maximum amplitude.
  - **Columns**: Single column containing the target amplitude values.
  
- `step_2_target_pha_list.csv`: 
  - **Directory**: `numerical_simulated_results`
  - **Description**: This file contains a list of target phases, linearly spaced from 0 to \(2\pi\).
  - **Columns**: Single column containing the target phase values.

- `step2_target_A{i, ii, iii}_N_{n}_phase_export.csv`: 
  - **Directory**: `numerical_simulated_results`
  - **Description**: These files contain the simulated phase information.
  - **Indexed By**: Each setting is indexed by `{i, ii, iii}`, and the particular combination is indexed by `N_{n}`.
  - **Columns**: Each column represents a phase delay for each transducers. It is indexed in the order of the transducer position as it appears on trans_x, trans_y, trans_z. 

- `step_2_target_A{i, ii, iii}_performance_amp.csv`: 
  - **Directory**: `numerical_simulated_results`
  - **Description**: These files store the log of amplitude performance metrics in numerical optimization.
  - **Indexed By**: Each setting is indexed by `{i, ii, iii}`.
  - **Columns**: Acoustic amplitude obtained in the numerical simulation. 
  - **Rows**: Each row represents result for particular combination N_{n}.

- `step_2_target_A{i, ii, iii}_performance_pha.csv`: 
  - **Directory**: `numerical_simulated_results`
  - **Description**: These files store the log of phase performance metrics in numerical optimization.
  - **Indexed By**: Each setting is indexed by `{i, ii, iii}`.
  - **Columns**: Acoustic phase obtained in the numerical simulation. 
  - **Rows**: Each row represents result for particular combination N_{n}.

### Generated Files by Step 3

The Step 3 script (`step_3_experimental_test_numerically_optimized.py`) generates multiple files to capture both time stamps and experimental data.

- `step_3_experiment_begin_time.txt`:
  - **Directory**: `experiment_data`
  - **Description**: This file contains the date and time at which the Step 3 experiment began.
  - **Contents**: Single line text in the format "dd/mm/yyyy hh:mm:ss".

- `step3_optimize_match_target_A{i, ii, iii}_N_{n}_fft_freq_record_{l}_try.csv`:
  - **Directory**: `experiment_data`
  - **Description**: These files store the frequency spectrum used in the FFT analysis.
  - **Indexed By**: `{i, ii, iii}` for the setting and `N_{n}` for the particular combination. `{l}` indicates the try count. We try 3 times to obtain standard deviation. 
  - **Columns**: Single column containing frequency values.

- `step3_optimize_match_target_A{i, ii, iii}_N_{n}_fft_data_record_{l}_try.csv`:
  - **Directory**: `experiment_data`
  - **Description**: These files contain FFT magnitudes.
  - **Indexed By**: `{i, ii, iii}` for the setting and `N_{n}` for the particular combination. `{l}` indicates the try count. We try 3 times to obtain standard deviation. 
  - **Columns**: Single column containing FFT magnitude values.

- `step3_compare_A{i, ii, iii}_numerical2experiment_amp_{l}_try.csv`:
  - **Directory**: `experiment_data`
  - **Description**: These files store the measured amplitude data in the experiment for comparison with numerical data.
  - **Indexed By**: `{i, ii, iii}` for the setting. `{l}` indicates the try count.
  - **Columns**: Single column containing measured amplitude values.

- `step3_compare_A{i, ii, iii}_numerical2experiment_pha_{l}_try.csv`:
  - **Directory**: `experiment_data`
  - **Description**: These files store the measured phase data in the experiment for comparison with numerical data.
  - **Indexed By**: `{i, ii, iii}` for the setting. `{l}` indicates the try count.
  - **Columns**: Single column containing measured phase values.

### Generated Files by Step 4

The Step 4 script generates multiple files to capture both time stamps and optimization data.

- `step_4_experiment_begin_time.txt`:
  - **Directory**: `experiment_data`
  - **Description**: This file contains the date and time at which the Step 4 experiment began.
  - **Contents**: Single line text in the format "dd/mm/yyyy hh:mm:ss".

- `step4_optimize_match_target_A{i, ii, iii}_N_{n}_loss_record_{l}_try.csv`:
  - **Directory**: `experiment_data`
  - **Description**: These files store the loss metrics during the optimization process for each target.
  - **Indexed By**: `{i, ii, iii}` for the setting, `N_{n}` for the particular combination, and `{l}` for the try count.
  - **Columns**: Single column containing loss values for each iteration.

- `step4_optimize_match_target_A{i, ii, iii}_N_{n}_pat_phase_record_{l}_try.csv`:
  - **Directory**: `experiment_data`
  - **Description**: These files store the optimized phase values for each target.
  - **Indexed By**: `{i, ii, iii}` for the setting, `N_{n}` for the particular combination, and `{l}` for the try count.
  - **Columns**: Each column contains optimized phase values for each transducer.

- `step4_optimize_match_target_A{i, ii, iii}_N_{n}_fft_freq_record_{l}_try.csv`:
  - **Directory**: `experiment_data`
  - **Description**: These files store the frequency spectrum used in the FFT analysis for each target.
  - **Indexed By**: `{i, ii, iii}` for the setting, `N_{n}` for the particular combination, and `{l}` for the try count.
  - **Columns**: Single column containing frequency values.

- `step4_optimize_match_target_A{i, ii, iii}_N_{n}_fft_data_record_{l}_try.csv`:
  - **Directory**: `experiment_data`
  - **Description**: These files store the FFT magnitudes for each target.
  - **Indexed By**: `{i, ii, iii}` for the setting, `N_{n}` for the particular combination, and `{l}` for the try count.
  - **Columns**: Single column containing FFT magnitude values.

- `step4_target_A{i, ii, iii}_optimized_final_amplitude_{l}_try.csv`:
  - **Directory**: `experiment_data`
  - **Description**: These files store the final optimized amplitude values for each setting.
  - **Indexed By**: `{i, ii, iii}` for the setting and `{l}` for the try count.
  - **Columns**: Single column containing final optimized amplitude values.

- `step4_target_A{i, ii, iii}_optimized_final_phase_{l}_try.csv`:
  - **Directory**: `experiment_data`
  - **Description**: These files store the final optimized phase values for each setting.
  - **Indexed By**: `{i, ii, iii}` for the setting and `{l}` for the try count.
  - **Columns**: Single column containing final optimized phase values.

- `step4_target_A{i, ii, iii}_optimized_final_elapsedtime_{l}_try.csv`:
  - **Directory**: `experiment_data`
  - **Description**: These files store the elapsed time for each optimization cycle for each setting.
  - **Indexed By**: `{i, ii, iii}` for the setting and `{l}` for the try count.
  - **Columns**: Single column containing the elapsed time in seconds.

### Generated Files by Step 5: Analyze Frequency

In this MATLAB script for Step 5, the following files are generated:

- `discussion_harmonic_distortion_ver3.png`
    - **Directory**: `fig_gen`
    - **Description**: This PNG file visualizes the Total Harmonic Distortion (THD) for different target amplitudes.

- `discussion_second_harmonic_ver3.png`
    - **Directory**: `fig_gen`
    - **Description**: This PNG file visualizes the amplitude of the second harmonic for different target amplitudes.

### Generated Files by Step 5: Compare Performance

In this MATLAB script for Step 5, the following files are generated:

1. `A_{i, ii}.png` & `A_{i, ii}.pdf`
    - **Directory**: `fig_gen`
    - **Description**: This PNG/PDF file visualizes the performance difference between the numerical and experimental optimization. Plots amplitude performance for A_i, phase performance for A_ii.  

2. `A_iii_{phase, amp}.png` & `A_iii_{phase, amp}.pdf`
    - **Directory**: `fig_gen`
    - **Description**: This PNG/PDF file visualizes the performance difference between the numerical and experimental optimization. Plots amplitude and phase performance for A_iii.  

### Generated Files by Step 6

This is Step 6 in a multi-step process. It calculates the pressure and acoustic radiation force based on various parameters.

- `step_6_eq_store.mat`:
  - **Directory**: numerical_simulated_results
  - **Description**: This MATLAB .mat file stores the equilibrium points calculated for different focal points in the x, y, z domain. Contains variables FY, FZ, and eq_store.
  
 ### Generated Files by Step 7

This is Step 7 in the multi-step process. It focuses on fitting curves to the equilibrium points obtained from Step 6, and saves the fit coefficients.

- `step_7_fyfzey_coeff.csv`, `step_7_fyfzez_coeff.csv`:
  - **Directory**: numerical_simulated_results
  - **Description**: Two CSV files (`step_7_fyfzey_coeff.csv`, `step_7_fyfzez_coeff.csv`) in the `numerical_simulated_results` directory containing the coefficients of the fitted models for `e_y` and `e_z`.

### Generated Text and CSV Files by Step 9

The script is responsible for image processing and data logging, using OpenCV and pypuclib among other libraries. It captures images from a camera, detects circles, and exports data for later usage. Below are the details of the generated files:

- `step_9_experiment_begin_time.txt:`
  - **Directory**: `experiment_data`
  - **Description**: This file contains the start time and date of the experiment, formatted as "DD/MM/YYYY HH:MM:SS".
  - **Columns**: N/A (Single line text file containing the datetime string).

- `step_9_calibrationdata.csv:`
  - **Directory**: `experiment_data`
  - **Description**: This file contains calibration data including offsets in millimeters and pixels, and the pixel to millimeter conversion factor.
  - **Columns**: 
    - `y_offset_mm`: Y offset in millimeters
    - `z_offset_mm`: Z offset in millimeters
    - `y_offset_pix`: Y offset in pixels
    - `z_offset_pix`: Z offset in pixels
    - `pix2mm`: Conversion factor from pixels to millimeters (mm per pixel).

### Generated Image and CSV Files by Step 10

This script set the focal point, taking pictures, and storing image and numerical data. It utilizes various libraries including NumPy, pandas, libtiepie, and OpenCV among others. It takes pictures at various focal points and analyzes them, then saves this data in the form of images and CSV files. Below are the details of the generated files:

- Image Files: `step_10_position_XX_N_XX_img.jpg`
  - **Directory**: `experiment_data`
  - **Description**: These are the images taken at each focal point, where `XX` varies to denote the focal point and iteration number.
  - **Format**: JPEG image files.

- CSV Files: `step_10_rec_y_N_XX_data.csv` and `step_10_rec_z_N_XX_data.csv`
  - **Directory**: `experiment_data`
  - **Description**: These files contain the recorded y and z coordinates of the focal point, respectively, for each iteration `XX`.
  - **Columns**: 
    - Single column containing the y or z coordinate values in millimeters.

### Generated Image and CSV Files by Step 11
This script is designed for an experiment that involves setting focal points, capturing images, and conducting an optimization procedure. It employs various libraries, including TensorFlow for optimization, OpenCV for image capture and analysis, and more. The script captures images at various focal points, runs optimization algorithms, and stores the data in JPEG images and CSV files. Below are the details of the generated files:

- Image Files: `step_11_optimized_position_XX_N_XX_img.jpg`
  - **Directory**: `experiment_data`
  - **Description**: These JPEG images are captured at each focal point after the optimization process. `XX` denotes the focal point and iteration number.
  - **Format**: JPEG image files.

- `step_11_optimize_record_XX_N_XX_loss.csv`
  - **Directory**: `experiment_data`
  - **Description**: These files contain the loss values recorded during the optimization process for each focal point and iteration `XX`.
  - **Columns**: Single column containing the loss values.

- `step_11_optimize_record_XX_N_XX_focal_opt_y.csv` and `step_11_optimize_record_XX_N_XX_focal_opt_z.csv`
  - **Directory**: `experiment_data`
  - **Description**: These files contain the optimized y and z coordinates of the focal point, respectively, for each iteration `XX`.
  - **Columns**: Single column containing the y or z coordinate values in millimeters.

- `step_11_rec_y_N_XX_data.csv` and `step_11_rec_z_N_XX_data.csv`
  - **Directory**: `experiment_data`
  - **Description**: These files contain the recorded y and z coordinates of the focal point, respectively, for each iteration `XX`.
  - **Columns**: Single column containing the y or z coordinate values in millimeters.


---

## Citation

If you find this code useful for your research, please cite our paper.

```bibtex
@article{insitu2023,
  title={In-situ Optimization of Acoustic Hologram with Digital Twin},
  authors={Tatsuki Fushimi, Daichi Tagami, Kenta Yamamoto, Yoichi Ochiai},
  journal={Nature Communications Engineering},
  year={2023}
}

