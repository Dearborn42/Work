import json
import math
import random


def assignmentCreation(assignmentName, subject, grade):
    """Function that creates a new assignment"""
    with open('people.json', 'r+') as file:
        fileData = json.load(file)
        # amount of assignments for each grade level
        fileData["assignmentNumber"][grade] += 1
        # amount of assignments for total number of assignments
        fileData["assignmentNumber"]["total"] += 1
        students = fileData["students"][grade]
        totalScore = 100

        for i in range(fileData["studentsNumber"][grade]):
            score = random.randint(
                int(students[i]["subjectSkills"][subject]), 101)
            for val in students[i]["personalityTraits"].values():
                score * val
            totalScore = (totalScore + score) / 2
            students[i]["grades"][subject] = score

            students[i]["grades"]["overall"] = students[i]["grades"]/5

        file.seek(0)
        file.truncate()
        json.dump(fileData, file, indent=4)


assignmentCreation("coolAssignment", "math", "junior")
