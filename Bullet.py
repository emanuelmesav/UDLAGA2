


class Bullet:
            
        def __init__(self, x, y):    
            self.x = x    
            self.y = y
            self.vel = 8
    
        
        def move(self):
            
            self.y -= self.vel