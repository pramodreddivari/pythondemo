"""class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area method")
    
    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Polymorphism in action
def print_shape_info(shape):
    """"""
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")
    print("-" * 20)

# Create different shape objects
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Triangle(6, 4, 5, 5, 6)
]

# Use polymorphism - same function works with different object types
for shape in shapes:
    print_shape_info(shape)

# Another example of polymorphism
def calculate_total_area(shapes_list):
    total = 0
    for shape in shapes_list:
        total += shape.area()  # Each shape calculates area differently
    return total

print(f"Total area of all shapes: {calculate_total_area(shapes):.2f}")
"""

import math

# Base Class
class Shape:
    def area(self):
        pass  # This will be overridden by subclasses

# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Subclass for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Subclass for Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Using polymorphism
shapes = [
    Circle(5),         # Circle with radius 5
    Rectangle(4, 6),   # Rectangle width 4 height 6
    Triangle(3, 7)     # Triangle base 3 height 7
]

for shape in shapes:
    print(f"Area: {shape.area():.2f}")

