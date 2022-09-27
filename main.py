from asyncio.windows_events import NULL
from operator import le
import random
import names
import json
import time
import math

fileName = 'students.json'


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
        gradeLevel = random.choice([9, 10, 11, 12])

        # Turns student data into a dictionary
        __student_data = {
            'firstName': _studentFirstName,
            'lastName': _studentLastName,
            'gradeLevel': gradeLevel,
            'gender': _studentGender,
            'studentId': _studentId,
            'studentGrade': 100,
            'totalPoints': 0,
            # [Intelligence,OnTask,WorkOnTime,Happiness] --Will be used later to calculate assignment scores
            'personality': [random.randint(50, 100), random.randint(40, 100), random.randint(55, 100), random.randint(40, 100)],
            # [Math,English,Science,History, Reset]
            'subjectSkills': [random.randint(25, 100), random.randint(30, 100), random.randint(45, 100), random.randint(20, 100), "reset"]
        }

        # Opens the json file
        with open(fileName, 'r+') as file:
            # Adds the student to Json file
            fileData = json.load(file)
            fileData["students"].append(__student_data)
            fileData["studentsNumber"] += 1
            file.seek(0)
            json.dump(fileData, file, indent=4)


leaderboard = [[NULL, NULL, NULL], [NULL, NULL, NULL], [NULL,
                                                        NULL, NULL], [NULL, NULL, NULL], [NULL, NULL, NULL]]


def pointsLeaderboard():
    """Function that returns the top of the leaderboard"""
    with open(fileName, 'r') as file:
        fileData = json.load(file)
        students = fileData["students"]
    topStudent = 0
    topSenior = 0
    topJunior = 0
    topSophmore = 0
    topFreshman = 0

    for i in range(fileData["studentsNumber"]):
        student = students[i]
        if student["gradeLevel"] == 9:
            if student["studentGrade"] > topFreshman:
                topFreshman = student["studentGrade"]
                leaderboard[1][0] = student['firstName']
                leaderboard[1][1] = student['lastName']
                leaderboard[1][2] = topFreshman

        if student["gradeLevel"] == 10:
            if student["studentGrade"] > topSophmore:
                topSophmore = student["studentGrade"]
                leaderboard[2][0] = student['firstName']
                leaderboard[2][1] = student['lastName']
                leaderboard[2][2] = topSophmore

        if student["gradeLevel"] == 11:
            if student["studentGrade"] > topJunior:
                topJunior = student["studentGrade"]
                leaderboard[3][0] = student['firstName']
                leaderboard[3][1] = student['lastName']
                leaderboard[3][2] = topJunior

        if student["gradeLevel"] == 12:
            if student["studentGrade"] > topSenior:
                topSenior = student["studentGrade"]
                leaderboard[4][0] = student['firstName']
                leaderboard[4][1] = student['lastName']
                leaderboard[4][2] = topSenior

        if students[i]["studentGrade"] > topStudent:
            topStudent = student["studentGrade"]
            leaderboard[0][0] = student['firstName']
            leaderboard[0][1] = student['lastName']
            leaderboard[0][2] = topStudent
    print(leaderboard)


# def createEvent():
#     events = ['footballGame', 'basketballGame', 'soccerGame', 'tennisGame',
#               'volleyballGame', 'prom', 'fundraiser', 'bakingComp', 'clubsNight', 'fbla']
#     with open(fileName, 'r+') as file:
#         fileData = json.load(file)
#         students = fileData["students"]
#     for i in range(fileData["studentsNumber"]):
#         chance = random.randint(0, 1)
#         print(chance)
#         if chance == 1:
#             students[i]["totalPoints"] += 1


def assignmentCreation(subject):
    """Function that creates a new assignment"""
    with open(fileName, 'r+') as file:
        fileData = json.load(file)
        students = fileData["students"]
        fileData["assignmentNumber"] += 1
        allScores = []
        for i in range(fileData["studentsNumber"]):
            # Calculates persons grade based on personality and subject skills.
            if subject == 4:
                students[i]["studentGrade"] = 100
                score = 100
                allScores.append(score)
            else:

                score = random.randint(
                    students[i]["subjectSkills"][subject], 101)
                personality = students[i]["personality"]
                score = score + \
                    personality[0] + personality[1] + \
                    personality[2] + personality[3]
                score = score / 5
                allScores.append(score)
                students[i]["studentGrade"] = (
                    students[i]["studentGrade"] + score) / 2
        totalScore = int(math.ceil(sum(allScores) / len(allScores)))
        file.seek(0)
        file.truncate()
        json.dump(fileData, file, indent=4)
        return totalScore


def simulation():
    """A multi threaded function that keeps track of time and starts events when the time is reached"""

    # Still being worked on

    _time = [0, 0, 0]
    _year = 0
    check = True
    while check:
        time.sleep(1)
        _time[2] += 1
        print(_time)
        if _time[2] % 30 == 0:
            assignmentCreation(0)
            assignmentCreation(1)
            assignmentCreation(2)
            assignmentCreation(3)
        if _time[1] >= 5:
            pointsLeaderboard()
            assignmentCreation(4)
            _time[1] = 0
            _year = _year + 1
            if _year == 4:
                check = False
                print("Year has ended")
        else:
            if _time[2] >= 60:
                _time[2] = 0
                _time[1] += 1


# if __name__ == "__main__":
#     simulation()
