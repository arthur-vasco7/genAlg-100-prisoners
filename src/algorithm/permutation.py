"""
permutation.py

Module responsible for generating the genetic representation
(using permutations) for a Genetic Algorithm applied to the
100 Prisoners Problem.

In this module, a genome is represented as a permutation of
the integers from 1 to 100, indicating the order in which boxes
should be opened during the simulation. The initial population
is composed of multiple individuals, each with its own randomly
generated genome.

Main functions:
- generate_permutation(): generates a permutation.
- generate_population(): generates a complete population.
"""

import random

def generate_permutation(size: int) -> list[int]:
    """
    Generates a permutation represented by a list of integers
    from 1 to size.

    The permutation is created by shuffling the base list,
    ensuring that each individual has a unique order of boxes
    to open

    Args:
        size (int): The size of the permutation (e.g. 100).

    Returns:
        list[int]: A random permutation containing all integers in the range [1, size]
    """
    perm = list(range(1, size+1))
    random.shuffle(perm)
    return perm

def generate_population(pop_size: int) -> list[list[int]]:
    """
    Creates an initial population containing multiple individuals,
    each with an independent genome.

    Args:
        pop_size (int): Number of individuals in the population.

    Returns:
        list[list[int]]: A list containing 'pop_size' genomes,
                         each one being a permutation of 1 to 100.
    """
    return [generate_permutation(50) for _ in range(pop_size)]
