import random
import json
import math


def createEvent(eventName):
    with open('people.json', 'r+') as file:
        fileData = json.load(file)
        students = fileData["students"]

        for i in range(fileData["studentsNumber"]):
            mGrade = students[i]["grades"]["math"]
            engGrade = students[i]["grades"]["english"]
            sGrade = students[i]["grades"]["science"]
            hGrade = students[i]["grades"]["history"]
            eleGrade = students[i]["grades"]["electives"]
            grades = [mGrade, engGrade, sGrade, hGrade, eleGrade]
            for j in grades:
                if grades[j] >= 60:
                    students[i]["points"] += 1

        file.seek(0)
        file.truncate()
        json.dump(fileData, file, indent=4)
