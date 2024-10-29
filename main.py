#Braden Leach
#OCT 29 2024
#Lists Evidence


#empty lists
names = []
schools = []
courses = []
score1 = []
score2 = []

#add
names.append('Thomson, Jack')
names.append('Evans, Sal')
schools.append('West High')
schools.append('East High')
courses.append('History')
courses.append('Biology')

#score 1
score1.append(88)
score1.append(90)
score1.append(97)
score1.append(30)
#score 2
score2.append(98)
score2.append(8)
score2.append(58)
score2.append(100)
#Math for score
    #1 
num_elements1 = len(score1)
average_score1 = sum(score1) / num_elements1
    #2 
num_elements2 = len(score2)
average_score2 = sum(score2) / num_elements2

#Display
    #1
print(f'''
Semester 1 Grade Report
-------------
Student: {names[0]}
School: {schools[0]}
Course: {courses[0]}
Average Score: {average_score1:.2f}
      ''')
    #2
print(f'''
Student: {names[1]}
School: {schools[1]}
Course: {courses[1]}
Average Score: {average_score2:.2f}
      ''')