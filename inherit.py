class Mammal:
    def walk(self):
        print('you walking')


class Dog(Mammal):
        def bark(self):
             print('dog is barking')

class Cat(Mammal):
    pass

# use pass when clsss is empty
class Horse(Mammal):
    pass

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()