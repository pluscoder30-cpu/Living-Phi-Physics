import math
PHI = (1 + math.sqrt(5)) / 2
C_CRIT = 0.563

class PhiESI:
    def __init__(self, capillary_diameter, voltage, flow_rate):
        self.d0 = capillary_diameter
        self.V = voltage
        self.Q = flow_rate
        self.C = 0.0

    def consciousness_update(self, cone_stability):
        self.C = (1/PHI) * self.C + PHI * cone_stability

    def droplet_size(self, surface_tension, conductivity):
        base_size = (self.Q * surface_tension / (conductivity * self.V**2))**(1/3)
        self.consciousness_update(1.0 / base_size if base_size > 0 else 0)
        if self.C > C_CRIT:
            return base_size * (1 - (self.C - C_CRIT) * PHI * 0.1)
        return base_size

    def charge_limit(self, droplet_radius):
        rayleigh_limit = 64 * math.pi * 8.85e-12 * droplet_radius**3 * 0.072
        return rayleigh_limit / 1.6e-19

    def ionization_efficiency(self, analyte_concentration):
        base_eff = 0.01 * analyte_concentration
        return base_eff * (1 + self.C * (PHI - 1))
