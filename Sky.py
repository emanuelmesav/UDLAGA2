import random

class Sky:
    
    def __init__(self, width, height):
        
        # Create a list of 50 stars at random positions from 0 to width and 0 to height
        self.height = height
        self.width = width
        self.stars = []
        for i in range(50):
            self.stars.append([random.randint(0, width), random.randint(0, height)])
    
    
    def move(self):
        for star in self.stars:
            star[1] += 1
            if star[1] > self.height:
                star[1] = 0
               # star[0] = random.randint(0, self.width)        