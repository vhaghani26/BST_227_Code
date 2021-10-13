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

# Initialize the parameters randomly for theta0
# Set a random seed for troubleshooting/consistency in outputs
np.random.seed(0)

# Generate lambdas that are dependent on each other and sum to 1
def initialize_lambdas():
    lambda0 = np.random.random_sample()
    lambda1 = 1 - lambda0
    return lambda0, lambda1

# Generate the lambdas using the previous function
# Generate the psis that correspond to the frequencies for ['A', 'C', 'G', 'T'], where bp frequencies sum to 1 in each array
# Store all initialized parameters in a dictionary called 'params'
def initialize_random_params():
    lambdas = initialize_lambdas()
    params = {'psi0': np.random.dirichlet(np.ones(4),size=1),
              'psi1': np.random.dirichlet(np.ones(4),size=1),
              'lambda0': lambdas[0],
              'lambda1': lambdas[1]
              }
    return params

# Implement function
print(initialize_random_params())


##########################################


def e_step():
    # Set convergence criterion L_t = 1e -4 (or some other number)
    L_t = 1e-4
    # Set t = 1
    t = 1
    return L_t

# Implement function
print(e_step())





# Set L^(-1) = -(infinity)
# Set L^(0) = 0
# While L(^(t-1) - L^(t-2) > L_t
## For the current iteration t, compute posteriors based on the previous best estimate of the parameters theta^(t-1) by computing 
