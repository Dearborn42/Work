from tkinter import *
import main
root = Tk()

# Functions
def _createStudents():

    main.createStudents(int(studentsNum.get()))
    myLabel = Label(root, text = "Added " + studentsNum.get() + " Students").grid(row=5, column=0)
    #myLabel.pack()



# Start
Label(root, text = "School control panel").grid(row=1, column=0)
Label(root).grid(row=2)

# Choose how many students
Label(root, text = "Add students:").grid(row=3, column=0)
studentsNum = Entry(root, text = "Type here...")
studentsNum.grid(row=4, column=0)
studentsNum_Submit = Button(root, text = "Submit", command=_createStudents).grid(row=4, column=1)

root.mainloop()