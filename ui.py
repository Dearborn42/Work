from ast import Num
import time
from time import strftime
from typing_extensions import IntVar
from main import createStudents, assignmentCreation, simulation, studentEvents
import asyncio
import tkinter as tk
import tkinter.font as tkFont
n = 0

class App:
    def __init__(self, root):
        global Log,addStudents_box,createEvent_box
        # setting title
        root.title("undefined")
        # setting window size
        width=400
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

    # Label

        Label4=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Label4["font"] = ft
        Label4["fg"] = "#333333"
        Label4["justify"] = "center"
        Label4["text"] = "Add Students:"
        Label4.place(x=10,y=10,width=82,height=20)

    # Add students box

        addStudents_box=tk.Entry(root)
        addStudents_box["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        addStudents_box["font"] = ft
        addStudents_box["fg"] = "#333333"
        addStudents_box["justify"] = "center"
        addStudents_box["text"] = "Students Num"
        addStudents_box.place(x=100,y=10,width=190,height=20)

    # Add students button

        addStudents=tk.Button(root)
        addStudents["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        addStudents["font"] = ft
        addStudents["fg"] = "#000000"
        addStudents["justify"] = "center"
        addStudents["text"] = "Add Students"
        addStudents.place(x=300,y=7,width=90,height=25)
        addStudents["command"] = self._addStudents

    # Label

        Label3=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Label3["font"] = ft
        Label3["fg"] = "#333333"
        Label3["justify"] = "center"
        Label3["text"] = "Custom Event:"
        Label3.place(x=10,y=40,width=82,height=20)

    # Create event box

        createEvent_box=tk.Entry(root)
        createEvent_box["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        createEvent_box["font"] = ft
        createEvent_box["fg"] = "#333333"
        createEvent_box["justify"] = "center"
        createEvent_box["text"] = "Event Name"
        createEvent_box.place(x=100,y=40,width=190,height=20)

    # Create event button

        createEvent=tk.Button(root)
        createEvent["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        createEvent["font"] = ft
        createEvent["fg"] = "#000000"
        createEvent["justify"] = "center"
        createEvent["text"] = "Add Event"
        createEvent.place(x=300,y=37,width=90,height=25)
        createEvent["command"] = self.GButton_864_command

    # Labels

        Label1=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Label1["font"] = ft
        Label1["fg"] = "#333333"
        Label1["justify"] = "center"
        Label1["text"] = "Start Event:"
        Label1.place(x=10,y=70,width=82,height=20)

        Label2=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Label2["font"] = ft
        Label2["fg"] = "#333333"
        Label2["justify"] = "center"
        Label2["text"] = "Start Assignment:"
        Label2.place(x=92,y=70,width=99,height=20)

    # Simulate button

        simulate=tk.Button(root)
        simulate["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        simulate["font"] = ft
        simulate["fg"] = "#000000"
        simulate["justify"] = "center"
        simulate["text"] = "Simulate"
        simulate.place(x=300,y=67,width=90,height=25)
        simulate["command"] = self.GButton_671_command

    # Logs

        LogsScroll = tk.Scrollbar(root)
        LogsList=tk.Listbox(root, yscrollcommand=LogsScroll.set)
        LogsList["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        LogsList["font"] = ft
        LogsList["fg"] = "#333333"
        LogsList["justify"] = "left"
        LogsList.place(x=10,y=180,width=380,height=410)
        LogsScroll.config(command=LogsList.yview)
        def Log(message):
            global n
            n += 1
            LogsList.insert(tk.END,f'{n}. {str(message)}')

    # Radiobuttons for events

        choice1_1=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        choice1_1["font"] = ft
        choice1_1["fg"] = "#333333"
        choice1_1["justify"] = "center"
        choice1_1["text"] = "Sport"
        choice1_1.place(x=10,y=90,width=85,height=25)
        choice1_1["value"] = "4"

        choice1_2=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        choice1_2["font"] = ft
        choice1_2["fg"] = "#333333"
        choice1_2["justify"] = "center"
        choice1_2["text"] = "Non-Sport"
        choice1_2.place(x=10,y=110,width=85,height=25)
        choice1_2["value"] = "5"

        choice1_3=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        choice1_3["font"] = ft
        choice1_3["fg"] = "#333333"
        choice1_3["justify"] = "center"
        choice1_3["text"] = "Elections"
        choice1_3.place(x=10,y=130,width=85,height=25)
        choice1_3["value"] = "6"

    # Make event

        makeEvent=tk.Button(root)
        makeEvent["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        makeEvent["font"] = ft
        makeEvent["fg"] = "#000000"
        makeEvent["justify"] = "center"
        makeEvent["text"] = "Start Event"
        makeEvent.place(x=200,y=67,width=90,height=25)
        makeEvent["command"] = self.GButton_464_command

    # Make assignment

        makeAssignment=tk.Button(root)
        makeAssignment["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=8)
        makeAssignment["font"] = ft
        makeAssignment["fg"] = "#000000"
        makeAssignment["justify"] = "center"
        makeAssignment["text"] = "Start Assignment"
        makeAssignment.place(x=200,y=100,width=90,height=25)
        makeAssignment["command"] = self.GButton_51_command

    # Radiobutton for Assignment selection

        choice2_1=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        choice2_1["font"] = ft
        choice2_1["fg"] = "#333333"
        choice2_1["justify"] = "center"
        choice2_1["text"] = "Math"
        choice2_1.place(x=92,y=90,width=85,height=25)
        choice2_1["value"] = "0"
        

        choice2_2=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        choice2_2["font"] = ft
        choice2_2["fg"] = "#333333"
        choice2_2["justify"] = "center"
        choice2_2["text"] = "English"
        choice2_2.place(x=92,y=110,width=85,height=25)
        choice2_2["value"] = "1"
        

        choice2_3=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        choice2_3["font"] = ft
        choice2_3["fg"] = "#333333"
        choice2_3["justify"] = "center"
        choice2_3["text"] = "Science"
        choice2_3.place(x=92,y=130,width=85,height=25)
        choice2_3["value"] = "2"
     

        choice2_4=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        choice2_4["font"] = ft
        choice2_4["fg"] = "#333333"
        choice2_4["justify"] = "center"
        choice2_4["text"] = "History"
        choice2_4.place(x=92,y=150,width=85,height=25)
        choice2_4["value"] = "3"

    def _addStudents(self):
        createStudents(int(addStudents_box.get()))
        Log("Generated " + addStudents_box.get() + " students. ")


    def GButton_864_command(self):
        Log("a")


    def GButton_671_command(self):
        Log("b")


    def GRadio_909_command(self):
        Log("b")


    def GRadio_361_command(self):
        print("command")


    def GRadio_704_command(self):
        print("command")


    def GButton_464_command(self):
        print("command")


    def GButton_51_command(self):
        print("command")


    def GRadio_58_command(self):
        print("command")


    def GRadio_796_command(self):
        print("command")


    def GRadio_221_command(self):
        print("command")


    def GRadio_134_command(self):
        print("command")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
