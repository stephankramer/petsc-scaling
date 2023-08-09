Performance comparison of a variable viscosity Mantle convection Stokes solve, section 6 
of https://gmd.copernicus.org/articles/15/5127/2022/ between two versions of PETSc: v3.16.4 (before) and PETSC main from May 2023 (after)

Full logs of runs on Level_5, Level_6, Level7, etc. are in before/Level_5/output1.dat and before/Level_5/output2.dat. 
output1.dat is from a two timestep cold start to ensure everything is precompiled by firedrake and output2.dat is a 10 timestep run after that

Level 5, 6, 7, and 8 have been run on 24, 192, 1536, 12288 cpus.
