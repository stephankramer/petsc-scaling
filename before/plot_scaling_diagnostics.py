#! /usr/bin/env python3

import numpy, pylab, sys
from matplotlib import rcParams

preamble = sys.argv[1]

# Matplotlib defaults:
rcParams['axes.titlesize']  = 16
rcParams['axes.labelsize']  = 16
rcParams['xtick.labelsize'] = 16
rcParams['ytick.labelsize'] = 16
rcParams['legend.fontsize'] = 15

############### FIRST GATHER DATA ###################

dirs  = ["Level_5", "Level_6","Level_7"]
cores = [24, 192, 1536]

# Set up arrays:
schur_solve_time   = numpy.zeros((len(dirs),1))
energy_solve_time  = numpy.zeros((len(dirs),1))
SNES_function_time = numpy.zeros((len(dirs),1))
SNES_jacobian_time = numpy.zeros((len(dirs),1))
assembly_time      = numpy.zeros((len(dirs),1))
PC_setup_time      = numpy.zeros((len(dirs),1))
mean_velocity_its  = numpy.zeros((len(dirs),1))
mean_pressure_its  = numpy.zeros((len(dirs),1))
mean_energy_its    = numpy.zeros((len(dirs),1))
velocity_cost_per_it = numpy.zeros((len(dirs),1))
total_cost = numpy.zeros((len(dirs),1))

# Loop over directiories and store data:
for dir in range(len(dirs)):
    data = numpy.loadtxt(dirs[dir]+"/Timings_Iterations.dat")
    schur_solve_time[dir,:]   = data[0]
    energy_solve_time[dir,:]  = data[1]
    SNES_function_time[dir,:] = data[2]
    SNES_jacobian_time[dir,:] = data[3]
    PC_setup_time[dir,:]      = data[4]
    mean_velocity_its[dir,:]  = data[5]
    mean_pressure_its[dir,:]  = data[6]
    mean_energy_its[dir,:]    = data[7]
    total_cost[dir,:]    = data[8]        

assembly_time = SNES_function_time + SNES_jacobian_time
velocity_cost_per_it = (schur_solve_time - PC_setup_time) / mean_velocity_its

print(velocity_cost_per_it)

############### NOW PLOT ###################

### # Schur solve time ###
pylab.semilogx(cores,schur_solve_time,'ko',linestyle="none", markersize=10)
pylab.xlabel("# Cores")
pylab.ylabel("Stokes Solve (s)")
pylab.xlim(10,3e4)
pylab.xticks([10,100,1000,10000])
pylab.ylim(0,16000)
pylab.yticks(numpy.linspace(0,16000,5))
pylab.grid()
pylab.savefig(preamble+"_Schur_Solve_time.png",bbox_inches="tight")
pylab.savefig(preamble+"_Schur_Solve_time.pdf",bbox_inches="tight")
pylab.close()

### # Energy solve time ###
pylab.semilogx(cores,energy_solve_time,'ko',linestyle="none", markersize=10)
pylab.xlabel("# Cores")
pylab.ylabel("Energy Solve (s)")
pylab.xlim(10,3e4)
pylab.xticks([10,100,1000,10000])
pylab.ylim(8,14)
pylab.yticks(numpy.linspace(8,14,4))
pylab.grid()
pylab.savefig(preamble+"_Energy_Solve_time.png",bbox_inches="tight")
pylab.savefig(preamble+"_Energy_Solve_time.pdf",bbox_inches="tight")
pylab.close()

### # SNES Function time ###
pylab.semilogx(cores,SNES_function_time,'ko',linestyle="none", markersize=10)
pylab.xlabel("# Cores")
pylab.ylabel("SNES Function (s)")
pylab.xlim(10,3e4)
pylab.xticks([10,100,1000,10000])
pylab.grid()
pylab.savefig(preamble+"_SNES_function_time.png",bbox_inches="tight")
pylab.savefig(preamble+"_SNES_function_time.pdf",bbox_inches="tight")
pylab.close()

### # SNES Jacobian time ###
pylab.semilogx(cores,SNES_jacobian_time,'ko',linestyle="none", markersize=10)
pylab.xlabel("# Cores")
pylab.ylabel("SNES Jacobian (s)")
pylab.xlim(10,3e4)
pylab.xticks([10,100,1000,10000])
pylab.grid()
pylab.savefig(preamble+"_SNES_jacobian_time.png",bbox_inches="tight")
pylab.savefig(preamble+"_SNES_jacobian_time.pdf",bbox_inches="tight")
pylab.close()

### # Assembly time ###
pylab.semilogx(cores,assembly_time,'ko',linestyle="none", markersize=10)
pylab.xlabel("# Cores")
pylab.ylabel("Assembly (s)")
pylab.xlim(10,3e4)
pylab.xticks([10,100,1000,10000])
pylab.ylim(0,12)
pylab.yticks(numpy.linspace(0,12,4))
pylab.grid()
pylab.savefig(preamble+"_assembly_time.png",bbox_inches="tight")
pylab.savefig(preamble+"_assembly_time.pdf",bbox_inches="tight")
pylab.close()

