import math
PHI = (1 + math.sqrt(5)) / 2

class PhiMagneticSector:
    def __init__(self, radius, B_field, sector_angle):
        self.R = radius
        self.B0 = B_field
        self.theta = sector_angle
        self.C = 0.0

    def phi_gradient(self, r):
        return self.B0 * PHI ** ((r - self.R) / self.R)

    def consciousness_update(self, dispersion_error):
        self.C = (1/PHI) * self.C + PHI * dispersion_error

    def momentum_radius(self, momentum, r):
        B = self.phi_gradient(r)
        return momentum / (1.6e-19 * B)

    def mass_dispersian(self, m1, m2, kinetic_energy):
        p1 = math.sqrt(2 * m1 * kinetic_energy)
        p2 = math.sqrt(2 * m2 * kinetic_energy)
        r1 = self.momentum_radius(p1, self.R)
        r2 = self.momentum_radius(p2, self.R)
        spatial_sep = abs(r1 - r2) * math.sin(self.theta)
        self.consciousness_update(abs(r1 - r2) / self.R)
        return spatial_sep * (1 + self.C * (PHI - 1))
