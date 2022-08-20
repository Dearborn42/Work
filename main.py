
import random
# import names
import json


fileName = 'students.json'

# Important data that will be used in the code "I think this should be able to be changed by input" -Jacob
_schoolData = {
    'numStudents': 20, # How many students
}

# turns numStudents into that many classes

# Finds highest number first run through, second run through it finds second highest, thrid run through is finds the third highest


# Adds students to the json by ammount choosen in chooseData function
# i is the number the student is
for i in range(_schoolData.get('numStudents')):
    # Chooses if student is going to be a male or female by random boolean value
    genderBool = random.getrandbits(1)
    if genderBool == True:
        # _studentFirstName = names.get_first_name(gender='male')
        _studentGender = "male"
    else:
        # _studentFirstName = names.get_first_name(gender='female')
        _studentGender = "female"
    # _studentLastName = names.get_last_name()
    _studentId = "10" + str(i)
    for x in range(0, _schoolData.get('numStudents')):
        num = random.randint(0, 10)
    _studentPoints = num
    # Turns student data into a dictionary
    __student_data = {
                # 'firstName': _studentFirstName,
                # 'lastName': _studentLastName,
                'gender': _studentGender,
                'studentId': _studentId,
                'studentPoints': _studentPoints
            }   
    # Opens the json file
    with open(fileName,'r+') as file:
        # Adds the student to Json file
        fileData = json.load(file)
        fileData["students"].append(__student_data)
        file.seek(0)
        json.dump(fileData, file, indent = 4)

# Counts and orders who has the most points and returns: 
# [[studentId, studentPoints],[studentId, studentPoints],[studentId, studentPoints],[studentId, studentPoints]]
# The first place starts on the left and moves to the right
def pointsLeaderboard():
    """Function that returns the top of the leaderboard."""
    _Leaderboard = []
    with open('students.json', 'r') as file:
            fileData = json.load(file)
    Leaderboard = fileData["students"]
    # Sorts studentPoints from greatest to least then sorts the leaderboard by [studentId, studentPoints]
    Leaderboard.sort(key=lambda x: x["studentPoints"],reverse=True)
    for i in range(_schoolData.get("numStudents")):
        _Leaderboard.append([Leaderboard[i]['studentId'],Leaderboard[i]['studentPoints']])
    return _Leaderboard
leaderboard = pointsLeaderboard()

print (leaderboard)


#ignore this for now, I am asking for help from Mr. Bernard
#numStudents = int(input("Enter number of students."))
# >>>>>>> 4cc68add7a4d110fc2a7a837d0888c6e39ec184c
