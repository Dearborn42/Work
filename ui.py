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
studentsNum = Entry(root)
studentsNum.grid(row=4, column=0)
Label(root, text = "").grid(row=4, column=1)
studentsNum_submit = Button(root, text = "Submit", command=_createStudents).grid(row=4, column=2)

logs = Label(root, text ='Logs', font = "30")  
logs.grid(row=11, column=0)
logsScroll = Scrollbar(root)
logsScroll.grid(row=12, column=1, sticky='ns')
LogsList = Listbox(root, yscrollcommand = logsScroll.set )
for line in range(1, 100): 
    LogsList.insert(END, "Number " + str(line)) 
LogsList.grid(row=12, column=0)  
 
logsScroll.config(command = LogsList.yview) 

Choice1 = IntVar()
Label(root, text = "Create an assignment:").grid(row=5, column=0)
assignmentRadio1 = Radiobutton(root, text = "Math", variable = Choice1, value = 1)
assignmentRadio1.grid(row=6, column=0)
Label(root, text = "Create an assignment:").grid(row=5, column=0)
assignmentRadio2 = Radiobutton(root, text = "English", variable = Choice1, value = 2)
assignmentRadio2.grid(row=7, column=0)
Label(root, text = "Create an assignment:").grid(row=5, column=0)
assignmentRadio3 = Radiobutton(root, text = "Science", variable = Choice1, value = 3)
assignmentRadio3.grid(row=8, column=0)
Label(root, text = "Create an assignment:").grid(row=5, column=0)
assignmentRadio4 = Radiobutton(root, text = "History", variable = Choice1, value = 4)
assignmentRadio4.grid(row=9, column=0)


assignment = Entry(root)
assignment.grid(row=10, column=0)
assignment.insert(0, "type assignment name...")
assignment_submit = Button(root, text = "Submit", command=_createStudents).grid(row=10, column=2)
root.mainloop()