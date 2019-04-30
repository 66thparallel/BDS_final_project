#!/bin/bash
#
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=2
#SBATCH --time=2:00:00
#SBATCH --mem=30GB
#SBATCH --job-name=BDSFinalProject
#SBATCH --mail-type=END
#SBATCH --mail-user=[email address for notification]
#SBATCH --output=slurm_%j.out

module purge
module load python3/intel/3.6.3

cd /scratch/jl860/final_project
source venv/bin/activate
python -u bdsproject_merge.py


