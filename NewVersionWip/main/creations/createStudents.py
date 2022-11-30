import json
import random

import names

file = open('people.json')
data = json.load(file)
yearNum = data['yearNumber']
posTraits = data['posTraits']
negTraits = data['negTraits']


def createStudents(numStudents):
    """Function that recieves a number of students to create students."""
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

        def createStudent(self, stuNum):
            """Function that gives a student attributes."""
            birthDay = random.randint(1, 30)
            birthMonth = random.randint(1, 12)
            birthYear = random.randint(2004 + yearNum, 2007 + yearNum)

            if birthYear == 2007 + yearNum:
                grade = 'freshman'
            elif birthYear == 2006 + yearNum:
                grade = 'sophmore'
            elif birthYear == 2005 + yearNum:
                grade = 'junior'
            else:
                grade = 'senior'

            self.gender = random.choice(['female', 'male'])
            self.firstName = names.get_first_name(gender=self.gender)
            self.lastName = names.get_last_name()
            self.birthday = [birthYear, birthMonth, birthDay]
            self.studentId = "10" + str(stuNum)
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
        student.createStudent(stuNum=i)


createStudents(1)
