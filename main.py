import json
import random
import names
import eel
eel.init('web')

file = open('people.json')
data = json.load(file)
yearNum = data['yearNumber']
posTraits = data['posTraits']
negTraits = data['negTraits']

schoolStaff = {
    "principal": 1,
    "vicePrincipal": 1,
    "counselor": 4,
    "officeWorker": 6,
    "security": 4,
    "maintenance": 10,
    "math": 5,
    "science": 5,
    "english": 5,
    "history": 5
}

def resetJson():
    """Function that wipes json data"""
    # take all text from template.txt and put it into people.txt
    with open("template.txt", "r") as file:
        template = file.read()
        with open("people.json", "w") as file:
            file.write(template)

@eel.expose
def createWorkers():
    """
    Function that creates school staff/administ and removes old ones.
    - Input: N/A
    - Output: Adds/removes staff to json 
    """
    class staff:
        def __init__(self):
            self.firstName = ""
            self.lastName = ""
            self.gender = ""
            self.birthday = []
            self.personalityTraits = {}
            self.skill = 0

        def createStaff(self, job):
            """Function that creates a new staff member."""
            birthDay = random.randint(1, 30)
            birthMonth = random.randint(1, 12)
            birthYear = random.randint(1969+yearNum, 1999+yearNum)

            self.gender = random.choice(["female", "male"])
            self.firstName = names.get_first_name(gender=self.gender)
            self.lastName = names.get_last_name()
            self.birthday = [birthYear, birthMonth, birthDay]
            self.personalityTraits = {}
            self.personalityTraits.update({random.choice(list(posTraits.items())), random.choice(list(negTraits.items()))})
            self.skill = random.randint(0, 100)

            with open("people.json", "r+") as file:
                fileData = json.load(file)
                # check if job is in list
                if job in ["math", "science", "english", "history"]:
                    fileData["staff"]["teacher"][job].append(self.__dict__)
                else:
                    fileData["staff"][job].append(self.__dict__)
                file.seek(0)
                json.dump(fileData, file, indent=4)

    # Genorate staff
    resetJson()
    staff = staff()
    allStaff = ["principal", "vicePrincipal", "counselor", "officeWorker", "security", "maintenance", "math", "science", "english", "history"]
    for i in allStaff:
        for j in range(schoolStaff[i]):
            staff.createStaff(job=i)

@eel.expose
def createStudents(numStudents):
    """
    Function that recieves a number of students to create students.
    - Input: Number of students
    - Output: Adds students to json
    """
    class Student:
        def __init__(self):
            self.firstName = ""
            self.lastName = ""
            self.gender = ""
            self.studentId = 0
            self.points = 0
            self.birthday = []
            self.assignments = []
            self.grades = {}
            self.personalityTraits = {}
            self.subjectSkills = {}

        def createStudent(self):
            """Function that gives a student attributes."""
            birthDay = str(random.randint(1, 30))
            birthMonth = str(random.randint(1, 12))
            birthYear = str(random.randint(2004 + yearNum, 2007 + yearNum))

            if int(birthYear) == 2007 + yearNum:
                grade = 'freshman'
            elif int(birthYear) == 2006 + yearNum:
                grade = 'sophmore'
            elif int(birthYear) == 2005 + yearNum:
                grade = 'junior'
            else:
                grade = 'senior'

            self.gender = random.choice(['female', 'male'])
            self.firstName = names.get_first_name(gender=self.gender)
            self.lastName = names.get_last_name()
            self.birthday = [birthYear, birthMonth, birthDay]
            self.studentId = "10" + str(birthDay + birthYear + birthMonth)
            self.grades = {
                'math': 100,
                'english': 100,
                'science': 100,
                'history': 100,
                'electives': 100,
                'overall': 100
            }
            self.personalityTraits.update(
                {random.choice(list(posTraits.items())), random.choice(list(negTraits.items()))})
            self.subjectSkills = {
                'math': random.randint(25, 100),
                'english': random.randint(30, 100),
                'science': random.randint(45, 100),
                'history': random.randint(20, 100),
                'electives': random.randint(50, 100)
            }

            with open('people.json', 'r+') as file:
                # Adds the student to Json file
                fileData = json.load(file)
                fileData["students"][grade].append(self.__dict__)
                fileData["studentsNumber"][grade] += 1
                file.seek(0)
                json.dump(fileData, file, indent=4)

    for i in range(numStudents):
        student = Student()
        student.createStudent()

@eel.expose
def createEvent(eventName, grade):
    """
    Function that creates a new event.
    - Input: The name of the event and grade
    - Output: Adds points to students who attend the event
    """
    with open('people.json', 'r+') as file:
        fileData = json.load(file)
        students = fileData["students"][grade]

        for i in range(fileData["studentsNumber"][grade]):
            mGrade = students[i]["grades"]["math"]
            engGrade = students[i]["grades"]["english"]
            sGrade = students[i]["grades"]["science"]
            hGrade = students[i]["grades"]["history"]
            eleGrade = students[i]["grades"]["electives"]
            grades = [mGrade, engGrade, sGrade, hGrade, eleGrade]
            check = 0
            for j in range(len(grades)):
                if grades[j] >= 60:
                    check += 1
                    if check == 5:
                        students[i]["points"] += 1
        file.seek(0)
        file.truncate()
        json.dump(fileData, file, indent=4)

@eel.expose
def assignmentCreation(assignmentName, subject, grade):
    """
    Function that creates a new assignment.
    - Input: The name of the assignment, the subject and the grade
    - Output: Changes students grades
    """
    def overallGrade(score):
        """Function that re-evaluates the overall score of the assignment"""
        grades = students[i]["grades"]
        # Adds all the grades together
        allGrades = sum(list(grades.values())) - grades["overall"]
        # Appends changes to the overall grade and subject grade
        grades[subject] = (grades[subject] + score) / 2
        grades["overall"] = allGrades / 5

    with open('people.json', 'r+') as file:
        fileData = json.load(file)
        # amount of assignments for each grade level
        fileData["assignmentNumber"][grade] += 1
        # amount of assignments for total number of assignments
        fileData["assignmentNumber"]["total"] += 1
        students = fileData["students"][grade]
        totalScore = 100

        for i in range(fileData["studentsNumber"][grade]):
            score = random.randint(int(students[i]["subjectSkills"][subject]), 101) 
            for j in students[i]["personalityTraits"].values():
                score * i
            totalScore = (totalScore + score) / 2
            overallGrade(score)
        file.seek(0)
        file.truncate()
        json.dump(fileData, file, indent=4)

eel.start('index.html')