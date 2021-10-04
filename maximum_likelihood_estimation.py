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

# Read in text file containing sequences
with open('sample_data_mle.txt', 'r') as f:
    lines = f.readlines()
    print(lines)


