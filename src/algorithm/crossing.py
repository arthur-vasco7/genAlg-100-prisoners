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

