#!/usr/bin/env python3

# Usage: 'python3 expectation_maximization.py --file sample_data_mle.txt'

import argparse
import numpy as np

# Setup
parser = argparse.ArgumentParser(
	description='Implements expectation maximization algorithm')

# Required arguments
parser.add_argument('--file', required=True, type=str,
	metavar='<path>', help='Text file containing  DNA sequences')

# Finalization 
arg = parser.parse_args()

# Read in text file containing sequences and add each sequence to a list
my_seqs = []
with open(arg.file, 'r') as a_file:
    for line in a_file:
        if not line.lstrip().startswith('#'):
            new_line = line.upper()
            my_seqs.append(new_line[:-1])

##########################################

# Initialize the parameters randomly for theta0
def initialize_lambdas():
    lambda0 = np.random.random_sample()
    lambda1 = 1 - lambda0
    return lambda0, lambda1

def initialize_random_params():
    params = {'psi0': np.random.dirichlet(np.ones(4),size=1),
              'psi1': np.random.dirichlet(np.ones(4),size=1),
              'lambda0': initialize_lambdas()[0],
              'lambda1': initialize_lambdas()[1]
              }
    return params

my_dict = initialize_random_params()
print(my_dict)
