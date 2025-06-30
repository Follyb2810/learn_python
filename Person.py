class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def talk(self,name):  
    print(f"Hi, I am {name}")
    print(f"Hi, I am {self.name}")

p1 = Person("John", 36)
print(p1.age)    
p1.talk('folly')        
