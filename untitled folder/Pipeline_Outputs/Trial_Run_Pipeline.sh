#!/bin/bash
#SBATCH -N 1
#SBATCH -C gpu
#SBATCH -G 1
#SBATCH -q debug
#SBATCH -J Trial_Run
#SBATCH --mail-user=acraffor@andrew.cmu.edu
#SBATCH --mail-type=ALL
#SBATCH -t 00:30:00
#SBATCH -A m1727

module load python 
conda activate rail-dev

#OpenMP settings:
export OMP_NUM_THREADS=1
export OMP_PLACES=threads
export OMP_PROC_BIND=spread

#run the application:
#applications may perform better with --gpu-bind=none instead of --gpu-bind=single:1 
srun -n 1 -c 128 --cpu_bind=cores -G 1 --gpu-bind=none  /global/homes/a/acraffor/Photo-z-Stress-Test/Pipeline_Outputs/Test_Pipeline_Run_Script.py


