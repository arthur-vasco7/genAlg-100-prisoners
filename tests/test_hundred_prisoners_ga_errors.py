import random
import pytest

from src.algorithm.hundred_prisioners_ga import HundredPrisonersGA

def test_eval_fitness_target_without_target_raises():
    ga = HundredPrisonersGA(fitness_mode="target", target=None)
    population = [[0]]
    with pytest.raises(ValueError, match="Fitness mode 'target' selected but no target provided"):
        ga.eval_fitness(population)

def test_eval_fitness_invalid_mode_raises():
    ga = HundredPrisonersGA(fitness_mode="invalid_mode")
    population = [[0, 1, 2]]
    with pytest.raises(ValueError, match="Invalid fitness mode"):
        ga.eval_fitness(population)

def test_generate_new_population_with_insufficient_parents_raises():
    # quando há menos de 2 pais, random.sample(parents, 2) deve levantar ValueError
    ga = HundredPrisonersGA(chromosome_length=3, population_size=5, elitism=False)
    parents = [[0, 1, 2]]  # apenas 1 pai
    with pytest.raises(ValueError):
        ga.generate_new_population(parents)


def test_get_best_with_empty_lists_raises():
    ga = HundredPrisonersGA()
    with pytest.raises(ValueError):
        ga.get_best([], [])


def test_cross_single_gene_raises():
    ga = HundredPrisonersGA()
    with pytest.raises(ValueError):
        ga.cross([0], [0])


def test_mutation_single_gene_raises():
    # Forçar branch de mutação e tamanho 1 -> random.sample deve falhar
    ga = HundredPrisonersGA(chromosome_length=1, mutation_rate=1.0)
    random.seed(0)
    with pytest.raises(ValueError):
        ga.mutation([0])
