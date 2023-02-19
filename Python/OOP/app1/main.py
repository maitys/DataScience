from random import randint
import turtle

############################################################
# Create a class called Point, which represents a point in two-dimensional space. 
# A point has x and y coordinates, for example, (0, 0) is the origin.
############################################################
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False

############################################################
# Create a class called Rectangle. A rectangle is defined by two points, 
# for example, bottom-left and top-right.
############################################################
class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)

############################################################
# Create a class called GuiRectangle. This class inherits from 
# the Rectangle class and draws the rectangle in Gui
############################################################
class GuiRectangle(Rectangle):
    
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x) 
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x) 
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        

############################################################
# Create a class called GuiPoint. This class inherits from
# the Point class and draws the point in Gui
############################################################
class GuiPoint(Point):
    
    def draw(self, canvas, size=10, color="red"):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)



# Create rectangle object
point1 = Point(randint(0, 400), randint(0, 400))
point2 = Point(randint(10, 400), randint(10, 400))
rectangle = GuiRectangle(point1, point2)

# Print rectangle coordinates
print("Rectangle Coordinates: ",
      rectangle.point1.x, ",",
      rectangle.point1.y, "and",
      rectangle.point2.x, ",",
      rectangle.point2.y)

# Get point and area from user
print("*" * 50)
user_point = GuiPoint(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game result
print("*" * 50)
print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle))
print("Your area was off by: ", rectangle.area() - user_area)
print("*" * 50)

myturtle = turtle.Turtle()
rectangle.draw(canvas=myturtle)
user_point.draw(canvas=myturtle)
turtle.done()