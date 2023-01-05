import json
import random
import names
import eel

eel.init("web")

# Open and load people.json file
file = open("people.json")
data = json.load(file)

# Assign variables for yearNumber, posTraits, and negTraits from data
year_num = data["yearNumber"]
pos_traits = data["posTraits"]
neg_traits = data["negTraits"]

# Define dictionary of school staff positions and the number of staff for each position
school_staff = {
    "principal": 1,
    "vicePrincipal": 1,
    "counselor": 4,
    "officeWorker": 6,
    "security": 4,
    "maintenance": 10,
    "math": 5,
    "science": 5,
    "english": 5,
    "history": 5,
}

def reset_json():
    """Function that wipes json data by replacing it with the contents of template.txt"""
    with open("template.txt", "r") as file:
        template = file.read()
        with open("people.json", "w") as file:
            file.write(template)

class Person:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.gender = ""
        self.birthday = []
        self.personality_traits = {}
        self.skill = 0
    
    def generate_name_and_personality(self):
        self.gender = random.choice(["female", "male"])
        self.first_name = names.get_first_name(gender=self.gender)
        self.last_name = names.get_last_name()
        self.birthday = [
            random.randint(1969, 1999),
            random.randint(1, 12),
            random.randint(1, 30),
        ]
        self.personality_traits = {
            random.choice(list(pos_traits.items())),
            random.choice(list(neg_traits.items())),
        }

class Staff(Person):
    def __init__(self, job):
        super().__init__()
        self.job = job
        self.generate_name_and_personality()

    def create(self):
        # Open and update people.json
        with open("people.json", "r+") as file:
            file_data = json.load(file)
            # Check if job is in list of teacher positions
            if self.job in ["math", "science", "english", "history"]:
                file_data["staff"]["teacher"][self.job].append(self.__dict__)
            else:
                file_data["staff"][self.job].append(self.__dict__)
            file.seek(0)
            json.dump(file_data, file, indent=4)

class Student(Person):
    def __init__(self):
        super().__init__()
        self.student_id = 0
        self.points = 0
        self.assignments = []
        self.grades = {}
        self.subject_skills = {}
        self.generate_name_and_personality()

    def create(self):
        birth_year = int(self.birthday[0])
        if birth_year == 2007:
            grade = "freshman"
        elif birth_year == 2006:
            grade = "sophmore"
        elif birth_year == 2005:
            grade = "junior"
        else:
            grade = "senior"

        self.student_id = "10" + str(self.birthday[2] + self.birthday[0] + self.birthday[1])
        self.grades = {
            "math": 100,
            "english": 100,
            "science": 100,
            "history": 100,
            "electives": 100,
            "overall": 100,
        }
        self.subject_skills = {
            "math": random.randint(25, 100),
            "english": random.randint(30, 100),
            "science": random.randint(45, 100),
            "history": random.randint(20, 100),
            "electives": random.randint(10, 100),
        }
        # Open and update people.json
        with open("people.json", "r+") as file:
            file_data = json.load(file)
            file_data["students"][grade].append(self.__dict__)
            file.seek(0)
            json.dump(file_data, file, indent=4)

@eel.expose
def create_workers():
    """
    Function that creates school staff/administrators and removes old ones.
    - Input: None
    - Output: Adds/removes staff to people.json 
    """
    reset_json()
    all_staff = ["principal", "vicePrincipal", "counselor", "officeWorker", "security", "maintenance", "math", "science", "english", "history"]
    for i in all_staff:
        for j in range(school_staff[i]):
            Staff(job=i).create()

@eel.expose
def create_students(num_students):
    """
    Function that recieves a number of students to create students.
    - Input: Number of students
    - Output: Adds students to json
    """
    for i in range(num_students):
        Student().create()

create_students(5)