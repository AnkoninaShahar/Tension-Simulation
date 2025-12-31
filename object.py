class Object:
    def __init__(self):
        self.position = (200.0, 0.0)
        self.velocity = (0.0, 0.0)
        self.mass = 1

        self.forces = [(0.0, 9.81)]

    def act(self):
        force_vector = self.calculate_force()
        acceleration_vector = (force_vector[0]/self.mass, force_vector[1]/self.mass)

        self.velocity = (self.velocity[0] + acceleration_vector[0] / 9, self.velocity[1] + acceleration_vector[1] / 9)
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])

    def add_froce(self, force):
        self.forces.__add__(force)

    def calculate_force(self) -> tuple[float, float]:
        sum_force = (0.0, 0.0)
        for force in self.forces:
            sum_force = (sum_force[0] + force[0], sum_force[1] + force[1])
        return sum_force
    
    def get_position(self) -> tuple[float, float]:
        return self.position

