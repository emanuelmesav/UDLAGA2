


class Bullet:
            
        def __init__(self, x, y):    
            self.x = x    
            self.y = y
            self.vel = 8

            self.direction="UP"
    
        
        def move(self):
            if self.direction =="UP":
                self.y -=self.vel
            elif self.direction=="DOWN":
                self.y +=self.vel   