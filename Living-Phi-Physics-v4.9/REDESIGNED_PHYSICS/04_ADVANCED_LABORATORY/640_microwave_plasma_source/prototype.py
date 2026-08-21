import math
PHI = (1 + math.sqrt(5)) / 2

class PhiMicrowavePlasma:
    def __init__(self, microwave_frequency, power):
        self.f = microwave_frequency
        self.P = power
        self.C = 0.0

    def phi_cavity_dimension(self, dim_idx):
        base_dim = 3e8 / (2 * self.f)
        return base_dim * PHI ** (dim_idx % 3)

    def consciousness_update(self, plasma_instability):
        self.C = (1/PHI) * self.C + PHI * plasma_instability

    def ecr_condition(self):
        B_res = 2 * math.pi * self.f * 9.11e-31 / (1.6e-19)
        return B_res

    def plasma_density(self):
        base_n = self.P * 1e12
        phi_n = base_n * (1 + self.C * (PHI - 1) * 0.1)
        return phi_n

    def plasma_stability(self):
        base_stability = 0.9
        return base_stability * (1 + self.C * (PHI - 1) * 0.05)
