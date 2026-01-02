from abc import ABC, abstractmethod
import pygame

class Drawable(ABC):
    @abstractmethod
    def render(self, surface: pygame.Surface):
        pass