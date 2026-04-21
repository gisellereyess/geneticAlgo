from Chromosome import Chromosome
import numpy as np
import matplotlib.pyplot as plt
import scipy
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
    #get fitness
    fit(generation)
    #put fitnesses into list
    raw_fitness = list(map(lambda x: x.get_fitness(), generation))
    #find the best schedule
    best_ind = raw_fitness.index(max(raw_fitness))
    best = generation[best_ind]
    #find the worst schedule
    worst_ind = raw_fitness.index(min(raw_fitness))
    worst = generation[worst_ind]
    #compute average from raw fitnesses
    avg = sum(raw_fitness) / len(raw_fitness)
    fitnesses.append(avg)
    #find change in average fitness
    if(i > 0):
      change = (fitnesses[-1] - fitnesses[-2]) / abs(fitnesses[-2])
    #half the mutation rate if we're over 50 generations and increasing average fitness
    if(i > 50 and change > 0):
      mutation_rate /= 2
    print(best)
    print(f'Best: {best.get_fitness()}')
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