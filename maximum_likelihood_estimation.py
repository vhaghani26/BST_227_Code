#!/usr/bin/env python3

## Instructions
# Write a program that implements the maximum likelihood estimation (MLE)
# Write some code to take in a file of sequences, and produce the matrix X_{ijk}
# Assume the text file input is going to be a set of N sequences (one per line, all of the same length, with the characters A, C, G, and T)
# In X_{ijk}
# i is the sequence number (sequence 1, 2, ..., n) 
# j is the index of the sequence (first position of the ith sequence)
# k is the assigned value of the base pair at the jth position in the ith sequence

## Usage
# python3 maximum_likelihood_estimation.py --file sample_data_mle.txt

import argparse
import numpy as np

# Setup
parser = argparse.ArgumentParser(
	description='Implements maximum likelihood estimation given sequence data')

# Required arguments
parser.add_argument('--file', required=True, type=str,
	metavar='<path>', help='Text file containing the DNA sequences')

# Finalization 
arg = parser.parse_args()

# Read in text file containing sequences and add each sequence to a list
my_seqs = []
with open(arg.file, 'r') as a_file:
    for line in a_file:
        if not line.lstrip().startswith('#'):
            new_line = line.upper()
            my_seqs.append(new_line[:-1])
    print(my_seqs)

# Make a one-hot encoded 3D matrix X_{ijk} 
def make_matrix(seqs):
    # Determine how many input sequences we have
    num_seqs = len(seqs)
    # Determine the length of each sequence
    # Based on instructions, all sequences are equal length
    # Therefore, we can assume the length of the first sequence is equal to the length of each sequence
    seq_length = len(seqs[0])
    matrix = np.zeros((num_seqs, seq_length, 4), dtype = int)
    for i, seq in enumerate(seqs):
        for j in range(seq_length):
            if seq[j] == 'A':
                matrix[i][j] = [1, 0, 0, 0]
            elif seq[j] == 'C':
                matrix[i][j] = [0, 1, 0, 0]
            elif seq[j] == 'G':
                matrix[i][j] = [0, 0, 1, 0]
            elif seq[j] == 'T':
                matrix[i][j] = [0, 0, 0, 1]
            else:
                print('Unknown base pair in sequence. Please ensure that only A, C, G, or T are present')
    return matrix

# Implement function
my_matrix = make_matrix(my_seqs)
print(my_matrix)