import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    


class Square:
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2
    

list_figures = [Square(5), Circle(4)]

for figure in list_figures:
    print(figure.calculate_area())
