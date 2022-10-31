from Bullet import Bullet

class Ship:
    
    def __init__(self):
        #Number of hits the ship has taken
        self.hits = 0
        self.x_pos = 0
        self.y_pos = 0
        self.length = 10
        self.direction = "RIGHT"
        self.status = "ALIVE"
        
        self.bullets= []
        
    
    def move(self):
        
        if self.direction == "RIGHT":
            self.x_pos += 1
        elif self.direction == "LEFT":
            self.x_pos -= 1
    def hit(self):
        self.hits += 1
        
    def explode(self):
        self.status = "DEAD"
        
    def fire(self):
        self.bullets.append(Bullet(self.x_pos, self.y_pos))
                
        #Check if the bullet is out of the screen
        for bullet in self.bullets:
            if bullet.y <= 0:
                bullet.direction='DOWN'


    
    
        