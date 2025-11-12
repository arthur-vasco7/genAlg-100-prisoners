# arquivo gerador de permutações aleatórias usadas tanto para representar a estratégia de 1 indivíduo como a disposição real das caixas.
import random

# tamanho 50: prisioneiro
# tamanho 100: caixas da sala
def generatePermutation(size: int) -> [int]:
    perm = []

    i = 0
    while i < size:
        num = random.randint(1,100)

        if num not in perm:
            perm.append(num)
            i += 1

    return perm

# nova população aleatória
def newPopulation() -> [[int]]:
    population = []
    for k in range(100):
        population.append(generatePermutation(50))

    return population

# nova disposição das caixas na sala
def newDisposition() -> [int]:
    return generatePermutation(100)

print(newDisposition())

# usar dicionario mapeando tag ou lista usando indice+1 ?
# jogar em um arquivo
