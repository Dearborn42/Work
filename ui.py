import time
from time import strftime
from tkinter import *
import main
import asyncio
root = Tk()
root.title("School control panel")

# Functions


def _createStudents():
    main.createStudents(int(studentsNum.get()))
    Label(root, text="Added " + studentsNum.get() +
          " Students").grid(row=5, column=0)
    # myLabel.pack()


def _createEvents():
    print()


def _createAssignment():
    print()


# Choose how many students
Label(root, text="Add students:").grid(row=3, column=0)
studentsNum = Entry(root, text="Type here...")
studentsNum.grid(row=4, column=0)
studentsNum_Submit = Button(
    root, text="Submit", command=_createStudents).grid(row=4, column=1)


root.mainloop()

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
countdown(int(t))
