from src.algorithm import mutation

def test_mutation_zero():
    genome =  list(range(1,101))
    genome_mutation = mutation.mutation(genome, 0.0)
    assert genome == genome_mutation

def test_mutation():
    genome =  list(range(1,101))
    genome_mutation = mutation.mutation(genome, 100)
    for gene in genome:
        for gene_mutation in genome_mutation:
            if gene != gene_mutation:
                assert True
    print(genome)
    print(genome_mutation)

def test_mutation_swap():
    genome = list(range(1, 101))
    genome_original = genome.copy()
    genome_mutation = mutation.mutation(genome, 1.0) 

    assert set(genome_original) == set(genome_mutation)

    diffs = [i for i, (a, b) in enumerate(zip(genome_original, genome_mutation)) if a != b]
    assert len(diffs) == 2

 
    i, j = diffs
    assert genome_original[i] == genome_mutation[j]
    assert genome_original[j] == genome_mutation[i]
