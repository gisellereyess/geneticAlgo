import Chromosome
import numpy as np
import fit
from Reproduction import make_kids
POP_SIZE = 20
GENERATIONS = 50
def drive():
  fitnesses = []
  generation = create_pop(POP_SIZE) 
  for i in range(GENERATIONS):
    fit(generation)
    # do math here
    # do output here
    generation = make_kids(generation)
def create_pop(pop_size):
  pop = []
  for _ in range(pop_size):
    pop.append(Chromosome())
  return pop