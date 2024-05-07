import pygame

class Start_Searching_Button:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("Start Button Law Database.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    # def rescale_image(self):
    #     self.image_size = self.image.get_size()
    #     scale_size = (self.image_size[0] * .02, self.image_size[1] * .02)
    #     self.image = pygame.transform.scale(self.image, scale_size)
