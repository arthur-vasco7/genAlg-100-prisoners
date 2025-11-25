from src.algorithm.hundred_prisioners_ga import HundredPrisonersGA


def test_disposition_is_permutation_of_100():
    ga = HundredPrisonersGA(chromosome_length=100, population_size=1)
    disposition = ga._initial_population()[0]
    assert len(disposition) == 100
    assert len(set(disposition)) == 100


def test_population_is_list_of_permutations():
    ga = HundredPrisonersGA(chromosome_length=100, population_size=100)
    population = ga._initial_population()
    assert len(population) == 100
    for individual in population:
        assert len(individual) == 100
        assert len(set(individual)) == 100