### # PC Setup Time ###
pylab.semilogx(cores,PC_setup_time,'ko',linestyle="none", markersize=10)
pylab.xlabel("# Cores")
pylab.ylabel("PC Setup (s)")
pylab.xlim(10,3e4)
pylab.xticks([10,100,1000,10000])
pylab.ylim(0,600)
pylab.yticks(numpy.linspace(0,600,7))
pylab.grid()
pylab.savefig(preamble+"_PC_Setup_time.png",bbox_inches="tight")
pylab.savefig(preamble+"_PC_Setup_time.pdf",bbox_inches="tight")
pylab.close()

### # Pressure iterations ###
pylab.semilogx(cores,mean_pressure_its,'ko',linestyle="none", markersize=10)
pylab.xlabel("# Cores")
pylab.ylabel("# Pressure Solve Iterations")
pylab.xlim(10,3e4)
pylab.xticks([10,100,1000,10000])
pylab.ylim(9,11)
pylab.yticks(numpy.linspace(9,11,5))
pylab.grid()
pylab.savefig(preamble+"_Pressure_Iterations.png",bbox_inches="tight")
pylab.savefig(preamble+"_Pressure_Iterations.pdf",bbox_inches="tight")
pylab.close()

### # Velocity iterations ###
pylab.semilogx(cores,mean_velocity_its,'ko',linestyle="none", markersize=10)
pylab.xlabel("# Cores")
pylab.ylabel("# Velocity Solve Iterations")
pylab.xlim(10,3e4)
pylab.xticks([10,100,1000,10000])
pylab.ylim(40,56)
pylab.yticks(numpy.linspace(40,56,5))
pylab.grid()
pylab.savefig(preamble+"_Velocity_Iterations.png",bbox_inches="tight")
pylab.savefig(preamble+"_Velocity_Iterations.pdf",bbox_inches="tight")
pylab.close()

### # Energy iterations ###
pylab.semilogx(cores,mean_energy_its,'ko',linestyle="none", markersize=10)
pylab.xlabel("# Cores")
pylab.ylabel("# Energy Solve Iterations")
pylab.xlim(10,3e4)
pylab.xticks([10,100,1000,10000])
pylab.ylim(11,13)
pylab.yticks(numpy.linspace(11,13,5))
pylab.grid()
pylab.savefig(preamble+"_Energy_Iterations.png",bbox_inches="tight")
pylab.savefig(preamble+"_Energy_Iterations.pdf",bbox_inches="tight")
pylab.close()

### # Velocity cost per iteration ###
pylab.semilogx(cores,velocity_cost_per_it,'ko',linestyle="none", markersize=10)
pylab.xlabel("# Cores")
pylab.ylabel("Per Velocity Iteration (s)")
pylab.xlim(10,3e4)
pylab.xticks([10,100,1000,10000])
pylab.ylim(0,300)
pylab.yticks(numpy.linspace(0,300,4))
pylab.grid()
pylab.savefig(preamble+"_Velocity_Cost_Per_Iteration.png",bbox_inches="tight")
pylab.savefig(preamble+"_Velocity_Cost_Per_Iteration.pdf",bbox_inches="tight")
pylab.close()

### # Total Time ###
pylab.semilogx(cores,total_cost,'ko',linestyle="none", markersize=10)
pylab.xlabel("# Cores")
pylab.ylabel("Total Time (s)")
pylab.xlim(10,3e4)
pylab.xticks([10,100,1000,10000])
pylab.ylim(0,16000)
pylab.yticks(numpy.linspace(0,16000,5))
pylab.grid()
pylab.savefig(preamble+"_Total_Time.png",bbox_inches="tight")
pylab.savefig(preamble+"_Total_Time.pdf",bbox_inches="tight")
pylab.close()

# Make some combination plots:

### # Iterations ###
pylab.semilogx(cores,mean_velocity_its,'go',linestyle="none", markersize=10,label="Velocity")
pylab.semilogx(cores,mean_pressure_its,'rs',linestyle="none", markersize=10,label="Pressure")
pylab.semilogx(cores,mean_energy_its,'b*',linestyle="none", markersize=10, label="Energy")
pylab.xlabel("# Cores")
pylab.ylabel("# Solve Iterations")
pylab.xlim(10,3e4)
pylab.xticks([10,100,1000,10000])
pylab.ylim(0,80)
pylab.yticks(numpy.linspace(0,80,5))
pylab.grid()
pylab.legend(numpoints=1)
pylab.savefig(preamble+"_Combined_Iterations.png",bbox_inches="tight")
pylab.savefig(preamble+"_Combined_Iterations.pdf",bbox_inches="tight")
pylab.close()



