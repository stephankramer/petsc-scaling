#!/bin/bash
#PBS -N L6
#PBS -P xd2
#PBS -q normal
#PBS -l walltime=10:00:00
#PBS -l mem=760GB
#PBS -l ncpus=192
#PBS -l jobfs=800GB
#PBS -l storage=scratch/xd2+gdata/xd2
#PBS -l wd
module use /g/data/xd2/modulefiles
module load firedrake/firedrake-20230525
export PYTHONPATH=$PYTHONPATH:/scratch/xd2/rad552/FIREDRAKE_GIT/gadopt-restructure
export OMP_NUM_THREADS=1
export PETSC_OPTIONS="-log_view"
#### Now run
mpiexec -np $PBS_NCPUS python stokes_cubed_sphere_7e3_A3_TS1.py &> output_1.dat &&
mpiexec -np $PBS_NCPUS python stokes_cubed_sphere_7e3_A3.py &> output_2.dat
