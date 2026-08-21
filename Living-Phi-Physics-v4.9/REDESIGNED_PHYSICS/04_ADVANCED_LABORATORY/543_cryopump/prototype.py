import math
PHI = (1 + math.sqrt(5)) / 2

class PhiCryopump:
    def __init__(self, cryo_surface_area, temperature):
        self.A = cryo_surface_area
        self.T = temperature
        self.C = 0.0

    def phi_fin_geometry(self, fin_idx):
        return self.A * PHI ** (fin_idx % 4) / 10

    def consciousness_update(self, condensation_rate):
        self.C = (1/PHI) * self.C + PHI * condensation_rate

    def pumping_speed(self, gas_type):
        sticking_coefficient = {'H2O': 0.9, 'N2': 0.5, 'H2': 0.1}
        S0 = sticking_coefficient.get(gas_type, 0.3)
        base_speed = self.A * S0 * 1e-2
        return base_speed * (1 + self.C * (PHI - 1) * 0.1)

    def condensation_rate(self, pressure, gas_type):
        speed = self.pumping_speed(gas_type)
        rate = speed * pressure
        self.consciousness_update(rate / 1e-3)
        return rate * (1 + self.C * (PHI - 1) * 0.05)

    def capacity(self, gas_type, molecular_weight):
        base_capacity = self.A * 1e-3 / molecular_weight
        return base_capacity * (1 + self.C * (PHI - 1))
