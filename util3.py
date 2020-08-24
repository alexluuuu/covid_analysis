"""util3.py

"""

import Bio
import os 
import sys 
import numpy as np
import pandas as pd
import csv

from Bio.Seq import *
from Bio.Alphabet import IUPAC
from Bio.Data import CodonTable

'''
def main():

	df = pd.read_csv('/Users/noaferziger/covid_analysis/test.csv', header=None, names=["strain", "sequence"])
	print(df)
	# sequences = df['sequence'].tolist()

	#coding_dna = [sequence]
	# coding_dna = Seq("GTGAAAAAGATGCAATCTATCGTACTCGCACTTTCCCTGGTTCTGGTCGCTCCCATGGCA")
	# coding_dna.translate(table=11)
	
	# aa = coding_dna.translate()
	# for var in "sequence":
	# 	var.translate()

	df['sequence'] = df['sequence'].map(sequence.translate(table=11))
	# print(df)

	# df['sequence'] = sequence.translate(df['sequence'])

	
if __name__ == "__main__": 
	print('hello')
	main()
'''

def main():

	df = pd.read_csv('/Users/noaferziger/covid_analysis/test.csv', header=None, names=["strain", "sequence"])
	print(df)
	# spark_df.rdd.map()
	# trans_df = spark_df.map(lambda x: x.translate(table=11) if x.name == 'sequence' else x)
	# x = ['sequences']
	df['sequence'] = df['sequence'].map(lambda x: translate(x, table=11))
	# sequence.translate(table=11)
	# print(trans_df)

	# df['sequence'] = df['sequence'].map(sequence.translate(table=11))

# with open('aa_sequences.csv', 'w') as f:
# 		writer = csv.writer(f)
# 		writer.writerows(zip(strain, sequence))


if __name__ == "__main__": 
	print('hello')
	main()