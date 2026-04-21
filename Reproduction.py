from data import *
import Chromosome
import random

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

# mutation rate is a float 0<=x<=1.0
def mutate(chromosome, mutation_rate):
  this_teachers = chromosome.get_teacher_list()
  this_times = chromosome.get_time_list()
  this_rooms = chromosome.get_room_list()
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