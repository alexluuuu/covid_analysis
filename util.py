"""util.py

Utilities for covid proteome predictions 

"""
import os 
import sys 
import numpy as np
import pandas as pd

from mhcflurry import Class1PresentationPredictor


def obtain_strain_list(file="/Users/Alex/Documents/SchneckLab/COVID/sequences.xlsx"): 

	strain_df = pd.read_excel(file)

	return list(strain_df['strain'])


def obtain_allele_list(): 
	predictor = Class1PresentationPredictor.load()
	# snippet for obtaining supported alleles directly
	return predictor.supported_alleles


def partition_alleles(all_alleles, num_per_partition=6, truncate_test=False): 

	partitioned_alleles = []
	for i in range(len(all_alleles)//num_per_partition):
		j = i + 6 if i + 6 < len(all_alleles) else None
		partitioned_alleles.append([all_alleles[i:i+6]])

	if truncate_test: 
		return partitioned_alleles[10]

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
		sequences = all_lines[1::2]

	# return the data structure 

	if target_identifiers is not None: 
		target_sequences = []
		for identifier in target_identifiers: 
			target_sequences.append(identifiers.index(identifier))

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
	
	fasta_name = "/Users/Alex/Documents/SchneckLab/COVID/allprot0818.fasta"
	strains = obtain_strain_list()
	print(strains)
	sequence_df = process_fasta(fasta_name, strains)

	outfile = "/Users/Alex/Documents/SchneckLab/COVID/prelim_seq.csv"
	sequence_df.to_csv(outfile)




if __name__ == "__main__": 
	main()


