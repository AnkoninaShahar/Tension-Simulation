import pygame, math
import object, abstract_drawable, abstract_physics, physics_object

class Tether(abstract_drawable.Drawable, abstract_physics.Physics):
    def __init__(self, objects: tuple[object.Object, object.Object]):
        self.objects = objects
    
    def act(self):
        distance_x = self.objects[1].get_position()[0] - self.objects[0].get_position()[0]
        distance_y = self.objects[1].get_position()[1] - self.objects[0].get_position()[1]
        forces = ((0.0, 0.0), (0.0, 0.0))

        if math.sqrt(pow(distance_x, 2) + pow(distance_y, 2)) >= 100:
            total_force = 30
            theta = (math.atan2(distance_y, distance_x), math.atan2(-distance_y, -distance_x))

            forces = (
                (total_force * math.cos(theta[0]), total_force * math.sin(theta[0])),
                (total_force * math.cos(theta[1]), total_force * math.sin(theta[1])),
            )
        
        for i in range(2):
            if isinstance(self.objects[i], physics_object.PhysicsObject):
                self.objects[i].apply_force([forces[i]])

    def render(self, surface):
        pygame.draw.line(surface, "orange", self.objects[0].get_position(), self.objects[1].get_position())
