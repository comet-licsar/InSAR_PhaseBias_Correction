# InSAR Phase Bias Correction
This repository contains scripts for mitigating phase bias in InSAR data. It includes tools for reading data, calculating loop closures, estimating calibration parameters, performing inversion, and correcting interferograms.

## Installation (pip)

The package is installable with pip (Python >= 3.9; GDAL >= 3.4 required,
pulled in via prebuilt `gdal-wheel` on x86_64/aarch64):

```bash
pip install insar-phasebias
# or from this repository:
pip install .
```

## Directory Structure
- `phasebias/PhaseBias_01_Read_Data.py`: Reads input wrapped ifgs and coherence data.
- `phasebias/PhaseBias_02_Loop_Closures.py`: Calculates loop closures.
- `phasebias/PhaseBias_03_calibration_pars.py`: Estimates the calibration parameters $a_n$.
- `phasebias/PhaseBias_04_Inversion.py`: Performs inversion for phase bias estimation.
- `phasebias/PhaseBias_05_Correction.py`: Corrects interferograms using estimated biases.
- `phasebias/bin/`: Contains auxiliary functions used by the scripts.
- `config.txt`: Example configuration file for setting parameters.

## Usage
1. Create a working directory, put a `config.txt` (see the example in this
   repository) into it, and point `root_path`/`output_path` at your data.
2. Run the five steps in order:
   ```bash
   phasebias-01-read-data
   phasebias-02-loop-closures
   phasebias-03-calibration-pars
   phasebias-04-inversion
   phasebias-05-correction
   ```
   (equivalently: `python -m phasebias.PhaseBias_01_Read_Data`, etc.).
   Each step accepts `--help` for a detailed description.
3. Outputs:
   - `Data/` under `output_path`: pickled ifg/coherence/loop-closure arrays,
     calibration parameters (`Mean_an_values.pkl`), base-ifg biases
     (`X_base_ifgs_biases.npy`);
   - `GEOC/` under `output_path`: corrected wrapped interferograms (GeoTIFF).

## Test Dataset

The test dataset used in this repository originates from one of the islands in the Azores. The full dataset can be accessed through the COMET LiCSAR frame **082D_05125_020000**, available at the following link:

[https://gws-access.jasmin.ac.uk/public/nceo_geohazards/LiCSAR_products/82/082D_05125_020000/](https://gws-access.jasmin.ac.uk/public/nceo_geohazards/LiCSAR_products/82/082D_05125_020000/)

Additionally, we provide a **sample dataset**, including example interferograms, which can be downloaded from Zenodo:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14525360.svg)](https://doi.org/10.5281/zenodo.14525360)


# Citation
If you use this repository for your research, please cite the following paper:

Maghsoudi, Y., Hooper, A.J., Wright, T.J., Lazecky, M., & Ansari, H. (2022). Characterizing and correcting phase biases in short-term, multilooked interferograms. Remote Sensing of Environment, 275, 113022.
https://doi.org/10.1016/j.rse.2022.113022


# Acknowledgment
This work was funded by the European Space Agency (ESA) as part of the Phase Bias Correction Project. We gratefully acknowledge their support.

