"""util.py

Utilities for covid proteome predictions 

"""
import os 
import sys 
import numpy as np
import pandas as pd
import csv

from mhcflurry import Class1PresentationPredictor


def produce_fasta(prelim_file): 

	sequence_df = pd.read_csv(prelim_file, index_col=0)

	# rows = [str(idx) for idx in sequence_df.index]
	for col in sequence_df.columns:
		print('---' + col)
		for row in sequence_df.index:
			outfile = os.path.join(os.getcwd(), 'data/test_' + row + '.fasta')
			with open(outfile, 'a') as f:
				f.write('>'+col+'\n')
				f.write(sequence_df[col][row]+'\n')

		print('--'*25)

	return
	


def obtain_strain_list(file="sequences.xlsx"): 

	cwd = os.getcwd()
	strain_df = pd.read_excel(os.path.join(cwd, file))

	return list(strain_df['strain'])


def obtain_allele_list(preselected=None): 

	if preselected is None:
		predictor = Class1PresentationPredictor.load()
		# snippet for obtaining supported alleles directly
		return predictor.supported_alleles

	else: 
		with open(preselected, 'r') as f: 
			all_lines = f.readlines()
			all_lines = list(map(lambda x: x.rstrip(), all_lines))
			return all_lines


def partition_alleles(all_alleles, num_per_partition=6, truncate_test=False): 

	partitioned_alleles = []
	for i in range(len(all_alleles)//num_per_partition):
		j = num_per_partition*(i+1) if i + 6 < len(all_alleles) else None
		partitioned_alleles.append(all_alleles[i*num_per_partition:j])

	if truncate_test: 
		print(partitioned_alleles[:10])
		return partitioned_alleles[:10]

	return partitioned_alleles


def process_fasta(fasta_name, target_identifiers): 

	sequences = {identifier: {} for identifier in target_identifiers}

	with open(fasta_name, 'rb') as f:

		meta = f.readline().decode("utf-8") 
		while meta: 
			sequence_line = f.readline().decode("utf-8").rstrip()
			for identifier in target_identifiers: 
				if identifier in meta: 
					splits = meta.split('|')
					protein = splits[0][1:] 
					print(identifier, protein)
					sequences[identifier][protein] = sequence_line

					break

			meta = f.readline().decode("utf-8") 

	proteins = list(sequences[target_identifiers[0]].keys())

	for identifier in target_identifiers: 
		if len(list(sequences[identifier].keys())) == 0: 
			print("protein sequences for %s were not found"%(identifier))
			del sequences[identifier]
			target_identifiers.remove(identifier)

	sequence_list = {identifier:[sequences[identifier][protein] for protein in proteins] for identifier in target_identifiers}

	sequence_df = pd.DataFrame(sequence_list, index=proteins)

	return sequence_df


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
	
	# cwd = os.getcwd()
	# fasta_name = os.path.join(cwd, "allprot0818.fasta")
	# strains = obtain_strain_list()
	# print(strains)
	# sequence_df = process_fasta(fasta_name, strains)

	# outfile = os.path.join(cwd, "prelim_seq.csv")
	# sequence_df.to_csv(outfile)


	cwd = os.getcwd()
	prelim_file = os.path.join(cwd, "prelim_seq.csv")

	produce_fasta(prelim_file)



if __name__ == "__main__": 

	main()
