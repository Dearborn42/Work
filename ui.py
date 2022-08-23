import time
from time import strftime
from tkinter import *
from main import createStudents, assignmentCreation
import asyncio
root = Tk()
root.title("School control panel")

# Functions


def _createStudents():
    createStudents(int(studentsNum.get()))
    Log("Generated " + studentsNum.get() + " students. ")


def _createEvents():
    print()


def _createAssignment():
    totalScore = assignmentCreation(int(Choice1.get()))
    Log("Created " + assignment.get() + " Assignment")
    Log("Total Score: " + str(totalScore) + "%")


# Choose how many students
Label(root, text = "Add students:").grid(row=3, column=0)
studentsNum = Entry(root)
studentsNum.grid(row=4, column=0)

# Submit button 1
Label(root, text = "").grid(row=4, column=1)
studentsNum_submit = Button(root, text = "Submit", command=_createStudents).grid(row=4, column=2)

# Lable
logs = Label(root, text ='Logs', font = "30")  
logs.grid(row=11, column=0)

# Scroll bar and menu
logsScroll = Scrollbar(root)
logsScroll.grid(row=12, column=1, sticky='ns')
LogsList = Listbox(root, yscrollcommand = logsScroll.set )

def Log(message):
    LogsList.insert(END, str(message))

LogsList.grid(row=12, column=0)  
 
logsScroll.config(command = LogsList.yview) 
Choice1 = IntVar()

# Math assignment button
Label(root, text = "Create an assignment:").grid(row=5, column=0)
assignmentRadio1 = Radiobutton(root, text = "Math", variable = Choice1, value = 1)
assignmentRadio1.grid(row=6, column=0)

# English assignment button
Label(root, text = "Create an assignment:").grid(row=5, column=0)
assignmentRadio2 = Radiobutton(root, text = "English", variable = Choice1, value = 2)
assignmentRadio2.grid(row=7, column=0)

# Science assignment button
Label(root, text = "Create an assignment:").grid(row=5, column=0)
assignmentRadio3 = Radiobutton(root, text = "Science", variable = Choice1, value = 3)
assignmentRadio3.grid(row=8, column=0)

# History assignmet button
Label(root, text = "Create an assignment:").grid(row=5, column=0)
assignmentRadio4 = Radiobutton(root, text = "History", variable = Choice1, value = 4)
assignmentRadio4.grid(row=9, column=0)

# Text box used to decide assignment name
assignment = Entry(root)
assignment.grid(row=10, column=0)
assignment.insert(0, "type assignment name...")
assignment_submit = Button(root, text = "Submit", command=_createAssignment).grid(row=10, column=2)
root.mainloop()

################################################################

def timeSystem():
    """A multi threaded function that keeps track of time and starts events when the time is reached"""
    _time = [0,0,0]
    while True:
        time.sleep(1)
        _time[2] += 1
        if _time[2] >= 60:
            _time[2] = 0
            _time[1] += 1
        elif _time[1] >= 60:
            _time[1] = 0
            _time[0] += 1
        print(_time)
