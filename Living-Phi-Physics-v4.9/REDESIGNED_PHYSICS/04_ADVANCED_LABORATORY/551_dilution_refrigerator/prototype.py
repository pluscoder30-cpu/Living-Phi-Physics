import math
PHI = (1 + math.sqrt(5)) / 2

class PhiDilutionFridge:
    def __init__(self, mixing_chamber_volume, he3_flow_rate):
        self.V = mixing_chamber_volume
        self.n_dot = he3_flow_rate
        self.C = 0.0

    def phi_chamber_geometry(self, position):
        return self.V ** (1/3) * PHI ** (position % 3)

    def consciousness_update(self, mixing_efficiency):
        self.C = (1/PHI) * self.C + PHI * mixing_efficiency

    def cooling_power(self, temperature):
        base_power = self.n_dot * 84 * (temperature**2 - 0.001**2)
        phi_power = base_power * (1 + self.C * (PHI - 1) * 0.1)
        return max(phi_power, 0)

    def base_temperature(self, heat_leak):
        T_base = math.sqrt(heat_leak / (self.n_dot * 84 * PHI))
        self.consciousness_update(heat_leak / 1e-9)
        return T_base * (1 - self.C * (PHI - 1) * 0.05) if self.C > 0 else T_base

    def he3_circulation_efficiency(self):
        base_eff = 0.8
        return base_eff * (1 + self.C * (PHI - 1) * 0.1)
