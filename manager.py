import pygame
import object

class Manager:
    def __init__(self):
        self.objects = []
        self.object = object.Object()
    
    def draw(self, surface: pygame.Surface):
        pygame.draw.circle(surface, "red", (self.object.get_position()[0],self.object.get_position()[1]) , 10)
        self.object.act()
