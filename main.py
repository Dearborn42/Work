#from asyncio.windows_events import NULL
from asyncio.windows_events import NULL
import random
import names
import json


fileName = 'students.json'

# Important data that will be used in the code "I think this should be able to be changed by input" -Jacob

# turns numStudents into that many classes

# Finds highest number first run through, second run through it finds second highest, thrid run through is finds the third highest


def createStudents(numStudents):
    global studentsNum
    """Function that creates students from numStudents"""
    for i in range(numStudents):
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

        # Random grade level: 0 is freshmen - 3 is senior
        gradeLevel = random.choice([9,10,11,12])
        # Turns student data into a dictionary
        __student_data = {
                    'firstName': _studentFirstName,
                    'lastName': _studentLastName,
                    'gradeLevel': gradeLevel,
                    'gender': _studentGender,
                    'studentId': _studentId,
                    'studentGrade': random.randint(50, 100),
                    'studentPoints': random.randint(0, 4),
                    'totalScore': 0,
                }   
        if __student_data.get('studentGrade') >= 90:
            __student_data['totalScore'] += 4 + __student_data['studentPoints']
        elif __student_data.get('studentGrade') >= 80:
            __student_data['totalScore'] += 3 + __student_data['studentPoints']
        elif __student_data.get('studentGrade') >= 70:
            __student_data['totalScore'] += 2 + __student_data['studentPoints']
        elif __student_data.get('studentGrade') >= 60:
            __student_data['totalScore'] += 1 + __student_data['studentPoints']
        else:
            __student_data['totalScore'] + __student_data['studentPoints']
    
        # Opens the json file
        with open(fileName,'r+') as file:
            # Adds the student to Json file
            fileData = json.load(file)
            fileData["students"].append(__student_data)
            fileData["studentsNumber"] += 1
            file.seek(0)
            json.dump(fileData, file, indent = 4)

def pointsLeaderboard():
    """Function that returns the top of the leaderboard"""
    _Leaderboard = []
    with open('students.json', 'r') as file:
            fileData = json.load(file)
    Leaderboard = fileData["students"]
    # Sorts studentPoints from greatest to least then sorts the leaderboard by [studentId, studentPoints, studentName]
    Leaderboard.sort(key=lambda x: x["totalScore"],reverse=True)
    for i in range(fileData["totalScore"]):
        _Leaderboard.append([Leaderboard[i]['studentId'],Leaderboard[i]['totalScore'],Leaderboard[i]['firstName'] + " " + Leaderboard[i]['lastName']])
    return _Leaderboard