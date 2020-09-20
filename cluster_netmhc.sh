#!/bin/bash
#SBATCH --job-name=matlab
#SBATCH --time=1:00:00
#SBATCH --partition=shared
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=2
### Using more tasks because default memory is ~5GB per core
### 'shared' will share the node with other users
### 'parallel' use entire node (24,28,48, depends on node type)

# Send an email to this address when your job starts and finishes
#SBATCH --mail-user=alexlu@jhmi.edu
#SBATCH --mail-type=begin
#SBATCH --mail-type=end


ml # confirm modules used

netMHC-4.0/netMHC -l 8,9,10,11,12 -s data/test_ref.fasta > output/test_ref.out

