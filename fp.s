#!/bin/bash
#
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=2
#SBATCH --time=12:00:00
#SBATCH --mem=100GB
#SBATCH --job-name=JL_fp
#SBATCH --mail-type=END
#SBATCH --mail-user=jl860@nyu.edu
#SBATCH --output=slurm_%j.out

module purge
module load python3/intel/3.6.3

cd /scratch/[netID]/final_project
source venv/bin/activate
python -u main.py


