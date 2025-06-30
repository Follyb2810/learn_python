class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
class Point:
        def __init__(self,x,y):
            self.x = x
            self.y=y

        def move(self):
            print('you move your head')
    
        def draw(self):
            print('you draw your head')

point1 = Point(10,2)

print(point1.x)
point1.x=15
print(point1.x)
point1.draw()