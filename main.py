from asyncio.windows_events import NULL
import random,names,json,time,math

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
        gradeLevel = random.choice([9,10,11,12])

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
                    'personality': [random.randint(50, 100),random.randint(40, 100),random.randint(55, 100),random.randint(40, 100)],
                    # [Math,English,Science,History]
                    'subjectSkills': [random.randint(25, 100),random.randint(30, 100), random.randint(45, 100), random.randint(20, 100)]
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
    Leaderboard.sort(key=lambda x: x["totalScore"],reverse=True)
    for i in range(fileData["studentsNumber"]):
        _Leaderboard.append([Leaderboard[i]['studentId'],Leaderboard[i]['totalScore'],Leaderboard[i]['firstName'] + " " + Leaderboard[i]['lastName']])
    return _Leaderboard

def assignmentCreation(subject):
    """Function that creates a new assignment"""
    with open(fileName, 'r+') as file:
        fileData = json.load(file)
        students = fileData["students"]
        fileData["assignmentNumber"] += 1
        allScores = []
        for i in range(fileData["studentsNumber"]):
            # Calculates persons grade based on personality and subject skills.
            score = random.randint(students[i]["subjectSkills"][subject],101)
            personality = students[i]["personality"]
            score = score + personality[0] + personality[1] + personality[2] + personality[3]
            score = score / 5
            allScores.append(score)
            students[i]["studentGrade"] = (students[i]["studentGrade"] + score) / 2
        file.seek(0)
        file.truncate()
        totalScore = int(math.ceil(sum(allScores) / len(allScores)))
        json.dump(fileData, file, indent=4)
        return totalScore

def studentEvents(event):
    """Function that creates or lets students participate in events."""

    ###### Still working on this so ignore how some parts may not work

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
    _time = [0, 0, 0]
    while True:
        time.sleep(1)
        _time[2] += 1
        print(_time)
        if _time[2]%30 == 0:
            assignmentCreation(0)
            assignmentCreation(1)
            assignmentCreation(2)
            assignmentCreation(3)
        # if time[1] == 2:
        #     print()
        # #    studentEvents[random.choice["football", "soccer", "baseball", "volleyball,",
        # #                                "softball", "SpellingBee", "Fbla", "ChessTournament", "ChessTournament", "CouncilElections"]]
        # if time[1] == 5:
        #      with open(fileName, 'r+') as file:
        #             fileData = json.load(file)
        #             students = fileData["students"]
        #             for i in range(fileData["studentsNumber"]):
        #                 student = students[i]
        #                 student[i]["studentGrade"] = 100
        #      time[1] = 0
        else:
            if _time[2] >= 59:
                _time[2] = 0
                _time[1] += 1
            elif _time[1] >= 5:
                _time[1] = 0
