class Rectangle:
    
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    def area(self):
        return self.width * self.height
    
    def distance_to_point(self, x, y):
        return ((self.x - x)**2 + (self.y - y)**2)**0.5
    
    def time_to_point(self, x, y, speed):
        return self.distance_to_point(x, y) / speed
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
rect1 = Rectangle(10, 20, 0, 0)
print(rect1.area())

rect2 = Rectangle(3, 4, 1, 2)
print(rect2.time_to_point(2, 3, 20))