"""util.py

Utilities for covid proteome predictions 

"""
import os 
import sys 
import numpy as np
import pandas as pd
import csv

from mhcflurry import Class1PresentationPredictor


def read_from_file(protein_file_name, target_identifiers=None): 
	"""read_from_file
	
	Args:
	    protein_file_name (str): specify the path to the fasta file 
	    target_sequences (None, List[str]: list of sequence identifiers 

	"""

	# initialize a data structure to store the results in the file
	identifiers = []
	sequences = []

	# open the file 
	with open(protein_file_name, 'rb') as f: 

		# iterate through the file and populate the data structure 

		all_lines = f.readlines() 

		identifiers = all_lines[::2]
		identifiers = list(map(lambda x: x[1:].decode('ascii').rstrip(), identifiers))
		print(identifiers[:10])
		sequences = all_lines[1::2]
		print(sequences[0])


	# return the data structure 

	if target_identifiers is not None: 
		target_sequences = []
		for identifier in target_identifiers: 
			target_sequences.append(sequences[identifiers.index(identifier)].decode('ascii').rstrip())

		return target_identifiers, target_sequences

	return identifiers, sequences


def preprocess_fasta(fasta_name, num_partitions=50):  
	"""preprocess_fasta
	
	Args:
	    fasta_name (TYPE): Description
	    num_partitions (int, optional): Description
	    
	    read in the giant fasta; 
	
	    partition it into smaller fastas
	
	    write out these fasta files
	
	Returns:
	    TYPE: Description
	
	"""

	return 


def write_sequences(filename, identifiers, sequences): 

	return 


def obtain_allele_list(): 
	predictor = Class1PresentationPredictor.load()
	# snippet for obtaining supported alleles directly
	return predictor.supported_alleles


def main(): 
	'''
	TODO FOR NOA: 

	consult: https://docs.python.org/3/tutorial/inputoutput.html
	
	1) use pandas package to read excel file and grab the column of identifiers corresponding to those 28 
	2) pass that column of identifiers as a list to the function read_from_file
	3) use python or pandas functions to write out a csv with format [identifier],[sequence] 
	4) push csv to repo

	--
	1) write / use function to translate RNA -> amino acidz
	2) write out amino acid sequences as a csv with format [identifier], [sequence]
	3) push csv to repo


	TODO FOR ALEX: 
	1) install multiple sequence alignment stuff
	2) do the alignment 
	3) run mhcflurry2.0 prediction

	---
	once complete, we will meet again to visualize data (write functions to do this)
	...

	talk with Dr. Schneck

	'''
	df = pd.read_excel('/Users/noaferziger/Documents/Schneck Lab /SARS-CoV-2 computational project/sequences/GISAID data/sample_sequences.xlsx')
	df1 = df[['strain']]
	print(df1)
	list_of_strains = df['strain'].to_list()
	print(list_of_strains)

	i = '/Users/noaferziger/covid_analysis/sequences_2020-07-27_16-35.fasta'

	identifiers, sequences = read_from_file(i, list_of_strains)
	print(sequences)

	list1 = ['hello', 'my', 'name']
	list2 = ['Noa', 'apple', 'banana']

	write_sequences('test.csv', list1, list2)


	with open('test.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerows(zip(identifiers, sequences))

if __name__ == "__main__": 
	print('hello')
	main()
