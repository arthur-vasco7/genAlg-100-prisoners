import random

from src.algorithm.hundred_prisioners_ga import HundredPrisonersGA

def test_initial_population_is_permutations():
    ga = HundredPrisonersGA(chromosome_length=10, population_size=20)
    population = ga._initial_population()
    assert len(population) == 20
    for individual in population:
        assert len(individual) == 10
        assert len(set(individual)) == 10  # sem repetições
        assert set(individual) == set(range(10))  # contém todos os genes esperados

def test_fitness_prisoners_on_identity_permutation():
    ga = HundredPrisonersGA(chromosome_length=10, population_size=1)
    identity = list(range(10))
    fitness = ga._fitness_prisoners([identity])
    # cada prisioneiro encontra seu número imediatamente -> 10 sucessos
    assert fitness == [10]

def test_fitness_target_mode():
    target = list(range(10))
    ga = HundredPrisonersGA(chromosome_length=10, population_size=1, fitness_mode="target", target=target)
    individual = list(range(10))
    fitness = ga.eval_fitness([individual])
    assert fitness == [10]

def test_cross_and_mutation_preserve_elements():
    ga = HundredPrisonersGA(chromosome_length=10, population_size=2, mutation_rate=1.0, crossover_rate=1.0)
    parent_a = list(range(10))
    parent_b = list(range(9, -1, -1))
    child = ga.cross(parent_a, parent_b)
    assert len(child) == 10
    assert set(child) == set(parent_a)  # mantém conjunto como permutação
    mutant = ga.mutation(child)
    assert set(mutant) == set(child)  # mutação por swap mantém elementos

def test_select_parents_returns_top_fraction():
    ga = HundredPrisonersGA(chromosome_length=6, population_size=6, parents_portion=0.5)
    # construir população com índices diferentes para diferenciar fitness
    pop = [list(range(6)), list(range(5, -1, -1)), list(range(6)), list(range(5, -1, -1)), list(range(6)), list(range(5, -1, -1))]
    fitness = ga.eval_fitness(pop)
    parents = ga.select_parents(pop, fitness)
    assert len(parents) == int(len(pop) * 0.5)
    # pais selecionados devem ser membros da população
    for p in parents:
        assert p in pop

def test_run_returns_expected_types_and_bounds():
    random.seed(0)
    ga = HundredPrisonersGA(chromosome_length=6, population_size=10, num_generations=3)
    best, best_fitness, generations = ga.run()
    assert (best is None) or isinstance(best, list)
    assert isinstance(best_fitness, int)
    assert isinstance(generations, int)
    # fitness nunca excede o comprimento do cromossomo
    assert best_fitness <= 6