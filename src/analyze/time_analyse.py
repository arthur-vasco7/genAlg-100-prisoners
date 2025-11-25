import time
import contextlib
import io


f = io.StringIO()




from src.algorithm.hundred_prisioners_ga import HundredPrisonersGA


cargas = [10, 50, 100, 200]
repeticoes = 5

#com elitistmo, com 100 geracoes
print("Com elitismo")
for n in cargas:
    tempos = []
    for _ in range(repeticoes):
        ga = HundredPrisonersGA(chromosome_length=n, population_size=50, num_generations=100, elitism=True)
        start = time.time()
        with contextlib.redirect_stdout(f):
            ga.run()

        end = time.time()
        tempos.append(end - start)
    
    media = sum(tempos)/repeticoes
    print(f"Carga {n}: tempo médio = {media:.4f} s")

print("Sem elitismo")
#sem elitismo, com 100 geracoes
for n in cargas:
    tempos = []
    for _ in range(repeticoes):
        ga = HundredPrisonersGA(chromosome_length=n, population_size=50, num_generations=100, elitism=False)
        start = time.time()
        with contextlib.redirect_stdout(f):
            ga.run()
        end = time.time()
        tempos.append(end - start)
    
    media = sum(tempos)/repeticoes
    print(f"Carga {n}: tempo médio = {media:.4f} s")


print("Com Stop")
for n in cargas:
    tempos = []
    for _ in range(repeticoes):
        ga = HundredPrisonersGA(chromosome_length=n, population_size=50, num_generations=100, stop_when_perfect_fitness=True)
        start = time.time()
        with contextlib.redirect_stdout(f):
            ga.run()

        end = time.time()
        tempos.append(end - start)
    
    media = sum(tempos)/repeticoes
    print(f"Carga {n}: tempo médio = {media:.4f} s")


print("Sem Stop")
for n in cargas:
    tempos = []
    for _ in range(repeticoes):
        ga = HundredPrisonersGA(chromosome_length=n, population_size=50, num_generations=100,stop_when_perfect_fitness=False)
        start = time.time()
        with contextlib.redirect_stdout(f):
            ga.run()
        end = time.time()
        tempos.append(end - start)
    
    media = sum(tempos)/repeticoes
    print(f"Carga {n}: tempo médio = {media:.4f} s")




