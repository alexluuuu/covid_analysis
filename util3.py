"""util3.py

"""

import Bio
import os 
import sys 
import numpy as np
import pandas as pd
import csv

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.Data import CodonTable


def main():

	df = pd.read_csv('/Users/noaferziger/covid_analysis/test.csv', header=None, names=["strain", "sequence"])
	print(df)
	sequence.translate(table=11)
	

	df['sequence'] = df['sequence'].map(sequence.translate(table=11))
	# print(df)

	# df['sequence'] = sequence.translate(df['sequence'])

	# with open('test2.csv', 'w') as f:
	# 	writer = csv.writer(f)
	# 	writer.writerows(zip(strain, sequence))

if __name__ == "__main__": 
	print('hello')
	main()