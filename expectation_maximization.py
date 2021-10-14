#!/usr/bin/env python3

# Usage: 'python3 expectation_maximization.py --file sample_data_mle.txt'

import argparse
import numpy as np
import math

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

print(f'My sequences are {my_seqs}')
            
# Make a one-hot encoded 3D matrix X_{ijk} 
# ['A', 'C', 'G', 'T'] corresponds to the indexing of the matrices 
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

# Implement function to ensure that it works as intended
my_matrix = make_matrix(my_seqs)
print(my_matrix)

# Initialize the parameters randomly for params0 (theta0)
# Set a random seed for troubleshooting/consistency in outputs
np.random.seed(0)

# Generate lambdas that are dependent on each other and sum to 1
def initialize_lambdas():
    lambda0 = np.random.random_sample()
    lambda1 = 1 - lambda0
    return lambda0, lambda1

# Generate the lambdas using the previous function
# Generate the psis that correspond to the frequencies for ['A', 'C', 'G', 'T'], where bp frequencies sum to 1 in each array
# Store all initialized parameters in a dictionary called 'params' (params = theta)
def initialize_random_params():
    lambdas = initialize_lambdas()
    params = {'psi0': (np.random.dirichlet(np.ones(4),size=1)).tolist(),
              'psi1': (np.random.dirichlet(np.ones(4),size=1)).tolist(),
              'lambda0': lambdas[0],
              'lambda1': lambdas[1]
              }
    return params

# Implement function to ensure that it works as intended
my_params = initialize_random_params()
print(f'My initialized parameters are {my_params}')

# Compute posterior for one iteration
# If we set q(C) equal to the posterior calculation, then the KL term can become zero
def compute_posterior(params):
    posterior_probabilities = []
    # Range corresponds to base pair identity, which translates to specific indices of psi
    for i in range(0,4):
        posterior = (params['lambda1']*params['psi1'][0][i])/((params['lambda0']*params['psi0'][0][i])+(params['lambda1']*params['psi1'][0][i]))
        posterior_probabilities.append(posterior)
    return posterior_probabilities

# Implement function to ensure that it works as intended
my_posterior = compute_posterior(my_params)
print(f'My posterior probabilities are {my_posterior}')

##########################################

def e_step():
    # t is the number of steps
    # Set t = 1
    t = 1
    # L is the ELBO
    # Set convergence criterion L_t = 1e -4 (or some other number)
    L_t = 1e-4
    # Set L^(0) = 0
    L_t_1 = 0
    # Set L^(-1) = -(infinity)
    L_t_2 = -math.inf
    # While L(^(t-1) - L^(t-2) > L_t, for the current iteration t, compute posteriors based on the previous best estimate of the parameters params^(t-1) by computing q_t(C) = P(C|X, theta(t-1))
    # Note the posterior of C depends on a specific set of parameter values theta
    while (L_t_1 - L_t_2) > L_t:
        for i in range(0,t):
            # Used as placeholder
            v = 7
        # Break while loop for now since we don't have multiple iterations yet
        break
    # Return placeholder to test function
    return v

# Implement function to ensure that it works as intended
my_e_step = e_step()
print(my_e_step)        
    
'''
Scratch code:

# Number of sequences
num_seqs = len(seqs)
# Sequence length
seq_length = len(seqs[0])
my_matrix = make_matrix(seqs)
#for i, seq in enumerate(seqs):
#    for j in range(seq_length):

def m_step():
    return 1
    
def run_em():
    return 1
'''