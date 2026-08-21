import math
PHI = (1 + math.sqrt(5)) / 2

class PhiCryoVacPump:
    def __init__(self, cryo_area, temperature):
        self.A = cryo_area
        self.T = temperature
        self.C = 0.0

    def phi_fin_geometry(self, fin_idx):
        return self.A * PHI ** (fin_idx % 4) / 10

    def consciousness_update(self, condensation_efficiency):
        self.C = (1/PHI) * self.C + PHI * condensation_efficiency

    def pumping_speed(self, gas_type):
        sticking = {'H2O': 0.95, 'N2': 0.6, 'H2': 0.15, 'Ar': 0.5}
        S0 = sticking.get(gas_type, 0.3)
        base_speed = self.A * S0 * 1e-2
        return base_speed * (1 + self.C * (PHI - 1) * 0.1)

    def ultimate_pressure(self):
        base_P = self.T * 1e-12
        return base_P * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_P

    def capacity(self, gas_type, molecular_weight):
        base_capacity = self.A * 1e-3 / molecular_weight
        return base_capacity * (1 + self.C * (PHI - 1))
