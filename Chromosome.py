from data import *
import random
# To create a randomly generated chromosome, call Chromosome()
# To use existing values for crossover etc, call Chromosome(teacher_list, time_list, room_list)
class Chromosome:
  def __init__(self, teacher_list=[], time_list=[], room_list=[]):
    self.fitness = 0
    self.teacher_list = teacher_list.copy()
    self.time_list = time_list.copy()
    self.room_list = room_list.copy()
    if len(teacher_list) == 0:
      for _ in range(NUM_CLASSES):
        self.teacher_list.append(teachers[random.randint(0, NUM_TEACHERS - 1)])
        self.time_list.append(times[random.randint(0, NUM_TIMES - 1)])
        self.room_list.append(rooms_names[random.randint(0, NUM_ROOMS - 1)])
  def __str__(self):
        return (f"Teachers: {self.teacher_list}\n" +
        f"Times: {self.time_list}\n" +
        f"Rooms: {self.room_list}")
  def set_fitness(self, new_val):
    self.fitness = new_val
  def get_fitness(self):
    return self.fitness
  def set_teacher_list(self, new_val):
    self.teacher_list = new_val.copy()
  def get_teacher_list(self):
    return self.teacher_list.copy()
  def set_time_list(self, new_val):
    self.time_list = new_val.copy()
  def get_time_list(self):
    return self.time_list.copy()
  def set_room_list(self, new_val):
    self.room_list = new_val.copy()
  def get_room_list(self):
    return self.room_list.copy()

# dunno where we are going to put this, but this is all that's needed to make a random pop of size pop_size  
def create_pop(pop_size):
  pop = []
  for _ in range(pop_size):
    pop.append(Chromosome())
  return pop
