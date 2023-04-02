from PIL import Image, ImageDraw

class Canvas:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.image = Image.new("RGB", (width, height), color)
    
    def make(self, filename):
        self.image.save(filename)

class Square:
    """
    A class to represent a square.

    Attributes:
    ----------
    x : int
        The x-coordinate of the top-left corner of the square.
    y : int
        The y-coordinate of the top-left corner of the square.
    side : int
        The length of the side of the square.
    color : str
        The color of the square in hex format, e.g. "#FF0000" for red.
    """
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color
    
    def draw(self, canvas):
        """
        Draw the square on the provided canvas.

        Parameters:
        ----------
        canvas : PIL.Image.Image
            The canvas on which to draw the square.
        """
        draw = ImageDraw.Draw(canvas)
        x1 = self.x
        y1 = self.y
        x2 = self.x + self.side
        y2 = self.y + self.side
        draw.rectangle([x1, y1, x2, y2], fill=self.color)

class Rectangle:
    """
    A class to represent a rectangle.

    Attributes:
    ----------
    x : int
        The x-coordinate of the top-left corner of the rectangle.
    y : int
        The y-coordinate of the top-left corner of the rectangle.
    width : int
        The width of the rectangle.
    height : int
        The height of the rectangle.
    color : str
        The color of the rectangle in hex format, e.g. "#FF0000" for red.
    """
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    
    def draw(self, canvas):
        """
        Draw the rectangle on the provided canvas.

        Parameters:
        ----------
        canvas : PIL.Image.Image
            The canvas on which to draw the rectangle.
        """
        draw = ImageDraw.Draw(canvas)
        x1 = self.x
        y1 = self.y
        x2 = self.x + self.width
        y2 = self.y + self.height
        draw.rectangle([x1, y1, x2, y2], fill=self.color)


##################### TESTING #####################
# Define the size of the canvas
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500

# Define the filename for the output image
IMAGE_FILENAME = "output.png"

# Initialize the canvas
canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT, "#FFFFFF")

# Get input from the user to create squares and rectangles
shapes = []
while True:
    shape_type = input("Enter 'square' or 'rectangle' to add a shape, or 'done' to finish: ")
    if shape_type == "square":
        x = int(input("Enter the x-coordinate of the top-left corner of the square: "))
        y = int(input("Enter the y-coordinate of the top-left corner of the square: "))
        side = int(input("Enter the length of the side of the square: "))
        color = input("Enter the color of the square in hex format, e.g. '#FF0000' for red: ")
        square = Square(x, y, side, color)
        shapes.append(square)
    elif shape_type == "rectangle":
        x = int(input("Enter the x-coordinate of the top-left corner of the rectangle: "))
        y = int(input("Enter the y-coordinate of the top-left corner of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enter the height of the rectangle: "))
        color = input("Enter the color of the rectangle in hex format, e.g. '#FF0000' for red: ")
        rectangle = Rectangle(x, y, width, height, color)
        shapes.append(rectangle)
    elif shape_type == "done":
        break

# Draw the shapes on the canvas
for shape in shapes:
    shape.draw(canvas.image)

# Save the image file
canvas.make(IMAGE_FILENAME)

# Open the image file in the default image viewer
Image.open(IMAGE_FILENAME).show()
