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

        #goes through list of all teachers
        #checks facilitator load
        for x in teachers_data:
            if(teachers.count(x) > 4):                                                          #teacher over-scheduled
                score -= 0.5
            elif(teachers.count(x) < 3 and x != 'Tyler'):                                       #teacher under-scheduled
                score -= 0.4
            if(x == 'Tyler' and teachers.count(x) > 1):                                         #Dr.Tyler over-scheduled
                score -= 0.4

        #checks consecutive time rules for SLA101
        if(abs(times[0] - times[1]) > 4):                                                       #SLA101 A and B are >4 hours apart
            score += 0.5
        elif(times[0] == times[1]):                                                             #SLA101 A and B are at the same time
            score -= 0.5

        #checks consecutive time rules for SLA191
        if(abs(times[2] - times[3]) > 4):                                                       #SLA191 A and B are >4 hours apart
            score += 0.5
        elif(times[2] == times[3]):                                                             #SLA191 A and B are at the same time
            score -= 0.5

        #SLA191 and SLA101 have consecutive times
        if(abs(times[0] - times[2]) == 1):                                                      #SLA101A and SLA191A right after the other
            if(rooms[0] not in ["Beach 201", "Beach 301", "Roman 201", "Roman 216"] ==          #SLA101A and SLA191A both in or not in beach or roman
            rooms[2] not in ["Beach 201", "Beach 301", "Roman 201", "Roman 216"]):
                score += 0.5
            else:
                score -= 0.4
        if(abs(times[0] - times[3]) == 1):                                                      #SLA101A and SLA191B right after the other
            if(rooms[0] not in ["Beach 201", "Beach 301", "Roman 201", "Roman 216"] ==          #SLA101A and SLA191B both in or not in beach or roman
            rooms[3] not in ["Beach 201", "Beach 301", "Roman 201", "Roman 216"]):
                score += 0.5
            else:
                score -= 0.4
        if(abs(times[1] - times[2]) == 1):                                                      #SLA101B and SLA191A right after the other
            if(rooms[1] not in ["Beach 201", "Beach 301", "Roman 201", "Roman 216"] ==          #SLA101B and SLA191A both in or not in beach or roman
            rooms[2] not in ["Beach 201", "Beach 301", "Roman 201", "Roman 216"]):
                score += 0.5
            else:
                score -= 0.4
        if(abs(times[1] - times[3]) == 1):                                                      #SLA101B and SLA191B right after the other
            if(rooms[1] not in ["Beach 201", "Beach 301", "Roman 201", "Roman 216"] ==          #SLA101B and SLA191B both in or not in beach or roman
            rooms[3] not in ["Beach 201", "Beach 301", "Roman 201", "Roman 216"]):
                score += 0.5
            else:
                score -= 0.4

        #SLA101 and SLA191 sections are separated by an hour or same time
        if(abs(times[0] - times[2]) == 2):                                                      #SLA101A and SLA191A are separated by an hour
            score += 0.25
        elif(times[0] == times[2]):                                                             #SLA101A and SLA191A are at the same time
            score -= 0.25
        if(abs(times[0] - times[3]) == 2):                                                      #SLA101A and SLA191B are separated by an hour
            score += 0.25
        elif(times[0] == times[3]):                                                             #SLA101A and SLA191B are at the same time
            score -= 0.25
        if(abs(times[1] - times[2]) == 2):                                                      #SLA101B and SLA191A are separated by an hour
            score += 0.25
        elif(times[1] == times[2]):                                                             #SLA101B and SLA191A are at the same time
            score -= 0.25
        if(abs(times[1] - times[3]) == 2):                                                      #SLA101B and SLA191B are separated by an hour
            score += 0.25
        elif(times[1] == times[3]):                                                             #SLA101B and SLA191B are at the same time
            score -= 0.25

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
            if(rooms_data[room] < class_size):                                                  #rooms smaller than class
                score -= 0.5
            elif(rooms_data[room] > class_size * 3):                                            #room much too big for class
                score -= 0.4
            elif(rooms_data[room] > class_size * 1.5):                                          #room too big for class
                score -= 0.2
            else:                                                                               #room proper size
                score += 0.3

            #preferred facilitators
            if(teacher in classes_data[sections_data[section]][1]):                             #preferred facilitator
                score += 0.5
            elif(teacher in classes_data[sections_data[section]][2]):                           #listed facilitator
                score += 0.2
            else:                                                                               #unlisted facilitator
                score -= 0.1

            for i in range(0, len(teachers)):
                if(time == times[i]):                                                           #class is at the same time as other
                    if(room == rooms[i]):                                                       #class is at same place as another
                        score -= 0.5
                    if(teacher == teachers[i]):                                                 #class has same teacher as other
                        score -= 0.2
                elif((abs(time - times[i]) == 1)):                                              #class is right after other
                    if(teacher == teachers[i]):                                                 #classes have same teacher
                        if(room not in ["Beach 201", "Beach 301", "Roman 201", "Roman 216"] ==  #both in or not in roman or beach
                           rooms[i] not in ["Beach 201", "Beach 301", "Roman 201", "Roman 216"]):
                            score += 0.5
                        else:                                                                   #consective classes one in roman or beach
                            score -= 0.4



        schedule.set_fitness(score)
            
                
                
