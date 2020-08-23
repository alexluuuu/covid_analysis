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

	# process parameter specifications from command line? 

	# protein_file_name = ""

	# # load in desired sequences
	# identifiers, sequences = read_from_file(protein_file_name)

	# seq_dict = {identifier:seq for identifier, seq in zip(identifiers, sequences)}

	# select the desired alleles 
	all_alleles = obtain_allele_list()

	partitioned_alleles = partition_alleles(all_alleles, truncate_test=True)

	prelim_file = "/Users/Alex/Documents/SchneckLab/COVID/prelim_seq.csv"
	sequence_df = pd.read_csv(prelim_file, index_col=0)

	strains = list(sequence_df.columns)

	for index, row in sequence_df.iterrows(): 
		print(row[strains[0]])
		print('--')
		for strain in strains: 
			prediction_df = prediction_whole_seq({strain:row[strain]}, partitioned_alleles[0])
			for allele_set in partitioned_alleles[1:]: 
				additional = prediction_whole_seq({strain:row[strain]}, partitioned_alleles[0])
				prediction.append(additional)


			prediction_df.to_csv('/Users/Alex/Documents/SchneckLab/COVID/predictions/' + strain.replace('/', '_') + '_test.csv')


	# call wrapped functions from prediction.py

	# write output files 



if __name__ == "__main__": 
	main()