import math
radius=input("Please enter the radius")

class Circle:

    def __init__(self, radius):
        self.radius = radius
    
    def calculate_circle_area(self):
        return math.pi * self.radius**2
    
    def calculate_circle_perimeter(self):
        return 2 * math.pi * self.radius




    


    








