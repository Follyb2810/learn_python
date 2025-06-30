class Point:
    def move(self):
        print('you move your head')
    
    def draw(self):
        print('you draw your head')


point1 = Point()
point1.draw()
point1.move()
point1.x=10
point1.y=10
print(point1.x)