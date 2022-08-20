
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