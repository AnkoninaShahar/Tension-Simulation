import pygame
import object, tether, physics_object, abstract_drawable, abstract_physics

class Manager:
    def __init__(self):
        physics_objects = [physics_object.PhysicsObject((200.0, 100.0)), 
                           physics_object.PhysicsObject((100.0, 100.0))
                           ]
        
        static_objects = [object.Object((500.0, 100.0)), 
                          object.Object((800.0, 150.0))]
        
        tethers = [tether.Tether((physics_objects[0], static_objects[0])),
                   tether.Tether((physics_objects[0], physics_objects[1])),
                   tether.Tether((physics_objects[1], static_objects[1]))
                   ]
        
        self.objects = []
        self.objects += physics_objects
        self.objects += static_objects
        self.objects += tethers
    
    def draw(self, surface: pygame.Surface):
        for object in self.objects:
            if isinstance(object, abstract_drawable.Drawable):
                object.render(surface)
            if isinstance(object, abstract_physics.Physics):
                object.act()
