import pygame

class Input_Done_Button:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("Input Done Button.png")
        self.rect = pygame.Rect(self.x, self.y)

