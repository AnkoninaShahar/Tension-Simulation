import pygame
import object, tether

class Manager:
    def __init__(self):
        self.objects = [object.Object((500.0, 100.0)), object.Object((500.0, 100.0))]
        self.tether = tether.Tether((self.objects[0], self.objects[1]))
    
    def draw(self, surface: pygame.Surface):
        for object in self.objects:
            pygame.draw.circle(surface, "red", (object.get_position()[0], object.get_position()[1]) , 10)

        self.objects[0].act()
        self.tether.act()
