# fintess function para avaliar a aptidão das soluções
import permutation

# verifica se um prisioneiro achou seu proprio numero em uma disposiçao de caixas
def found_box(id: int, prisoner: [int], boxes: [int]) -> bool:
    for guess in prisoner:
        if (boxes[guess-1] == id):
            return True
    return False

# avalia a estrategia de cada prisioneiro, contando em quantas disposiçoes aleatorias eles passaram
def eval(population: [[int]], rounds: int) -> [int]:
    scores = [0 for _ in range(len(population))]
    
    for _ in range(rounds):
        current = permutation.generate_solution()
        for p in range(len(population)):
            if found_box(p+1, population[p], current):
                scores[p] += 1

    return scores

# seleciona as estrategias com maior acerto apos varios rounds de teste
def select(population: [[int]], elite_size: int) -> [int]:
    scores = eval(population, 500)
    elite = []

    i = 0
    while i < elite_size:
        max = 0
        index = 0
        for j in range(len(scores)):
            if (scores[j] > max):
                max = scores[j]
                index = j
        
        elite.append(index)
        scores[index] = 0
        i += 1

    return elite

# main para testes manuais
if (__name__ == "__main__"):
    pop = permutation.generate_population(100)
    
    print(eval(pop, 500))
    exit()

    curr = select(pop, 50)
    print(curr)
        
    t = 0
    f = 0
    for e in curr:
        if (found_box(e-1, pop[e], permutation.generate_solution())):
            t += 1
        else:
            f += 1

    print(t)
    print(f)

