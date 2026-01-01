import math
import object

class Tether:
    def __init__(self, objects: tuple[object.Object, object.Object]):
        self.objects = objects
    
    def act(self):
        distance_x = self.objects[1].get_position()[0] - self.objects[0].get_position()[0]
        distance_y = self.objects[1].get_position()[1] - self.objects[0].get_position()[1]
        forces = ((0.0, 0.0), (0.0, 0.0))

        if math.sqrt(pow(distance_x, 2) + pow(distance_y, 2)) >= 200:
            forces = (
                (distance_x, distance_y),
                (-distance_x, -distance_y),
            )
    
        self.objects[0].apply_force([forces[0]])
        self.objects[1].apply_force([forces[1]])
