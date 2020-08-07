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

	protein_file_name = ""

	# load in desired sequences
	identifiers, sequences = read_from_file(protein_file_name)

	seq_dict = {identifier:seq for identifier, seq in zip(identifiers, sequences)}

	# select the desired alleles 
	all_alleles = obtain_allele_list()

	alelles = {}
	for i, allele in enumerate(all_alleles): 
		alleles{'allele_' + str(i)} = allele


	# call wrapped functions from prediction.py

	# write output files 



if __name__ == "__main__": 
	main()