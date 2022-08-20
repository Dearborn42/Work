
class student:
      
   def __init__(self, name, grade, points):
    self.name = name
    self.grade = grade
    self.points = points

s1 = student('HARRY', 'A', 5)
s2 = student('Johnny', 'C', 7)

Points = [s1.points, s2.points]
Best = 0


print(s1.name)
print(s2.grade)

#ignore this for now, I am asking for help from Mr. Bernard
#numStudents = int(input("Enter number of students."))
numStudents = 5
#creates an empty list
studentList = []
#adds a number to the list and adds as much as the user inputs
#can replace items later, they are just placeholders for now
for x in range(0, numStudents):
    studentList.append(x)
print(studentList)
