"""prediction.py

Wrapping functions, calls to mhcflurry 2.0
"""
import numpy as np
import pandas as pd
from mhcflurry import Class1PresentationPredictor


def prediction_whole_seq(protein_seqs, alleles, result_format="filtered", comparison_quantity="affinity", filter_value=500): 
	"""prediction_whole_seq 

	wraps the class1presentationpredictor from mhcflurry 2.0 for customizability
	
	Args:
	    protein_seqs (Dict): 	dictionary that maps a name like "protein_x": aa sequence
	    alleles (Dict): 		dictionary that maps a name like "sample_1": allele name
	    result_format (str, optional): 			Description
	    comparison_quantity (str, optional): 	Description
	    filter_value (int, optional): 			Description
	"""
	predictor = Class1PresentationPredictor.load()

	prediction_df = predictor.predict_sequences(
						sequences=protein_seqs,
						alleles=alleles,
						result=result_format,
						comparison_quantity=comparison_quantity,
						filter_value=filter_value,
						verbose=1
					)

	return prediction_df


def main(): 
	print("testing prediction.py") 


if __name__ == "__main__": 
	main()