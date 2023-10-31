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

### Step 5: Analyze Frequency - Generated Files

In this MATLAB script for Step 5, the following files are generated:

#### Image Files

1. `discussion_harmonic_distortion_ver3.png`
    - **Description**: This PNG file visualizes the Total Harmonic Distortion (THD) for different target amplitudes.
    - **Generated by**: `exportgraphics(gcf,'fig_gen\discussion_harmonic_distortion_ver3.png');`

2. `discussion_second_harmonic_ver3.png`
    - **Description**: This PNG file visualizes the amplitude of the second harmonic for different target amplitudes.
    - **Generated by**: `exportgraphics(gcf,'fig_gen\discussion_second_harmonic_ver3.png');`



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

