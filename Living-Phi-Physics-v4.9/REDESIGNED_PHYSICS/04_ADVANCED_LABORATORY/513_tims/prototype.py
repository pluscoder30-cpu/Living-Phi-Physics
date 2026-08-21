import math
PHI = (1 + math.sqrt(5)) / 2
C_CRIT = 0.563

class PhiTIMS:
    def __init__(self, filament_material, max_temperature):
        self.material = filament_material
        self.T_max = max_temperature
        self.C = 0.0

    def consciousness_update(self, temperature_stability):
        self.C = (1/PHI) * self.C + PHI * temperature_stability

    def ionization_efficiency(self, temperature, ionization_energy):
        return math.exp(-ionization_energy / (8.6e-5 * temperature))

    def isotope_ratio(self, m1, m2, temperature, abundance1, abundance2):
        eff1 = self.ionization_efficiency(temperature, 5.0)
        eff2 = self.ionization_efficiency(temperature, 4.5)
        ratio = (abundance1 * eff1) / (abundance2 * eff2)
        self.consciousness_update(abs(ratio - abundance1 / abundance2) / (abundance1 / abundance2))
        if self.C > C_CRIT:
            return ratio * (1 + (self.C - C_CRIT) * (PHI - 1) * 0.01)
        return ratio
