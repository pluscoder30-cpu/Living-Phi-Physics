import math
PHI = (1 + math.sqrt(5)) / 2

class PhiHighVoltageInsulator:
    def __init__(self, voltage_rating, creepage_distance):
        self.V = voltage_rating
        self.L_creepage = creepage_distance
        self.C = 0.0

    def phi_shed_spacing(self, shed_idx):
        base_spacing = 1e-2
        return base_spacing * PHI ** (shed_idx % 3)

    def consciousness_update(self, flashover_risk):
        self.C = (1/PHI) * self.C + PHI * flashover_risk

    def flashover_voltage(self, pollution_level):
        base_V = self.V * 1.5
        pollution_factor = 1 - pollution_level * 0.2
        phi_V = base_V * pollution_factor * (1 + self.C * (PHI - 1) * 0.1)
        return phi_V

    def creepage_ratio(self):
        return self.L_creepage / (self.V / 1000)

    def hydrophobicity(self):
        base_hydro = 0.8
        return base_hydro * (1 + self.C * (PHI - 1) * 0.05)
