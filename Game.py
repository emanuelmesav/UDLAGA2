from Ship import Ship
from Sky import Sky
import pygame
import random

class Game:
    
    def __init__(self, fps=80):
        
        self.width = 400
        self.height = 400        
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.fps= fps    
        
        # Load the sprite sheet        
        try:
            self.spriteSheet = pygame.image.load("sprites.png")            
        except:
            print("Error loading sprites.png")
            pygame.quit()
            return
        
        # Show the ship from the sprite sheet            
        self.shipSprite= self.loadSprite(288, 172, 16, 16)
        self.shipSprite = pygame.transform.scale(self.shipSprite, (32, 32))
        
        self.myShip = Ship()
        self.myShip.y_pos= self.height - 42
        
        self.mySky= Sky(self.width, self.height)
    
    def run(self):
        pygame.init()
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            # Clear the screen
            self.screen.fill((0, 0, 0))
            
            # Check the keys pressed
            self.checkKeys()
            
            #Show the sky
            self.showSky()
            
            #Move the sky
            self.mySky.move()
            
            # Add the ship to the screen
            self.screen.blit(self.shipSprite, (self.myShip.x_pos, self.myShip.y_pos))
            # Update display
            
            pygame.display.flip()
            
            self.clock.tick(self.fps)            
    
    
    def showSky(self):
        
        #Show each element of the sky as a circle
        
        for star in self.mySky.stars:
            pygame.draw.circle(self.screen, (100, 100, 100), star, 1)

    
    
    
    def checkKeys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.myShip.direction = "LEFT"
            self.myShip.move()
        elif keys[pygame.K_RIGHT]:
            self.myShip.direction = "RIGHT"
            self.myShip.move()
        elif keys[pygame.K_q]:
            self.fps += 5
        elif keys[pygame.K_a]:
            self.fps -= 5
        elif keys[pygame.K_SPACE]:
            self.myShip.fire()
            
    #Load a sprite from the sprite sheet in a rectangle
    def loadSprite(self, x, y, width, height):
        
        #Create a blank surface
        sprite = pygame.Surface((width, height)).convert()
        
        #Copy the sprite from the large sheet onto the smaller surface
        sprite.blit(self.spriteSheet, (0, 0), (x, y, width, height))
        
        return sprite    
    


myGame= Game()
myGame.run()