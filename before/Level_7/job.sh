#!/bin/bash
#PBS -N L7
#PBS -P xd2
#PBS -q normal
#PBS -l walltime=05:00:00
#PBS -l mem=6080GB
#PBS -l ncpus=1536
#PBS -l jobfs=6400GB
#PBS -l storage=scratch/xd2+gdata/xd2
#PBS -l wd
module use /g/data/xd2/modulefiles
module load firedrake/firedrake-zenodo
export OMP_NUM_THREADS=1
export PETSC_OPTIONS="-log_view"
#### Now run
mpiexec -np $PBS_NCPUS python stokes_cubed_sphere_7e3_A3_TS1.py &> output_1.dat &&
mpiexec -np $PBS_NCPUS python stokes_cubed_sphere_7e3_A3.py &> output_2.dat
