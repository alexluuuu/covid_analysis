"""test_cluster_script.py

Test batch runs of 
"""
import os 
import numpy as np
import sys 


def main():
	allele_list_path = "test_allele_list.txt"
	path_to_netmhc = "/home-1/alu27@jhu.edu/prototype/covid_analysis/netMHC-4.0/netMHC"
	size = 20
	with open(allele_list_path, 'r') as f:
		alleles = list(f.read().splitlines()) 
		for i, pos in enumerate(range(0, len(alleles), size)): 
			for prot in ['test_ref', 'test_Spike']:
				allele_str = ",".join(alleles[pos:pos+size])
				cluster_call_base = "sbatch -c 2 -t 4:0:0 -p shared --mail-type=begin --mail-type=end --mail-user=alu27@jhu.edu "
				cluster_call_base += " --job-name=netmhc_%s_%d "%(prot, i)
                                cluster_call_base += " --output=output/%s_%d.o "%(prot, i)
                                cluster_call_base += " --error=output/error/%j.e "

				cluster_call_base += path_to_netmhc
				cluster_call_base += " -l 8,9,10,11,12 -s " 
				cluster_call_base += " -a %s "%(allele_str)
                                # cluster_call_base += "-xls 1 -xlsfile output/%s_%d.xls "%(prot, i)
                                cluster_call_base += " data/%s.fasta"%(prot)
				print(cluster_call_base)
				# os.system(cluster_call_base)

if __name__ == "__main__": 
	main()
