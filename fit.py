import Chromosome

from data import classes as classes_data
from data import rooms as rooms_data
from data import teachers as teachers_data
from data import sections as sections_data

def fit(schedules):
    #iterates through each schedule to be evaluated
    for schedule in schedules:
        teachers = schedule.get_teacher_list()
        times = schedule.get_time_list()
        rooms = schedule.get_room_list()
        score = 0

        for x in teachers_data:
            if(teachers.count(x) > 4):
                score -= 0.5
            elif(teachers.count(x) < 3):
                score -= 0.4

        #goes one-by-one through classes
        #removes classes as it goes to prevent doubling comparisons
        #tracks remaining classes by watching length of teachers list
        while(len(teachers) > 1):
            section = len(sections_data) - len(teachers)
            teacher = teachers.pop()
            time = times.pop()
            room = rooms.pop()
            
            #room sizes
            class_size = classes_data[sections_data[section]][0]
            if(rooms_data[room] < class_size):                              #rooms smaller than class
                score -= 0.5
            elif(rooms_data[room] > class_size * 3):                      #room much too big for class
                score -= 0.4
            elif(rooms_data[room] > class_size * 1.5):                        #room too big for class
                score -= 0.2
            else:                                                           #room proper size
                score += 0.3

            #preferred facilitators
            if(teacher in classes_data[sections_data[section]][1]):                        #preferred facilitator
                score += 0.5
            elif(teacher in classes_data[sections_data[section]][2]):                      #listed facilitator
                score += 0.2
            else:                                                           #unlisted facilitator
                score -= 0.1

            for i in range(0, len(teachers)):
                if(time == times[i] and room == rooms[i]):                  #class is at same time and place as another
                    score -= 0.5
                if(time == times[i] and teacher == teachers[i]):            #class has same time and teacher as other
                    score -= 0.2

        schedule.set_fitness(score)
            
                
                
