# In-situ Optimization of Acoustic Hologram with Digital Twin

## Authors

- Tatsuki Fushimi¹,²
- Daichi Tagami³
- Kenta Yamamoto³
- Yoichi Ochiai¹,²,⁴

### Affiliations
1. Institute of Library, Information and Media Science, University of Tsukuba, Kasuga Campus Kasuga 1-2, Tsukuba, 305-8550, Ibaraki, Japan.
2. R&D Center for Digital Nature, University of Tsukuba, Kasuga Campus Kasuga 1-2, Tsukuba, 305-8550, Ibaraki, Japan.
3. Graduate School of Comprehensive Human Sciences, University of Tsukuba, Kasuga Campus Kasuga 1-2, Tsukuba, 305-8550, Ibaraki, Japan.
4. Pixie Dust Technologies, Inc., Misakicho 2-20-5, Chiyoda, 101-0061, Tokyo, Japan.

**Corresponding Author(s)**: tfushimi@slis.tsukuba.ac.jp

---

## Abstract

The need for accurate generation of acoustic holograms has increased with the prevalence of acoustophoresis methods like ultrasonic haptic sensation, acoustic levitation, and displays. However, experimental results indicate that the actual acoustic field may differ from the simulated field. This work introduces a digital twin approach that combines feedback from experimental measurements with numerically obtained derivatives of the loss function to optimize the hologram efficiently.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Installation and Requirements](#installation-and-requirements)
3. [Usage](#usage)
4. [Data and Code Structure](#data-and-code-structure)
5. [Simulation](#simulation)
6. [Recreating Experiments](#recreating-experiments)
7. [License](#license)
8. [Citation](#citation)

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

- `step_1_exp_prep_move_mic.py`: Script for preparing the experiment, including moving the microphone to the initial position.
- `step_2_numerical_optimize.py`: Script for numerical optimization of the acoustic field.
- `step_3_experimental_test_numerically_optimized.py`: Script for experimentally testing the numerically optimized acoustic field.
- `step_4_experimental_optimize2match.py`: Script for adjusting the experiment based on the numerical optimization results.
- `step_5_analyze_frequency_ver3.m`: MATLAB script for frequency analysis.
- `step_5_compare_performance_ver2.m`: MATLAB script for performance comparison between experimental and numerical results.
- `step_6_calculating_equilibirum.m`: MATLAB script for calculating the equilibrium state of the acoustic field.
- `step_7_fit_equilibrium.m`: MATLAB script for fitting the calculated equilibrium state.
- `step_8_exp_prep_move_calibrator.py`: Script for preparing the experiment, including moving the calibrator to the initial position.
- `step_9_capture_calibration_image.py`: Script for capturing images for calibration.
- `step_10_experimental_eq_nooptimization.py`: Script for experimental results without optimization.
- `step_11_experimental_eq_optimization.py`: Script for experimental results with optimization.

### Subfolders

- `discussion`: This folder contains discussion points and supplementary material.
- `experiment_data`: This folder contains all the raw and processed data from the experiments.
- `fig_gen`: This folder contains generated figures for the paper.
- `numerical_simulated_results`: This folder contains the results of the numerical simulations.

---

## Citation

If you find this code useful for your research, please cite our paper.

```bibtex
@article{your_paper_identifier,
  title={In-situ Optimization of Acoustic Hologram with Digital Twin},
  authors={Tatsuki Fushimi, Daichi Tagami, Kenta Yamamoto, Yoichi Ochiai},
  journal={Your Journal},
  year={Your Year}
}

