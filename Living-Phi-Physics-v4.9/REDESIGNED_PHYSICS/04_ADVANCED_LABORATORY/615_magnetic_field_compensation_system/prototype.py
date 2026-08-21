import math
PHI = (1 + math.sqrt(5)) / 2

class PhiMagneticCompensation:
    def __init__(self, coil_radius, n_turns):
        self.R = coil_radius
        self.N = n_turns
        self.C = 0.0

    def phi_coil_position(self, coil_idx):
        return self.R * PHI ** (coil_idx % 3)

    def consciousness_update(self, residual_field):
        self.C = (1/PHI) * self.C + PHI * residual_field

    def field_cancellation(self, ambient_field, compensation_current):
        mu_0 = 4 * math.pi * 1e-7
        B_comp = mu_0 * self.N * compensation_current / (2 * self.R)
        residual = ambient_field - B_comp
        self.consciousness_update(abs(residual) / ambient_field if ambient_field > 0 else 0)
        return residual * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else residual

    def cancellation_ratio(self, ambient_field, residual_field):
        return ambient_field / residual_field if residual_field > 0 else float('inf')

    def bandwidth(self):
        base_BW = 1e3
        return base_BW * (1 + self.C * (PHI - 1) * 0.1)
