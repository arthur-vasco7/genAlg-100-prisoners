"""Main module to run the 100 Prisoners GA algorithm."""


from algorithm.hundred_prisioners_ga import HundredPrisonersGA

def main():
    """Main entry point for running the 100 Prisoners GA algorithm."""
    ga = HundredPrisonersGA()
    best, best_fitness, num_generation = ga.run()

    print(f"The best Fitness {best_fitness:.2f}")
    print(f"Num Generation {num_generation}")
    print(f"Nums Boxes {best}")

if __name__ == "__main__":
    main()
