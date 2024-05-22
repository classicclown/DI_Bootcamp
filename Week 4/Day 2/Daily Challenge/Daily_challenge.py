import math
import turtle
class Circle:

    def __init__(self,variable, measurement):
        if variable == 'r':
            self.radius=measurement
            self.diameter=measurement*2
        elif variable == 'd':
            self.diameter=measurement
            self.radius=measurement/2
        else:
            print('Invalid variable condition')
        

    def area(self):
        return math.pi*self.radius**2

    def __str__(self):
        print (f"Radius: {self.radius}, Diameter: {self.diameter}, Area: {self.area()}")

    def __add__(self,circle2):
        new_circle= self.radius+circle2.radius
        return (f'New radius: {new_circle}')
    
    def __gt__(self, circle2):
        if self.radius>circle2.radius:
            return True
        else:
            return False
    def __eq__(self,circle2):
        if self.radius==circle2.radius:
            return True
        else:
            return False
    def sorted (self,circle2):
        circle_list=[self.radius, circle2.radius]
        return sorted(circle_list)
    
    def print_circle(self):
        s= turtle.Screen()
        t = turtle.Turtle()
        t.penup()
        t.goto(0,-self.radius)
        t.pendown()
        t.circle(self.radius)
        turtle.Screen().exitonclick()

circle1 = Circle('r',100)
circle2=Circle('d',4)
print(circle1.sorted(circle2))
print(circle1.__add__(circle2))
circle1.print_circle()