import math
PHI = (1 + math.sqrt(5)) / 2

class PhiMagneticMomentum:
    def __init__(self, field_strength, path_length):
        self.B0 = field_strength
        self.L = path_length
        self.C = 0.0

    def phi_field(self, x):
        return self.B0 * PHI ** (x / self.L)

    def consciousness_update(self, field_error):
        self.C = (1/PHI) * self.C + PHI * field_error

    def radius_from_momentum(self, momentum, x=0):
        B = self.phi_field(x)
        return momentum / (1.6e-19 * B)

    def momentum_resolution(self, momentum, position_error):
        r = self.radius_from_momentum(momentum)
        dr = position_error
        self.consciousness_update(dr / r)
        base_resolution = momentum * dr / r
        return base_resolution * (1 + self.C * (PHI - 1) * 0.1)

    def deflection_angle(self, momentum, path_length):
        r = self.radius_from_momentum(momentum)
        return path_length / r * (1 + self.C * (PHI - 1) * 0.01)
