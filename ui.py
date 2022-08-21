from tkinter import *
import main
root = Tk()
root.title("School control panel")

# Functions
def _createStudents():
    main.createStudents(int(studentsNum.get()))
    Label(root, text = "Added " + studentsNum.get() + " Students").grid(row=5, column=0)
    #myLabel.pack()

def _createEvents():
    print()

def _createAssignment():
    print()

# Choose how many students
Label(root, text = "Add students:").grid(row=3, column=0)
studentsNum = Entry(root, text = "Type here...")
studentsNum.grid(row=4, column=0)
studentsNum_Submit = Button(root, text = "Submit", command=_createStudents).grid(row=4, column=1)


root.mainloop()