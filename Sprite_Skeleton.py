import pygame
from pygame.locals import *

class User_Sprite(pygame.sprite.Sprite):
    #Starting position and speed
    x = 250
    y = 250

    #Constructor
    def __init__(self):
        super(User_Sprite, self).__init__() #some inhertiance crap. don't worry about it

        #Create a surface and give it a size
        self.image = pygame.Surface([130, 130])

        self.image.set_colorkey((255, 255, 255))

        #Create an image and give it a png picture
        self.image = pygame.image.load("images/red_mushroom.png").convert_alpha()
        
        #Create a rect with the size of the image and center it on it's location
        self.rect = self.image.get_rect(center=(self.x, self.y))
