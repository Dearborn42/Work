# Finished

import json
import random
import names

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


def createWorkers():
    """Function that creates school staff/administ."""
    with open("template.txt", "r") as file:
        template = file.read()
        with open("people.json", "w") as file:
            file.write(template)

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
    staff = staff()
    allStaff = ["principal", "vicePrincipal", "counselor", "officeWorker", "security", "maintenance", "math", "science", "english", "history"]
    for i in allStaff:
        for j in range(schoolStaff[i]):
            staff.createStaff(job=i)

createWorkers()