from Chromosome import Chromosome
import numpy as np
import matplotlib.pyplot as plt
from fit import fit
from Reproduction import make_kids
POP_SIZE = 300
GENERATIONS = 100
def drive():
  fitnesses = []
  generation = create_pop(POP_SIZE) 
  change = 0
  mutation_rate = 0.1
  for i in range(GENERATIONS):
    fit(generation)
    gen_fitness = list(map(lambda x: x.get_fitness(), generation))
    for j in range(len(generation)):
      generation[j].set_fitness(gen_fitness[j])
    best_ind = gen_fitness.index(max(gen_fitness))
    best = generation[best_ind]
    worst_ind = gen_fitness.index(min(gen_fitness))
    worst = generation[worst_ind]
    avg = sum(gen_fitness) / len(gen_fitness)
    fitnesses.append(avg)
    if(i > 0):
      change = fitnesses[-1] - fitnesses[-2] / abs(fitnesses[-2])
    if(i > 50 and change > 0):
      mutation_rate /= 2
    print(f'Best: {best.get_fitness()}')
    print(best)
    print(f'Worst: {worst.get_fitness()}')
    print(f'Average Improvement: {change}')
    generation = make_kids(generation, mutation_rate)
  graphAVG(fitnesses)

def create_pop(pop_size):
  pop = []
  for _ in range(pop_size):
    pop.append(Chromosome())
  return pop

def graphAVG(fitnesses):
  x = np.arange(0, GENERATIONS)
  y = np.array(fitnesses)

  plt.plot(x, y)
  plt.show()

drive()