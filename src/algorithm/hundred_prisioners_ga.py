"""
Module implementing a Genetic Algorithm for the 100 Prisoners problem.

Contains the `HundredPrisonersGA` class with methods for:
- Initializing population
- Evaluating fitness
- Crossover and mutation
- Selecting parents
- Running the main GA loop
"""


import random

class HundredPrisonersGA:
    """Genetic algorithm for the 100 prisoners problem or a generic target permutation problem."""

    def __init__(
        self,
        chromosome_length=100,
        population_size=50,
        num_generations=100,
        mutation_rate=0.2,
        crossover_rate=0.8,
        parents_portion=0.4,
        elitism=True,
        stop_when_perfect_fitness=False,
        fitness_mode="prisoners",
        target=None,
    ):
        # === Algorithm configuration ===
        self._chromosome_length = chromosome_length
        self._population_size = population_size
        self._num_generations = num_generations
        self._mutation_rate = mutation_rate
        self._crossover_rate = crossover_rate
        self._parents_portion = parents_portion
        self._elitism = elitism
        self._stop_when_perfect_fitness = stop_when_perfect_fitness
        self._fitness_mode = fitness_mode  # 'prisoners' or 'target'
        self._target = target  # target permutation if using 'target' fitness

    def _initial_population(self):
        """Generate the initial population of random permutations."""
        population = []
        for _ in range(self._population_size):
            individual = list(range(self._chromosome_length))
            random.shuffle(individual)
            population.append(individual)
        return population

    def eval_fitness(self, population):
        """Evaluate fitness of a population according to the selected mode."""
        if self._fitness_mode == "prisoners":
            return self._fitness_prisoners(population)
        if self._fitness_mode == "target":
            if self._target is None:
                raise ValueError("Fitness mode 'target' selected but no target provided.")
            return self._fitness_target(population, self._target)
        raise ValueError("Invalid fitness mode.")

    def _fitness_prisoners(self, population):
        """Fitness evaluation for the 100 prisoners problem."""
        fitness_values = []
        for individual in population:
            successes = 0
            for prisoner in range(self._chromosome_length):
                box = prisoner
                for _ in range(self._chromosome_length // 2):
                    if individual[box] == prisoner:
                        successes += 1
                        break
                    box = individual[box]
            fitness_values.append(successes)
        return fitness_values

    def _fitness_target(self, population, target):
        """Fitness evaluation comparing individual to a target permutation."""
        fitness_values = []
        for individual in population:
            score = sum(1 for i in range(len(individual)) if individual[i] == target[i])
            fitness_values.append(score)
        return fitness_values

    def cross(self, gen_a, gen_b):
        """Create a child permutation by combining two parents without duplicates."""
        if len(gen_a) < 2 or len(gen_b) < 2:
            raise ValueError("Crossing requires at least 2 genes per individual.")
        if random.random() > self._crossover_rate:
            return gen_a.copy()
        size = len(gen_a)
        start = random.randint(0, size - 2)
        end = random.randint(start + 1, size - 1)
        child = gen_a[start:end]
        for gene in gen_b:
            if gene not in child:
                child.append(gene)
        return child

    def mutation(self, individual):
        """Apply swap mutation to a permutation."""
        mutant = individual.copy()
        if random.random() < self._mutation_rate:
            i, j = random.sample(range(len(mutant)), 2)
            mutant[i], mutant[j] = mutant[j], mutant[i]
        return mutant

    def select_parents(self, population, fitness_values):
        """Select top-performing individuals as parents."""
        n_parents = int(len(population) * self._parents_portion)
        sorted_population = [
            x for _, x in sorted(zip(fitness_values, population), reverse=True)
        ]
        return sorted_population[:n_parents]

    def generate_new_population(self, parents):
        """Generate new population using crossover, mutation, and optional elitism."""
        new_population = []
        if self._elitism:
            fitness_values = self.eval_fitness(parents)
            best_parent, _ = self.get_best(parents, fitness_values)
            new_population.append(best_parent.copy())
        while len(new_population) < self._population_size:
            parent1, parent2 = random.sample(parents, 2)
            child = self.cross(parent1, parent2)
            child = self.mutation(child)
            new_population.append(child)
        return new_population

    def get_best(self, population, fitness_values):
        """Return the best individual and its fitness in the population."""
        best_index = fitness_values.index(max(fitness_values))
        return population[best_index], fitness_values[best_index]

    # ==============================
    # MAIN ALGORITHM
    # ==============================
    def run(self):
        """Run the genetic algorithm until max generations or perfect fitness."""
        population = self._initial_population()
        count = 0
        generation = 0
        best_individual = None
        best_fitness = 0

        while generation < self._num_generations:
            fitness_values = self.eval_fitness(population)
            parents = self.select_parents(population, fitness_values)
            population = self.generate_new_population(parents)

            fitness_values = self.eval_fitness(population)
            current_best, current_fit = self.get_best(population, fitness_values)
            print(f"Generation {generation} | Best fitness: {current_fit}")
            print(f"Best individual: {current_best}")
            print("-" * 40)

            # Update global best
            if current_fit > best_fitness:
                best_individual, best_fitness = current_best, current_fit
                count = 0  # reset patience if improved
            else:
                count += 1

            # Stop early if perfect fitness reached and patience exceeded
            if self._stop_when_perfect_fitness and count >= 10:
                break

            generation += 1

        return best_individual, best_fitness, generation
