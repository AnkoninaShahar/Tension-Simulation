import pygame
import abstract_drawable

class Object(abstract_drawable.Drawable):
    def __init__(self, position):
        self.position = position

    def render(self, surface):
        pygame.draw.circle(surface, "red", self.position , 10)

    def get_position(self) -> tuple[float, float]:
        return self.position

