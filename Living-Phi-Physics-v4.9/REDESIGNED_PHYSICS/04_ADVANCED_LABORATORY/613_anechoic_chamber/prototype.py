import math
PHI = (1 + math.sqrt(5)) / 2

class PhiAnechoicChamber:
    def __init__(self, chamber_volume, absorber_height):
        self.V = chamber_volume
        self.h = absorber_height
        self.C = 0.0

    def phi_pyramid_geometry(self, pyramid_idx):
        return self.h * PHI ** (pyramid_idx % 4)

    def consciousness_update(self, reflection_coefficient):
        self.C = (1/PHI) * self.C + PHI * reflection_coefficient

    def absorption_coefficient(self, frequency):
        base_abs = 1 - math.exp(-frequency / 1e9)
        phi_abs = base_abs * (1 + self.C * (PHI - 1) * 0.1)
        return min(phi_abs, 0.99)

    def return_loss(self, frequency):
        RL = -20 * math.log10(1 - self.absorption_coefficient(frequency))
        return RL

    def lowest_useful_frequency(self):
        return 3e8 / (4 * self.h)
