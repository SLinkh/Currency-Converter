import pygame

class Trump_Mugshot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('Trump Mugshot (1).jpg')
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])