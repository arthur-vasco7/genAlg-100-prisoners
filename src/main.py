from algorithm.hundred_prisoners_ga import HundredPrisonersGA

if __name__ == "__main__":
    ga = HundredPrisonersGA(
        chromosome_length=100, num_generations=100, stop_when_perfect_fitness=False
    )

    best_individual, best_fitness, generation = ga.genetic_algorithm()

    print("Best individual found:", best_individual)
    print("Best fitness:", best_fitness)
    print(f"Genereation {generation}")
