import pytest
from src.algorithm import permutation

def test_permutation_hundred():
    n = 100
    boxes = permutation.generate_permutation(n)
    assert len(boxes) == n
    assert set(boxes) == set(range(1, n +1))

def test_permutation_thousand():
    with pytest.raises(ValueError):
        permutation.generate_permutation(1000)

def test_permutation_zero():
    boxes = permutation.generate_permutation(0)
    assert boxes == []

def test_permutation_negative():
    with pytest.raises(ValueError):
        permutation.generate_permutation(-50)

    population = permutation.generate_population(100)
    assert len(population) == 100

def test_generate_population():
    population = permutation.generate_population(10)
    assert len(population) == 10
    for individual in population:
        assert len(individual) == 50
        assert all(1 <= x <= 100 for x in individual)

def test_population_thousand():
    population = permutation.generate_population(1000)
    assert len(population) == 1000
    for individual in population:
        assert len(individual) == 50
        assert len(set(individual)) == 50
        assert all(1 <= x <= 100 for x in individual)

def test_population_zero():
    population = permutation.generate_population(0)
    assert population == []

def test_population_negative():
    population = permutation.generate_population(-100)
    assert population == []

def test_generate_solution():
    sol = permutation.generate_solution()
    assert len(sol) == 100
    assert set(sol) == set(range(1, 101))