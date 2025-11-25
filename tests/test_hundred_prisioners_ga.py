"Tests for HundredPrisonersGA functions."
# pylint: disable=protected-access

import random

import pytest
from src.algorithm.hundred_prisioners_ga import HundredPrisonersGA

#Variavel structure
hp_ga = HundredPrisonersGA(
        chromosome_length=10,
        population_size=50,
        num_generations=100,
        mutation_rate=0.2,
        crossover_rate=0.8,
        parents_portion=0.4,
        elitism=True,
        stop_when_perfect_fitness=False,
        fitness_mode="prisoners",
        target=None)

def test_init_params():
    """Test parameter initialization."""
    ga_test = HundredPrisonersGA(
        chromosome_length=12,
        population_size=30,
        num_generations=200,
        mutation_rate=0.15,
        crossover_rate=0.7,
        parents_portion=0.3,
        elitism=False,
        stop_when_perfect_fitness=True,
        fitness_mode="target",
        target=[1,2,3]
    )

    assert ga_test._chromosome_length == 12
    assert ga_test._population_size == 30
    assert ga_test._num_generations == 200
    assert ga_test._mutation_rate == 0.15
    assert ga_test._crossover_rate == 0.7
    assert ga_test._parents_portion == 0.3
    assert ga_test._elitism is False
    assert ga_test._stop_when_perfect_fitness is True
    assert ga_test._fitness_mode == "target"
    assert ga_test._target == [1,2,3]

"Tests for population initialization in HundredPrisonersGA."

def test_initial_population_structure():
    "Test population size and chromosome structure."
    population = hp_ga._initial_population()

    assert len(population) == hp_ga._population_size
    for individual in population:
        assert len(individual) == hp_ga._chromosome_length
        assert set(individual) == set(range(hp_ga._chromosome_length))

def test_population_randomness():
    "Test that two generated populations are different."
    pop1 = hp_ga._initial_population()
    pop2 = hp_ga._initial_population()

    assert pop1 != pop2

"Tests for fitness in HundredPrisonersGA"

def test_fitness_target_perfect_match():
    "Tests that a perfect matching individual receives maximum fitness."
    target = list(range(10))
    population = [target.copy()]
    result = hp_ga._fitness_target(population, target)
    
    assert result == [10]

def test_fitness_target_no_match():
    "Tests that an individual with no matching positions receives zero fitness."
    target = list(range(10))
    population = [[x + 1 for x in target]]
    result = hp_ga._fitness_target(population, target)

    assert result == [0]

def test_fitness_target_partial_match():
    "Tests fitness computation when some positions match the target."
    target = [0, 1, 2, 3, 4]
    individual = [0, 9, 2, 8, 4]
    result = hp_ga._fitness_target([individual], target)

    assert result == [3]

def test_fitness_target_empty_population():
    "Tests behavior when the population is empty."
    target = list(range(10))
    result = hp_ga._fitness_target([], target)

    assert result == []

def test_fitness_target_multiple_individuals():
    """Tests multiple individuals evaluated against the same target."""
    target = [0, 1, 2, 3]

    population = [
        [0, 1, 2, 3],
        [0, 9, 2, 8],
        [9, 9, 9, 9]
    ]

    result = hp_ga._fitness_target(population, target)

    assert result == [4, 2, 0]

def test_fitness_target_random_statistical():
    "Statistical test: random individuals should match around 1 position on average for length 10."
    length = 10
    trials = 5000
    target = list(range(length))
    population = []

    for _ in range(trials):
        indiv = target.copy()
        random.shuffle(indiv)
        population.append(indiv)

    fitness = hp_ga._fitness_target(population, target)
    avg = sum(fitness) / trials

    assert 0.7 < avg < 1.5  # expected for random permutations

def test_fitness():
    "Tests whether a perfectly correct individual achieves maximum fitness."
    population = [list(range(hp_ga._chromosome_length))]

    fitness = hp_ga.eval_fitness(population)
    assert fitness == [hp_ga._chromosome_length]

