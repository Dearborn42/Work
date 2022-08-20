

class student:
      
   def __init__(self, name, grade, points):
    self.name = name
    self.grade = grade
    self.points = points

s1 = student('HARRY', 'A', 12)
s2 = student('Johnny', 'C', 6)
s3 = student('Bob', 'B', 3)
s4 = student('Ryan', 'D', 49)

Points = [s1.points, s2.points, s3.points, s4.points]
Best = 0
SecondBest = 0
ThirdBest = 0
FourthBest = 0
for x in Points:
    if x > Best:
        Best = x
for y in Points:
    if y > SecondBest and y != Best:
       SecondBest = y
for z in Points:
    if z > ThirdBest and z != Best and z != SecondBest:
        ThirdBest = z


print(Best, SecondBest, ThirdBest)


#ignore this for now, I am asking for help from Mr. Bernard
#numStudents = int(input("Enter number of students."))
numStudents = 5
#creates an empty list
studentList = []
#adds a number to the list and adds as much as the user inputs
#can replace items later, they are just placeholders for now


# for x in range(0, numStudents):
#     studentList.append(x)
# print(studentList)
# >>>>>>> 4cc68add7a4d110fc2a7a837d0888c6e39ec184c
