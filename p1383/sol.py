# This problem was asked by Triplebyte.

# You are given n numbers as well as n probabilities that sum up to 1. 
# Write a function to generate one of the numbers with its corresponding probability.

# For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2], 
# your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

# You can generate random numbers between 0 and 1 uniformly.

import random


class Solution:
    def __init__(self):
        pass
    
    def solve(self, arr, probs):
        '''
        generate uniform number x between [0, 1] and test what bucket x falls into.
        whatever bucket y that x falls into determines what number to return. 
        '''
        if len(arr) != len(probs):
            return RuntimeError(f'arr len ({len(arr)}) != probs len ({len(probs)})')
        
        if sum(probs) != 1.0:
            return RuntimeError(f'probs do not sum to 1.0, got {sum(probs)}')
        
        # create bucket cutoffs (strictly increasing values)
        bucket_cutoffs = []
        running_prob_sum = 0
        for prob in probs:
            running_prob_sum += prob
            bucket_cutoffs.append(running_prob_sum)

        # generate uniform number
        x = random.random()
        chosen_bucket_i = 0
        for i in range(len(bucket_cutoffs)):
            cutoff = bucket_cutoffs[i]
            if x < cutoff:
                chosen_bucket_i = i
                break

        return arr[chosen_bucket_i]