def test_fitness_large_cycle():
    "Tests an individual that forms a single large cycle, preventing successful search."
    individual = list(range(1, hp_ga._chromosome_length)) + [0]
    fitness = hp_ga.eval_fitness([individual])

    assert fitness == [0]

def test_fitness_empty_population():
    "Tests behavior when the population is empty."
    fitness = hp_ga.eval_fitness([])

    assert not fitness

def test_fitness_valid_range():
    "Tests whether the returned fitness is within the expected range."
    individual = list(range(hp_ga._chromosome_length))
    fitness = hp_ga.eval_fitness([individual])

    assert 0 <= fitness[0] <= hp_ga._chromosome_length

def test_fitness_multiple():
    "Tests evaluation of multiple individuals simultaneously."
    pop = [
        list(range(hp_ga._chromosome_length)),                
        list(range(1, hp_ga._chromosome_length)) + [0],      
    ]

    fitness = hp_ga.eval_fitness(pop)
    assert fitness == [10, 0]

def test_fitness_statistical():
    """Statistical test: shuffles many individuals and checks the average fitness."""
    trials = 10000
    population = []

    # Generate many randomly shuffled individuals
    for _ in range(trials):
        indiv = list(range(hp_ga._chromosome_length))
        random.shuffle(indiv)
        population.append(indiv)

    fitness = hp_ga.eval_fitness(population)
    avg = sum(fitness) / trials

    # Expected average fitness for random permutations is between ~3 and ~6
    assert 3 < avg < 6

def test_eval_fitness_target_mode_valid():
    "Tests that eval_fitness correctly calls _fitness_target when mode is 'target'."
    hp_ga._fitness_mode = "target"
    hp_ga._target = [0, 1, 2, 3]

    population = [
        [0, 1, 5, 9],
        [0, 2, 2, 3]
    ]

    fitness = hp_ga.eval_fitness(population)

    assert fitness == [2, 3]

def test_eval_fitness_target_mode_missing_target():
    "Tests that eval_fitness raises an error when target mode is selected but no target is provided."
    hp_ga._fitness_mode = "target"
    hp_ga._target = None

    with pytest.raises(ValueError):
        hp_ga.eval_fitness([[1, 2, 3]])

def test_eval_fitness_invalid_mode():
    "Tests that eval_fitness raises an error when an invalid fitness mode is used."
    hp_ga._fitness_mode = "invalid_mode"

    with pytest.raises(ValueError):
        hp_ga.eval_fitness([[1, 2, 3]])

"Test for crossover in HundredPrisonersGA"

def test_crossover_low():
    "Tests that crossover does not occur when crossover rate is 0.0."
    hp_ga._crossover_rate = 0.0
    p1 = [0, 1, 2, 3, 4, 5]
    p2 = [5, 4, 3, 2, 1, 0]
    child = hp_ga.cross(p1, p2)

    assert child == p1
    assert child is not p1

def test_crossover_valid_permutation():
    "Tests that full crossover produces a valid permutation."
    hp_ga._crossover_rate = 1.0
    p1 = [0, 1, 2, 3, 4, 5]
    p2 = [5, 4, 3, 2, 1, 0]
    child = hp_ga.cross(p1, p2)

    assert len(child) == len(p1)
    assert set(child) == set(p1)

def test_crossover_order_preserved():
    "Tests that crossover output contains no duplicated or missing genes."
    hp_ga._crossover_rate = 1.0
    p1 = [0, 1, 2, 3, 4, 5]
    p2 = [5, 0, 4, 1, 3, 2]
    child = hp_ga.cross(p1, p2)

    for gene in child:
        assert child.count(gene) == 1

def test_crossover_probabilistic():
    "Tests that probabilistic crossover generates diverse children."
    hp_ga._crossover_rate = 0.5
    p1 = [0, 1, 2, 3, 4, 5]
    p2 = [5, 4, 3, 2, 1, 0]
    results = {tuple(hp_ga.cross(p1, p2)) for _ in range(10000)}

    assert len(results) > 1

