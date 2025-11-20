import random


def cross(genA: [[int]], genB: [[int]]) -> ([[int]], [[int]]):
    # limiares de escolha definidos para forçar ao menos 1 troca sempre
    start = random.randint(0, 99)
    end = random.randint(start+1, 100)

    aux = genA[start:end]
    
    # novos genes formados a partir da troca de informações
    newGenA = genA[0:start] + genB[start:end] + genA[end:100]
    newGenB = genB[0:start] + aux + genB[end:100]
    
    return (newGenA, newGenB)


def mutation(gen: [[int]]) -> [[int]]:
    # escolhe dois índices diferentes para trocar
    first = random.randint(0, 99)

    while True:
        second = random.randint(0, 99)
        if second != first:
            break

    # troca simples (swap)
    gen[first], gen[second] = gen[second], gen[first]

    return gen


