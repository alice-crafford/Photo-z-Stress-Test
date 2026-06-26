# Photo-z Stress Test

Code and analysis for **"Diagnosing the Effects of Spectroscopic Training Set Imperfection on Photometric Redshift Performance"** (Crafford et al. 2026).

Paper: [arXiv:2601.10797](https://arxiv.org/abs/2601.10797)

## Overview

This repository contains the full analysis pipeline used to evaluate photo-z estimators under realistic spectroscopic training-set degradations. Six estimators (TrainZ, CMNN, GPz, GPz+GL, FZBoost, PZFlow) are run across six spectroscopic degradations (BOSS, DEEP2, GAMA, HSC, VVDSf02, zCOSMOS) and a range of inverse-redshift weighting strengths, with results compared using various metrics.

## Repository Structure

```
notebooks/      Jupyter notebooks for the full analysis pipeline
scripts/        Utility scripts for running the pipeline
paper_data/     Input catalogs, pipeline outputs, and computed statistics (gitignored)
plots/          Publication-quality figures
qp/             Local copy of the qp photo-z metrics library
```

## Notebooks

| Notebook | Description |
|---|---|
| `Test_Pipeline.ipynb` | Sets up and runs the RAIL pipeline: applies spectroscopic selection degradations, trains all six photo-z estimators on each degraded training set, and writes estimate outputs to `paper_data/` |
| `Evaluation_Pipeline.ipynb` | Computes distribution-to-distribution metrics (CvM, KS, RMSE, KLD, Wasserstein distance), PIT histograms, CDE loss, and outlier rejection statistics for all estimators across all degradation scenarios; writes results as `.pq` stat files in `paper_data/` |
| `Paper_Plots.ipynb` | Reads the computed statistics and generates all publication figures, saved to `plots/` |

## Scripts

| Script | Description |
|---|---|
| `Pipeline_and_Intermediates_Script.py` | Utility functions for converting RAIL pipeline intermediates (HDF5 → QP ensembles, table conversion, posterior plotting) |
| `Test_Pipeline_Run_Script.py` | CLI script to run a pre-configured RAIL pipeline YAML from the command line |
| `Trial_Run_Pipeline.sh` | SLURM batch script for running the pipeline on an HPC cluster |

## Data

All data files are stored in `paper_data/` (gitignored due to file size). To run any of the notebooks or scripts, download the dataset from Zenodo and extract it into `paper_data/`:

**Dataset:** [https://zenodo.org/records/20937648](https://zenodo.org/records/20937648)

The directory contains:
- `data/` — input galaxy catalog (`rubin_roman_catalog.pq`) and trained normalizing flow models
- `CMNN/`, `FZBoost/`, `GPz/`, `GPz_GL/`, `PZFlow/`, `TrainZ/` — per-estimator, per-degradation pipeline outputs and computed statistics
- Root-level `.pq` files — survey band grids, derived statistics, and pipeline intermediates

## Dependencies

- [RAIL](https://github.com/LSSTDESC/RAIL) — the core photo-z pipeline framework
- [qp](https://github.com/LSSTDESC/qp) — quantile-parametrized photo-z ensemble library (included as `qp/`)
- Standard scientific Python stack: numpy, scipy, pandas, matplotlib, h5py
