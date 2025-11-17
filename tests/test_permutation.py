from src.algorithm import permutations

def test_permutation():
    boxes = permutations.newDisposition()
    assert len(boxes) == 100
    assert len(set(boxes)) == 100
    

def test_population():
    prisoners = permutations.newPopulation()
    assert len(prisoners) == 100
    for prison in prisoners:
        assert len(set(prison)) == 50