def test_crossover_identical_parents():
    "Tests that crossover with identical parents returns a valid permutation."
    hp_ga._crossover_rate = 1.0
    p = [0, 1, 2, 3, 4, 5]
    child = hp_ga.cross(p, p)

    assert set(child) == set(p)

"Tests mutation in HundredPrisonersGA"

def test_mutation_zero():
    "Tests that mutation does nothing when mutation_rate is 0.0."
    genome = list(range(1, 101))
    hp_ga._mutation_rate = 0.0
    mutated = hp_ga.mutation(genome.copy())

    assert mutated == genome

def test_mutation_always_swaps():
    "Tests that mutation with rate 1.1 performs exactly one swap in the genome."
    hp_ga._mutation_rate = 1.0
    genome = list(range(1, 101))
    mutated = hp_ga.mutation(genome.copy())
    diffs = [i for i, (a, b) in enumerate(zip(genome, mutated)) if a != b]

    assert set(mutated) == set(genome)
    assert len(diffs) == 2

    i, j = diffs
    assert genome[i] == mutated[j]
    assert genome[j] == mutated[i]

def test_mutation_changes_rate_high():
    "Tests that mutation_rate = 1.1 always produces a genome different from the original."
    hp_ga._mutation_rate = 1.0
    genome = list(range(1, 101))
    mutated = hp_ga.mutation(genome.copy())

    assert mutated != genome

"Tests for select parentes in HundredPrisonersGA"

def test_select_parents_correct_count():
    "Tests that select_parents returns the correct number of parents."
    hp_ga._parents_portion = 0.5
    population = ["A", "B", "C", "D"]
    fitness =     [10,  20,  30,  40]
    parents = hp_ga.select_parents(population, fitness)

    assert len(parents) == 2
    assert parents == ["D", "C"]

def test_select_parents_sorted_by_fitness():
    "Tests that parents are selected in descending fitness order."
    hp_ga._parents_portion = 1.0
    population = ["A", "B", "C", "D"]
    fitness =     [10,  20,  30,  40]
    parents = hp_ga.select_parents(population, fitness)

    assert parents == ["D", "C", "B", "A"]

def test_select_parents_alignment():
    "Tests that selection keeps correct alignment between individuals and their fitness."
    hp_ga._parents_portion = 0.5
    population = [["ind0"], ["ind1"], ["ind2"], ["ind3"]]
    fitness =     [  5,       50,       10,       40    ]
    parents = hp_ga.select_parents(population, fitness)

    assert parents == [["ind1"], ["ind3"]]

def test_select_parents_zero_portion():
    "Tests that parents_portion = 0.0 yields an empty parent list."
    hp_ga._parents_portion = 0.0
    population = [1, 2, 3]
    fitness =    [5, 4, 3]
    parents = hp_ga.select_parents(population, fitness)

    assert parents == []

def test_select_parents_equal_fitness():
    "Tests that when all fitness values are equal, all individuals are selected."
    hp_ga._parents_portion = 1.0
    population = ["A", "B", "C"]
    fitness =     [10, 10, 10]
    parents = hp_ga.select_parents(population, fitness)

    assert set(parents) == set(["A", "B", "C"])

"Tests for population elitism in HundredPrisonersGA"

def test_generate_new_population_elitism_preserves_best():
    "Tests that elitism preserves the best parent as the first individual."
    hp_ga._fitness_mode = "prisoners"
    hp_ga._elitism = True
    hp_ga._population_size = 5
    parents = [list(range(50)), list(range(50)), list(range(50))]
    fitness = [0, 1, 2]

    best_parent, _ = hp_ga.get_best(parents, fitness)
    new_population = hp_ga.generate_new_population(parents)

    assert new_population[0] == best_parent

def test_generate_new_population_size():
    "Tests that the generated population has the configured population size."
    hp_ga._elitism = False
    hp_ga._population_size = 10
    parents = [list(range(5)) for _ in range(5)]

    new_population = hp_ga.generate_new_population(parents)

    assert len(new_population) == 10

