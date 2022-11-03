from asyncio.windows_events import NULL
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
        gender = random.choice(["male", "female"])
        _studentFirstName = names.get_first_name(gender=gender)
        _studentGender = gender
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


def pointsLeaderboard():
    """Function that returns the top of the leaderboard"""
    _Leaderboard = []
    with open(fileName, 'r') as file:
        fileData = json.load(file)
    Leaderboard = fileData["students"]
    # Sorts studentPoints from greatest to least then sorts the leaderboard by [studentId, studentPoints, studentName]
    Leaderboard.sort(key=lambda x: x["totalScore"], reverse=True)
    for i in range(fileData["studentsNumber"]):
        _Leaderboard.append([Leaderboard[i]['studentId'], Leaderboard[i]['totalScore'],
                            Leaderboard[i]['firstName'] + " " + Leaderboard[i]['lastName']])
    return _Leaderboard


pointsLeaderboard()


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


def studentEvents(event):
    """Function that creates or lets students participate in events."""

    # Still being worked on

    sports = ["football", "soccer", "baseball", "volleyball,", "softball"]
    nonsports = ["SpellingBee", "Fbla", "ChessTournament", "ChessTournament"]
    possibleWinners = []
    possibleStudentCouncil = []

    with open(fileName, 'r+') as file:
        fileData = json.load(file)
        students = fileData["students"]
        for i in range(len(students)):
            student = fileData["students"][i]
            canAttend = bool(random.getrandbits(1))
            if canAttend == True and student["personality"]["happiness"] >= 60:
                if event in sports:
                    student["totalPoints"] += 1
                elif event in nonsports:
                    if student["Intelligence"] >= 80:
                        possibleWinners.append(student["studentId"])
                        student["totalPoints"] += 1
                elif event == "CouncilElections":
                    if student["Intelligence"] >= 60 and student["studentGrade"] >= 70:
                        possibleStudentCouncil.append(student["studentId"])
                        student["totalPoints"] += 1
                elif event == "CustomEvent":
                    student["totalPoints"] += 1


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
            assignmentCreation(4)
            _year = _year + 1
            _time[1] = 0
            if _year == 4:
                check = False
                print("Year has ended")
        else:
            if _time[2] >= 60:
                _time[2] = 0
                _time[1] += 1


# if __name__ == "__main__":
#     simulation()
