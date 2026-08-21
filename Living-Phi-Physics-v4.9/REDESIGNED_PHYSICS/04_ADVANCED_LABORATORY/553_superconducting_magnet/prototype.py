import math
PHI = (1 + math.sqrt(5)) / 2

class PhiSuperconductingMagnet:
    def __init__(self, n_turns, critical_current):
        self.N = n_turns
        self.Ic = critical_current
        self.C = 0.0

    def phi_winding_pitch(self, turn_idx):
        return 1e-3 * PHI ** (turn_idx % 5)

    def consciousness_update(self, field_error):
        self.C = (1/PHI) * self.C + PHI * field_error

    def field_homogeneity(self, sample_volume):
        base_error = 1e-4
        phi_error = base_error * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_error
        return phi_error

    def quench_current(self, temperature):
        Tc = 9.2
        base_Ic = self.Ic * math.sqrt(1 - (temperature / Tc)**2) if temperature < Tc else 0
        self.consciousness_update(abs(base_Ic - self.Ic) / self.Ic if self.Ic > 0 else 0)
        return base_Ic * (1 + self.C * (PHI - 1) * 0.05)

    def stored_energy(self, current):
        L = 1e-3 * self.N * PHI
        return 0.5 * L * current**2
