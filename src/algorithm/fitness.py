# fintess function para avaliar a aptidão das soluções
import permutations

def countPrisoners(population: [[int]]) -> float:
    acc = 0
    for i in range(len(population)):
        if (i+1 in population[i]):
            acc += 1

    return acc/100

if (__name__ == "__main__"):
    print(countPrisoners(permutations.newGenome()))

