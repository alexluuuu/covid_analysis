"""pipeline.py

Full pipeline 
"""
import numpy as np
import os 
import sys 
import pandas as pd
import argparse

from prediction import *
from util import *


def main(): 

	# select the desired alleles 
	cwd = os.getcwd()
	all_alleles = obtain_allele_list(preselected=os.path.join(cwd, "supported_alleles.txt"))

	# # to do: how to find the most ocmmon worldwide? 

	partitioned_alleles = partition_alleles(all_alleles, truncate_test=True)

	prelim_file = os.path.join(cwd, "prelim_seq.csv")
	sequence_df = pd.read_csv(prelim_file, index_col=0)

	strains = list(sequence_df.columns)

	for index, row in sequence_df.iterrows(): 
		print('=='*25)
		for strain in strains: 
			print('>' + ' '*25 + strain)
			print(partitioned_alleles[0])
			prediction_df = prediction_whole_seq({strain:row[strain]}, partitioned_alleles[0])
			for allele_set in partitioned_alleles[1:]: 
				print(allele_set)
				additional = prediction_whole_seq({strain + index:row[strain]}, allele_set)
				prediction_df.append(additional)

			print('--'*25)


			prediction_df.to_csv(os.path.join(cwd, 'predictions/', strain.replace('/', '_') + '_' + index + '_test.csv'))


	# call wrapped functions from prediction.py

	# write output files 



if __name__ == "__main__": 
	main()