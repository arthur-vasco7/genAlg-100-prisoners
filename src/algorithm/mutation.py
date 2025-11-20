"""
mutation.py

Module responsible for the mutation operation of the genetic algorithm.

Functions:
- mutate(): applies mutation to a genome.
"""

import random

def mutation(genome: list[int], mutation_rate: float) -> list[int]:
    """
    Applies a swap mutation to a genome representing a permutation.

    Args:
        genome (list[int]): The permutation to be mutated.
        mutation_rate (float): Probability (0-1) of applying mutation.

    Returns:
        list[int]: The mutated genome.
    """
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(genome)), 2)
        genome[i], genome[j] = genome[j], genome[i]
    
    return genome