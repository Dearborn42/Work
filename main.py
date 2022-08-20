

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