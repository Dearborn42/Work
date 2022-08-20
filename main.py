
import random

numStudents = 5
#creates an empty list

import json
import random
import names
fileName = 'students.json'

studentList = []
#adds a number to the list and adds as much as the user inputs
#can replace items later, they are just placeholders for now

# Important data that will be used in the code "I think this should be able to be changed by input" -Jacob
_schoolData = {
    'numStudents': 10, # How many students
}


class student:
      
   def __init__(self, name, grade, points):
    self.name = name
    self.grade = grade
    self.points = points
# # creates class

# for x in range(0, numStudents):
#     num = random.randint(0, 10)
#     studentList.append(student('John', 'A', num))
#     print(studentList[x].points)

# turns numStudents into that many classes

s1 = student('Harry', 'A', 12)
s2 = student('Johnny', 'C', 6)
s3 = student('Bob', 'B', 3)
s4 = student('Ryan', 'D', 49)

# Test objects

Points = [s1.points, s2.points, s3.points, s4.points]
Best = 0
SecondBest = 0
ThirdBest = 0
FourthBest = 0

# test list and varibles

for x in Points:
    if x > Best:
        Best = x
for y in Points:
    if y > SecondBest and y != Best:
       SecondBest = y
for z in Points:
    if z > ThirdBest and z != Best and z != SecondBest:
        ThirdBest = z

# Finds highest number first run through, second run through it finds second highest, thrid run through is finds the third highest

print(Best, SecondBest, ThirdBest)

# Adds students to the json by ammount choosen in chooseData function
# i is the number the student is
for i in range(_schoolData.get('numStudents')):
    # Chooses if student is going to be a male or female by random boolean value
    genderBool = random.getrandbits(1)
    if genderBool == True:
        _studentFirstName = names.get_first_name(gender='male')
        _studentGender = "male"
    else:
        _studentFirstName = names.get_first_name(gender='female')
        _studentGender = "female"
    _studentLastName = names.get_last_name()
    _studentId = "10" + str(i)
    _studentPoints = 0
    # Turns student data into a dictionary
    __student_data = {
                'firstName': _studentFirstName,
                'lastName': _studentLastName,
                'gender': _studentGender,
                'studentId': _studentId,
                'studentPoints': _studentPoints
            }   
    # Opens the json file
    with open(fileName,'r+') as file:
        # Adds the student to Json file
        fileData = json.load(file)
        fileData["students"].append(__student_data)
        file.seek(0)
        json.dump(fileData, file, indent = 4)

# Counts and orders who has the most points and returns: 
# [[studentId, studentPoints],[studentId, studentPoints],[studentId, studentPoints],[studentId, studentPoints]]
# The first place starts on the left and moves to the right
def pointsLeaderboard():
    """Function that returns the top of the leaderboard."""
    _Leaderboard = []
    with open('students.json', 'r') as file:
            fileData = json.load(file)
    Leaderboard = fileData["students"]
    # Sorts studentPoints from greatest to least then sorts the leaderboard by [studentId, studentPoints]
    Leaderboard.sort(key=lambda x: x["studentPoints"],reverse=True)
    for i in range(_schoolData.get("numStudents")):
        _Leaderboard.append([Leaderboard[i]['studentId'],Leaderboard[i]['studentPoints']])
    return _Leaderboard
leaderboard = pointsLeaderboard()


#ignore this for now, I am asking for help from Mr. Bernard
#numStudents = int(input("Enter number of students."))
# >>>>>>> 4cc68add7a4d110fc2a7a837d0888c6e39ec184c
