import random
import data

def generate_schedule():
    schedule = {}
    for x in data.classes:
        teacher = random.choice(data.teachers)
        time = random.choice(data.times)
        room = random.choice(list(data.rooms))
        print (x, teacher, room)
        schedule[x] = (teacher, time, room)
    return schedule