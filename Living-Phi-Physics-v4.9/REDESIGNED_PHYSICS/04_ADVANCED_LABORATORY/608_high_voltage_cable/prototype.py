import math
PHI = (1 + math.sqrt(5)) / 2

class PhiHighVoltageCable:
    def __init__(self, voltage_rating, cable_length):
        self.V = voltage_rating
        self.L = cable_length
        self.C = 0.0

    def phi_insulation_layer(self, layer_idx):
        base_thickness = 1e-3
        return base_thickness * PHI ** (layer_idx % 4)

    def consciousness_update(self, field_stress):
        self.C = (1/PHI) * self.C + PHI * field_stress

    def maximum_field(self):
        base_field = self.V / (5e-3)
        phi_field = base_field * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_field
        return phi_field

    def capacitance_per_length(self):
        return 1e-10 * (1 + self.C * (PHI - 1) * 0.05)

    def voltage_rating(self):
        base_rating = 1e5
        return base_rating * (1 + self.C * (PHI - 1) * 0.1)
