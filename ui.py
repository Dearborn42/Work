import time
from time import strftime
from tkinter import *
from main import createStudents,assignmentCreation
import asyncio
root = Tk()
root.title("School control panel")

# Functions


def _createStudents():
    createStudents(int(studentsNum.get()))
    Log("Generated " + studentsNum.get() + " students. ")

def _createAssignment():
    assignmentCreation(int(Choice1.get()))

################################################################

# Choose how many students
Label(root, text = "Add students:").grid(row=3, column=0)
studentsNum = Entry(root)
studentsNum.grid(row=4, column=0)
Label(root, text = "").grid(row=4, column=1)
studentsNum_submit = Button(root, text = "Submit", command=_createStudents).grid(row=4, column=2)

################################################################

logs = Label(root, text ='Logs', font = "30")  
logs.grid(row=11, column=0)
logsScroll = Scrollbar(root)
logsScroll.grid(row=12, column=1, sticky='ns')
LogsList = Listbox(root, yscrollcommand = logsScroll.set )

line = 1
def Log(message):
    LogsList.insert(END, str(message) + str(line)) 

LogsList.grid(row=12, column=0)  

################################################################
 
logsScroll.config(command = LogsList.yview) 
Choice1 = IntVar()
Label(root, text = "Create an assignment:").grid(row=5, column=0)
assignmentRadio1 = Radiobutton(root, text = "Math", variable = Choice1, value = 0)
assignmentRadio1.grid(row=6, column=0)
Label(root, text = "Create an assignment:").grid(row=5, column=0)
assignmentRadio2 = Radiobutton(root, text = "English", variable = Choice1, value = 1)
assignmentRadio2.grid(row=7, column=0)
Label(root, text = "Create an assignment:").grid(row=5, column=0)
assignmentRadio3 = Radiobutton(root, text = "Science", variable = Choice1, value = 2)
assignmentRadio3.grid(row=8, column=0)
Label(root, text = "Create an assignment:").grid(row=5, column=0)
assignmentRadio4 = Radiobutton(root, text = "History", variable = Choice1, value = 3)
assignmentRadio4.grid(row=9, column=0)
assignment = Entry(root)
assignment.grid(row=10, column=0)
assignment.insert(0, "type assignment name...")
assignment_submit = Button(root, text = "Submit", command=_createAssignment).grid(row=10, column=2)

root.mainloop()

################################################################

# import the time module


def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t += 1
        if t == 120:
            t = 1


t = 1
#countdown(int(t))
