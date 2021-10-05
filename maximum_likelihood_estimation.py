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
#import numpy as np

# Setup
parser = argparse.ArgumentParser(
	description='Implements maximum likelihood estimation given sequence data')

# Required arguments
parser.add_argument('--file', required=True, type=str,
	metavar='<path>', help='Text file containing the DNA sequences')

# Finalization 
arg = parser.parse_args()

# Read in text file containing sequences and add each sequence to a list
seqs = []
with open(arg.file, 'r') as a_file:
    for line in a_file:
        if not line.lstrip().startswith('#'):
            new_line = line.upper()
            seqs.append(new_line[:-1])
    print(seqs)
           
# Write a function to generate the matrix
#def make_matrix(seqs):
example_list = [1, 2, 3, 4]
def sample_function(sample_list):
    for i in sample_list:
        print(i)

sample_function(example_list)


'''
for seq in seqs:
    for i, v in enumerate(seq):
        if v == 'A':
            print(v, 'This is an A')
        elif v == 'C':
            print(v, 'This is a C')
        elif v == 'G':
            print(v, 'This is a G')
        elif v == 'T':
            print(v, 'This is a T')
        else:
            print('Unknown base pair in sequence. Please ensure that only A, C, G, or T are present')
        print(i, v)
'''


# Write a function to do the Boolean part