from algorithm.hundred_prisioners_ga import HundredPrisonersGA

def main():
    ga = HundredPrisonersGA()
    best, best_fitness, num_generation = ga.run()

    print(f"The best Fitness {best_fitness:.2f}")
    print(f"Num Generation {num_generation}")
    print(f"Nums Boxes {best}")

if __name__ == "__main__":
    main()
