import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def observed(seq, k):
    counts = {}
    for i in range(len(seq) - k + 1):
        kmer = seq[i:i+k]
        if kmer not in counts:
            counts[kmer] = 0
        counts[kmer] += 1
    return len(counts)
def possible(seq,k):
	if k == 1:
		poss = 4**1
	else:
		if 4**k < (len(seq)):
			poss = 4**k
		else:
			poss = (len(seq)) - k + 1
	return poss
def lingProb(obs,poss):
	return obs/poss
def readFile():
	file_name=sys.argv[1]
	seq = []
	with open(file_name, "r") as ins:
		for line in ins:
			line = line.rstrip("\n")
			seq.append(line)
	return seq


def main():
	#read in sequences 
	seq = readFile()
	#loop for each sequence in text file
	for seqs in seq:
		# initilize data frame and lists 
		dataframe =	pd.DataFrame(columns=["k","Observed","Possible"])
		obsList = []
		possList = []
		k_list = []
		#loop over K 
		for k in range(1,len(seqs)+1):
			# calculate oberserved and possilbe and append to list 
			poss = possible(seqs,k)
			possList.append(poss)
			obs = observed(seqs,k)
			obsList.append(obs)
			k_list.append(k)
			# append each value to pandas dataframe 
			row = [k,obs,poss]
			dataframe = dataframe.append(pd.Series([k, obs, poss], index=dataframe.columns ), ignore_index=True)
		print(seqs)
		print(dataframe)
		#calculate linguistic prob
		x = sum(obsList)
		y = sum(possList)
		ling = lingProb(x,y)
		print(ling)

		#plot obs vs poss
		plt.plot(k_list, obsList, color='g')
		plt.plot(k_list, possList, color='orange')
		plt.xlabel('k')
		plt.ylabel('kmers')
		plt.show()
print("All sequences parsed")



main()