def test_generate_new_population_no_elitism():
    "Tests that without elitism, the first individual is not guaranteed to be the best parent."
    hp_ga._elitism = False
    hp_ga._population_size = 5
    parents = [list(range(50)), list(range(50)), list(range(50))]

    new_population = hp_ga.generate_new_population(parents)

    assert new_population[0] not in parents or new_population[0] != parents[2]

def test_generate_new_population_elitism_parent_not_modified():
    "Tests that elitism does not modify the best parent during reproduction."
    hp_ga._elitism = True
    hp_ga._population_size = 5
    parents = [list(range(50)), list(range(50)), list(range(50))]
    fitness = [0, 2, 1]

    best_parent, _ = hp_ga.get_best(parents, fitness)
    best_copy_before = best_parent.copy()

    new_population = hp_ga.generate_new_population(parents)

    assert new_population[0] == best_copy_before
    assert best_parent == best_copy_before

def test_generate_new_population_children_are_modified():
    "Tests that generated children differ from the original parents."
    hp_ga._elitism = False
    hp_ga._population_size = 5
    parents = [[0, 1, 2, 3], [3, 2, 1, 0]]

    new_population = hp_ga.generate_new_population(parents)

    assert any(child not in parents for child in new_population)

def test_generate_new_population_two_parents_only():
    "Tests that two parents can generate a full new population."
    hp_ga._elitism = False
    hp_ga._population_size = 5
    parents = [[0, 1, 2, 3], [3, 2, 1, 0]]

    new_population = hp_ga.generate_new_population(parents)

    assert len(new_population) == 5

"Tests for get best individual in HundredPrisonersGA"

def test_get_best_correct():
    "Tests that get_best returns the individual with the highest fitness."
    population = ["A", "B", "C"]
    fitness =    [10, 50, 20]
    best_ind, best_fit = hp_ga.get_best(population, fitness)

    assert best_ind == "B"
    assert best_fit == 50

def test_get_best_tie():
    "Tests that get_best selects the first individual in case of a fitness tie."
    population = ["A", "B", "C"]
    fitness =    [30, 50, 50]
    best, fit = hp_ga.get_best(population, fitness)

    assert best == "B"
    assert fit == 50

"Tests for run in HundredPrisonersGA"

def test_ga_basic_run():
    "Tests that the genetic algorithm returns valid types for best individual, fitness, and generation."
    ga = HundredPrisonersGA(
        population_size=4,
        chromosome_length=3,
        num_generations=5,
        parents_portion=0.5,
        mutation_rate=0.0,
        stop_when_perfect_fitness=False,
        elitism=False
    )

    best_ind, best_fit, gen = ga.run()

    assert isinstance(best_ind, list)
    assert isinstance(best_fit, int)
    assert isinstance(gen, int)

def test_ga_monotonic_improvement():
    "Tests that the best fitness stays within the valid bounds and that all generations run when early stop is disabled."
    ga = HundredPrisonersGA(
        population_size=5,
        chromosome_length=3,
        num_generations=10,
        parents_portion=0.5,
        mutation_rate=0.0,
        stop_when_perfect_fitness=False,
        elitism=True
    )

    _, best_fit, gen = ga.run()

    assert 0 <= best_fit <= 3
    assert gen == 10

def test_ga_early_stop():
    "Tests that the GA stops early once perfect fitness is reached when early-stop is enabled."
    ga = HundredPrisonersGA(
        population_size=5,
        chromosome_length=3,
        num_generations=50,
        parents_portion=1.0,
        mutation_rate=0.0,
        stop_when_perfect_fitness=True,
        elitism=True
    )

    _, _, gen = ga.run()

    # Expected to stop at generation 10 due to perfect fitness
    assert gen == 10

def test_ga_generation_counter_full_run():
    "Tests that the GA completes all generations when early-stop is disabled."
    ga = HundredPrisonersGA(
        population_size=4,
        chromosome_length=3,
        num_generations=7,
        parents_portion=0.5,
        mutation_rate=0.1,
        stop_when_perfect_fitness=False,
        elitism=True
    )

    _, _, gen = ga.run()

    assert gen == 7
