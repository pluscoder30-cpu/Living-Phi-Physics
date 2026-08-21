import math
PHI = (1 + math.sqrt(5)) / 2

class PhiEMPShield:
    def __init__(self, shield_thickness, conductivity):
        self.t = shield_thickness
        self.sigma = conductivity
        self.C = 0.0

    def phi_layer_spacing(self, layer_idx):
        base_spacing = self.t / 5
        return base_spacing * PHI ** (layer_idx % 3)

    def consciousness_update(self, field_penetration):
        self.C = (1/PHI) * self.C + PHI * field_penetration

    def skin_depth(self, frequency):
        mu = 4 * math.pi * 1e-7
        return math.sqrt(2 / (mu * self.sigma * 2 * math.pi * frequency))

    def shielding_effectiveness(self, frequency):
        delta = self.skin_depth(frequency)
        base_SE = 20 * math.log10(math.e) * self.t / delta
        phi_SE = base_SE * (1 + self.C * (PHI - 1) * 0.1)
        return phi_SE

    def rise_time_limitation(self):
        base_limit = 1e-9
        return base_limit * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_limit
