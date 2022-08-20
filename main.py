print("test")

class Person:
  def __init__(self, name, grade, points):
    self.name = name
    self.grade = grade
    self.points = points

  def myfunc(x):
    print(x.name, x.grade, x.points)


p1 = Person("John", 'B', 3)
p2 = Person("Joe", 'A', 6)

Person.myfunc(p1)
Person.myfunc(p2)