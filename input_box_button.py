import pygame
class Input_Box_Button:

    def __init__(self):
        self.x = x
        self.y = y
        self.image = pygame.image.load('Input New Law Case Image.png')
        self.rect = pygame.Rect(self.x, self.y)
    def collide_point(self, pos):
        if