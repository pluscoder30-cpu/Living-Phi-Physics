import math
PHI = (1 + math.sqrt(5)) / 2

class PhiGroundingPlane:
    def __init__(self, plane_size, conductor_width):
        self.L = plane_size
        self.w = conductor_width
        self.C = 0.0

    def phi_grid_spacing(self, position):
        base_spacing = 0.1
        return base_spacing * PHI ** (position % 3)

    def consciousness_update(self, ground_impedance):
        self.C = (1/PHI) * self.C + PHI * ground_impedance

    def impedance(self, frequency):
        mu = 4 * math.pi * 1e-7
        sigma = 5.8e7
        delta = math.sqrt(2 / (mu * sigma * 2 * math.pi * frequency))
        base_Z = 1 / (sigma * self.w * delta)
        phi_Z = base_Z * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_Z
        return phi_Z

    def resonance_frequency(self):
        return 3e8 / (2 * self.L * math.sqrt(2))

    def ground_current_distribution(self, injection_point):
        return 1.0 / (1 + abs(injection_point - self.L/2) / self.L)
