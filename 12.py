class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius

circle = Circle(5)
print("Area: ", round(circle.area(),2))
print("Perimeter: ", round(circle.perimeter(),2))