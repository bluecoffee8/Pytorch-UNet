#!/bin/bash
#SBATCH -c 1 
#SBATCH -t 0:00:10
#SBATCH -p gpu
#SBATCH --gres=gpu:1 
#SBATCH --mem=1G

module load gcc/9.2.0
module load cuda/11.7 

python train.py --amp 