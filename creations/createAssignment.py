# Finished

import json
import math
import random

def assignmentCreation(assignmentName, subject, grade):
    """Function that creates a new assignment"""
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

assignmentCreation("coolAssignment", "math", "junior")
