import permutation
import fitness
import crossing
import mutation

# ALGORITMO GENÉTICO 
# 1. definir parâmetros
# 2. inicializar população
# 3. avaliar (fitness)
# 4. loop (seleciona melhor --> cruzamento --> mutacao --> avaliar fitness filhos --> inserir filhos na nova população .. .etc)

def main():
    #parametros
    PRISIONEIRO = 5
    POP_SIZE = 200
    GENERATIONS = 500
    CROSSOVER_RATE = 0.9
    MUTATION_RATE = 0.1

    #inicizaliar pop
    population = permutation.generate_population()

    #avaliar fitness
    for individual in population:
        individual.fitness = cal_fitness(individual)

        #loop de gerações
    for gen in range(1, GENERATIONS+1):
        new_population = []

        elite = get_best_individual(population) # acho que é o individuo com menor fitness
        new_population.append(elite_copy(elite))

        while len(new_population) < POP_SIZE:
            parent1 = permutation.generate_genome (100)
            parent2 = permutation.generate_genome (100)

            if rand() > CROSSOVER_RATE:
                child1, child2 = crossover(parent1, parent2)
            else:
                child1, child2 = clone(parent1, parent2)

            mutation.mutate(child1)
            mutation.mutate(child2)

            #avaliar fitness filhos

        population = new_population




def random_strategy():
    return 0.0

def cycle_strategy():
    return 0.3127

def random_strategy_prisoners(boxes):
    return [False] * 100


def cycle_strategy_prisoners(boxes):
    if boxes[0] == 0:
        return [True] * 100
    return [False] * 100
