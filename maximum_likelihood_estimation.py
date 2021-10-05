#!/usr/bin/env python3

## Instructions
# Write a program that implements the maximum likelihood estimation (MLE)
# Write some code to take in a file of sequences, and produce the matrix X_{ijk}
# Assume the text file input is going to be a set of N sequences (one per line, all of the same length, with the characters A, C, G, and T)

## Usage
# python3 maximum_likelihood_estimation.py --file sample_data_mle.txt

import argparse

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
            seqs.append(line[:-1])
    print(seqs)

# Make a dictionary containing the base pair and corresponding numeric value
bp_vals = {'A': 1, 'a': 1,
           'C': 2, 'c': 2,
           'G': 3, 'g': 3,
           'T': 4, 't': 4}
           
# In X_{ijk}
# i is the sequence number (sequence 1, 2, ..., n) 
# j is the index of the sequence (first position of the ith sequence)
# k is the assigned value of the base pair at the jth position in the ith sequence