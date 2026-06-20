class Circle:
    def __init__(self, radius):
        # self._radius = radius
        self.__radius = radius

    def calculate_area(self):
        # return math.pi * self._radius ** 2
        return math.pi * self.__radius ** 2
        
    
    def calculate_perimeter(self):
        # return 2 * math.pi * self._radius
        return 2 * math.pi * self.__radius
    
##NAME MANGLING