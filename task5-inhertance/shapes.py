import math
class Shape:
    """
    A base class for all shapes.
    """
    def __init__(self, name):
        """
        Initialize the shape with a name.
        """
        self.name = name
    def area(self):
        """
        Calculate the area of the shape.
        """
        raise NotImplementedError("Subclasses must be implemented this method.")
    def __str__(self):
        """
        Return a string representation of the shape.
        """
        return f"Shape: {self.name}"
class Circle(Shape):
    """
    A class to represnt a circle.
    """
    def __init__(self, radius):
        """
        initialize the circle with a radius.
        args:
            radius (float): The radius of the circle.
        """  
        super().__init__("Circle")
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius
    def area(self):
        """
        Calculate the area of the circle.
        """
        return math.pi * (self.radius ** 2)
    def __str__(self):
        """
        Return a string representation of the circle.
        """
        return f"{super().__str__()}, Radius: {self.radius}, Area: {self.area():.2f}"
class Rectangle(Shape):
    """
    A class to represent a rectangle.
    """
    def __init__(self, width, height):
        """
        initialize the rectangle with width and height.
        args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        super().__init__("Rectangle")
        if width <= 0 or height <=0:
            raise ValueError("Width and height must be positive.")
        self.width = width
        self.height = height
    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.width * self.height
    def __str__(self):
        """
        Return a string representation of the rectangle.
        """
        return f"{super().__str__()}, Width: {self.width}, Height: {self.height}, Area: {self.area():.2f}"
class Triangle(Shape):
    """
    A class to represent a triangle.
    """
    def __init__(self, base, height):
        """
        Initialize the trianngle with base and height.
        args:
            base (float): The base of the triangle.
            height (float): The height of the triangle.
        """
        super().__init__("Triangle")
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive.")
        self.base = base
        self.height = height
    def area(self):
        """
        Calculate the area of the triangle.
        """
        return 0.5 * self.base * self.height
    def __str__(self):
        """
        Return a string representation of the triangle.
        """
        return f"{super().__str__()}, Base: {self.base}, Height: {self.height}, Area: {self.area():.2f}"
    class Square(Shape):
        """
        A class to represent a square.
        """
        def __init__(self, side):
            """
            Initialize the square with a side length.
            args:
                side (float): The length of the side of the square.
            """
            super().__init__("Square")
            if side <= 0:
                raise ValueError("Side must be positive.")
            self.side = side
        def area(self):
            """
            Calculate the area of the square.
            """
            return self.side ** 2
        def __str__(self):
            """
            Return a string representation of the square.
            """
            return f"{super().__str__()}, Side: {self.side}, Area: {self.area():.2f}"
