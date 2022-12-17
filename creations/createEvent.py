import json
import math
import random


def createEvent(eventName, grade):
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


createEvent("Basketball", "senior")
