import object, abstract_physics

class PhysicsObject(object.Object, abstract_physics.Physics):
    def __init__(self, position, mass = 1):
        super().__init__(position)
        self.velocity = (0.0, 0.0)
        self.mass = mass

        self.forces = [(0.0, 9.81)]

    def act(self):
        force_vector = self.calculate_force()
        acceleration_vector = (force_vector[0]/self.mass, force_vector[1]/self.mass)

        self.velocity = (self.velocity[0] + acceleration_vector[0] / 9, self.velocity[1] + acceleration_vector[1] / 9)
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])

        self.velocity = (self.velocity[0] * 0.95, self.velocity[1] * 0.95)
        self.reset_forces()

    def apply_force(self, force):
        self.forces += force

    def reset_forces(self):
        self.forces = [(0.0, 9.81)]

    def calculate_force(self) -> tuple[float, float]:
        sum_force = (0.0, 0.0)
        for force in self.forces:
            sum_force = (round(sum_force[0] + force[0]), round(sum_force[1] + force[1]))
        return sum_force
    
    def get_velocity(self) -> tuple[float, float]:
        return self.velocity