from data import *
import Chromosome
import random

# Creates the new generation. pass in old gen as population
# Mutation rate is a float 0<=x<=1.0
def make_kids(population, mutation_rate = .1):
  kids = []
  parents = get_parents(population)
  # breed parents
  for i in range(0, len(parents), 2):
    child_1, child_2 = crossover(parents[i], parents[i + 1])
    kids.append(child_1)
    kids.append(child_2)
  # mutate kids
  for kid in kids:
    mutate(kid, mutation_rate)
  return parents + kids

# Create a list of parents using tournament selection
def get_parents(population):
  parents = []
  for _ in range(len(population) // 2):
    parents.append(tournament_selection(population))
  return parents

# Run tournament selection, return the winning parent
def tournament_selection(population, k=3):
  tournament_pop = random.sample(population, k)
  tournament_pop = sorted(tournament_pop, key=lambda x: x.get_fitness(), reverse=True)
  return tournament_pop[0]

# Do one point crossover on two parents, return the two children created
def crossover(parent_A, parent_B):
  threshold = random.randint(1, NUM_CLASSES - 1)
  this_teachers_1 = parent_A.get_teacher_list()[:threshold] + parent_B.get_teacher_list()[threshold:]
  this_times_1 = parent_A.get_time_list()[:threshold] + parent_B.get_time_list()[threshold:]
  this_rooms_1 = parent_A.get_room_list()[:threshold] + parent_B.get_room_list()[threshold:]

  this_teachers_2 = parent_B.get_teacher_list()[:threshold] + parent_A.get_teacher_list()[threshold:]
  this_times_2 = parent_B.get_time_list()[:threshold] + parent_A.get_time_list()[threshold:]
  this_rooms_2 = parent_B.get_room_list()[:threshold] + parent_A.get_room_list()[threshold:]

  child_1 = Chromosome(this_teachers_1, this_times_1, this_rooms_1)
  child_2 = Chromosome(this_teachers_2, this_times_2, this_rooms_2)
  return child_1, child_2

# Mutates the genes of the given chromosome
def mutate(chromosome, mutation_rate):
  this_teachers = chromosome.get_teacher_list()
  this_times = chromosome.get_time_list()
  this_rooms = chromosome.get_room_list()
  # mutate each gene independently
  for i in range(len(this_teachers)):
    if random.random() < mutation_rate:
      this_teachers[i] = teachers[random.randint(0, NUM_TEACHERS - 1)]
    if random.random() < mutation_rate:
      this_times[i] = times[random.randint(0, NUM_TIMES - 1)]
    if random.random() < mutation_rate:
      this_rooms[i] = rooms_names[random.randint(0, NUM_ROOMS - 1)]
  chromosome.set_teacher_list(this_teachers)
  chromosome.set_time_list(this_times)
  chromosome.set_room_list(this_rooms)