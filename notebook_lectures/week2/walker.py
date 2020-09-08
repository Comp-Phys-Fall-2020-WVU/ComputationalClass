import math as m

class Walking2D():
    # A particle moving in 2D

    def __init__(self, x=0, y=0):
        # Initially you define the initial (x,y) position.
        self.x = x
        self.y = y
        
    def move_walker(self, x_increment=0, y_increment=1):
        # Move the rocket according to the paremeters given.
        #  Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self, walker):
        # Calculates the distance from between the existing and another provided walker
        #  and returns that value.
        distance = m.sqrt((self.x-walker.x)**2+(self.y-walker.y)**2)
        return distance
