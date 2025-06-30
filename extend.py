class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f"Hi, I am {self.name}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")


s1 = Student("Alice", 22, "STU123")
s1.talk()       # Inherited method from Person
s1.study()      # Own method
print(s1.age)   # Inherited property


class Student(Person):
    def talk(self):  # Override the talk method
        print(f"I'm {self.name}, and I'm a student.")
        
super().talk()


