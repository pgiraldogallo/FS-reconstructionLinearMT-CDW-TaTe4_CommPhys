#!/bin/bash
#SBATCH -J opt
#SBATCH -o vasp.o%j
#SBATCH -e vasp.e%j
#SBATCH -n 96
#SBATCH --ntasks-per-node=24
#SBATCH --exclude=cn0204-3,cn0211-1,cn0210-3,cn0208-4,cn0204-4,cn0112-2,cn0210-1,cn0512-4,cn0513-4,cn0512-2,cn0512-3,cn0513-1,cn0513-2,cn0514-1,cn0514-2,cn0514-3,cn0514-4,cn0512-1,cn0513-3,cn0210-4
#SBATCH --job-name=opt
#SBATCH -p comp
#SBATCH -t 96:00:00
#SBATCH --mail-type=END
#SBATCH --mail-user=acgarcia@uis.edu.co

# Intel Parallel Studio
source /software/LNS/Modules/3.2.10/init/bash
module load compilers/intel/parallel_studio_xe_2015/15.0.1
module load tools/intel/mkl/11.2.1
module load tools/intel/impi/5.0.2.044

# Location of VASP binary
VASP=/home/201901013c-2/codes/vasp/vasp.5.4.4-wannier-2.1.0/bin/vasp_ncl

# Location of mpirun
MPIRUN=/software/LNS/intel/impi/5.0.2.044/intel64/bin/mpirun

# Working directory

# Job starts
date
ulimit -s unlimited

# Enter the working directory
cd ${SLURM_SUBMIT_DIR}

# Run VASP

${MPIRUN} -np $SLURM_NTASKS ${VASP} > tvasp.out

# Job ends
date

rm WAVECAR CHG


