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

# novo genoma (conjunto de 100 estratégias) aleatório
def newGenome() -> [[int]]:
    population = []
    for k in range(100):
        population.append(generatePermutation(50))

    return population

# nova disposição das caixas na sala
# codigo morto no momento, nao necessario para verificar acerto
def newDisposition() -> [int]:
    return generatePermutation(100)

if (__name__ == "__main__"):
    print(newDisposition())
