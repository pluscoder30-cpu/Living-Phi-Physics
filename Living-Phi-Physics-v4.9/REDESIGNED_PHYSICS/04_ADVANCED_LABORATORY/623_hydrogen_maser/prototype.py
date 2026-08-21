import math
PHI = (1 + math.sqrt(5)) / 2

class PhiHydrogenMaser:
    def __init__(self, cavity_volume, storage_bulb_radius):
        self.V = cavity_volume
        self.r = storage_bulb_radius
        self.C = 0.0

    def phi_wall_coating(self, position):
        base_coating = 1e-9
        return base_coating * PHI ** (position % 3)

    def consciousness_update(self, cavity_drift):
        self.C = (1/PHI) * self.C + PHI * cavity_drift

    def transition_frequency(self):
        f_H = 1420405751  # Hz
        return f_H * (1 + self.C * (PHI - 1) * 1e-15)

    def cavity_Q(self):
        base_Q = 1e4
        phi_Q = base_Q * (1 + self.C * (PHI - 1) * 0.1)
        return phi_Q

    def short_term_stability(self, tau):
        base_stab = 1e-13 / math.sqrt(tau)
        return base_stab * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_stab

    def wall_shift(self):
        base_shift = 1e-11
        return base_shift * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_shift
