#!/bin/bash

#SBATCH --job-name=mitos2_zhokhov
#SBATCH --error=zhokhov_error.out
#SBATCH --nodes=1
#SBATCH --cpus-per-task=4
#SBATCH --ntasks-per-node=16
#SBATCH --time=300:00:00
#SBATCH --mem=120Gb
#SBATCH --account=bisc030525

cd $SLURM_SUBMIT_DIR

runmitos.py -i /user/work/xl23854/Annotating/full_mtDNA_alignment.fasta -o /user/work/xl23854/mitos2_output_zhokhov_new -c 2 -R /user/work/xl23854/mitos2_refdata -r refseq63m --debug 
