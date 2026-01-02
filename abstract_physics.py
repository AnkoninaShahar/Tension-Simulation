from abc import ABC, abstractmethod

class Physics(ABC):
    @abstractmethod
    def act(self):
        pass