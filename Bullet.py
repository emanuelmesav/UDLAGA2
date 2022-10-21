


class Bullet:
            
        def __init__(self, x, y, radius, color, facing):    
            self.x = x    
            self.y = y
            self.vel = 8
    
        
        def move(self):    
            self.x += self.vel