"""postprocessing.py


utities file for post-processing of antigen binding data
"""

import numpy as np
import sys
import os 
import pandas as pd
import pickle


def write_to_file(name, obj):
	'''
		Write object of specified name to a pickle file 
	'''

	print 'writing structures to pickle'
	print '----------------------------'

	path = os.getcwd() + '/pickles/' + name + '.pkl'
	file = open(path, 'wb')
	pickle.dump(obj, file)
	file.close()


def display_dict(d): 
	for k, v in d.iteritems(): 
		print "===========" * 3, k, '====='*3
		# for k2, v2 in v.iteritems(): 
		# 	print "==" * 3, k2, "=="*3
		# 	print v2


def extract_top_ref(filenames, mode="SB"): 
	"""extract_top_ref
	
	Args:
	    filenames (TYPE): Description
	    mode (str, optional): Description
	
	Returns:
	    we should be producing a dictionary of the form 
	
	    extracted = {
	    	<protein> = {
	    		<HLA variant> = [ structure containing pos peptide affinity ]
	    	}
	    }
	
	Deleted Parameters:
	    filename (TYPE): Description
	    type (str, optional): Description
	"""
	if mode == 'SB': 
		accept_bindlevel = ["SB"]
	elif mode == 'WB': 
		accept_bindlevel = ["SB", "WB"]

	extracted = {}
	for filename in filenames: 
		with open(filename, 'r') as f: 
			line = f.readline()

			# temp = []
			while line: 
				comp = line.split()
				if len(comp) == 0: 
					line = f.readline()
					continue

				if comp[0].isdigit() and comp[-1] in accept_bindlevel: 
					temp = [comp[i] for i in [0, 2, 12]]

					protein_name = comp[10][:comp[10].index('_')] # lol this is gross
					hla = comp[1]

					if protein_name in extracted.keys(): 
						if hla in extracted[protein_name].keys(): 
							extracted[protein_name][hla].append(temp)

						else: 
							extracted[protein_name][hla] =[temp]

					else: 
						extracted[protein_name] = {hla: [temp]}

				line = f.readline()

	display_dict(extracted)
	return extracted


def extract_top(filenames, strain_list, mode="SB"): 
	"""extract_top
	
	Args:
	    filenames (TYPE): Description
	    strain_list (TYPE): Description
	    mode (str, optional): Description
	
	Returns:
	    for the non-reference sequences, we want to return dictionary of the following form :
	
	        extracted_protein = {
	        	<strain> = {
	        		<HLA variant> = [ structure containing pos peptide affinity ]
	        	}
	        }
	
	"""

	def strain_name_match(partial): 
		for strain in strain_list: 
			if partial in strain.replace('/','_'): 
				return strain


	if mode == 'SB': 
		accept_bindlevel = ["SB"]
	elif mode == 'WB': 
		accept_bindlevel = ["SB", "WB"]

	extracted = {}
	for filename in filenames: 
		with open(filename, 'r') as f: 
			line = f.readline()

			# temp = []
			while line: 
				comp = line.split()
				if len(comp) == 0: 
					line = f.readline() 
					continue

				if comp[0].isdigit() and comp[-1] in accept_bindlevel: 
					temp = [comp[i] for i in [0, 2, 12]]

					strain_name = strain_name_match(comp[10])
					hla = comp[1]

					if strain_name in extracted.keys(): 
						if hla in extracted[strain_name].keys(): 
							extracted[strain_name][hla].append(temp)

						else: 
							extracted[strain_name][hla] = temp

					else: 
						extracted[strain_name] = {hla: temp}

				line = f.readline()

	display_dict(extracted)
	return extracted


def main(): 
	"""Summary
	
	Returns:
	    TYPE: Description
	"""

	cwd = os.getcwd()
	output_dir = os.path.join(cwd, 'output/')
	ref_files = [output_dir + 'test_ref_' + str(i) + '.o' for i in range(5)]
	spike_files = [output_dir + 'test_Spike_' + str(i) + '.o' for i in range(5)]

	extracted_ref = extract_top_ref(ref_files)

	prelim_file = os.path.join(cwd, "prelim_seq.csv")
	sequence_df = pd.read_csv(prelim_file, index_col=0)

	strain_list = [str(col) for col in sequence_df.columns]

	extracted_spike = extract_top(spike_files, strain_list)

	write_to_file('extracted_ref', extracted_ref)
	write_to_file('extracted_spike', extracted_spike)


if __name__ == "__main__": 
	main()

