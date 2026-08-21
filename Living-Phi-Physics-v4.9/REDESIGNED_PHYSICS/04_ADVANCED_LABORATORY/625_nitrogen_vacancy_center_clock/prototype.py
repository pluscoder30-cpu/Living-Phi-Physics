import math
PHI = (1 + math.sqrt(5)) / 2

class PhiNVClock:
    def __init__(self, nv_density, magnetic_field):
        self.n_nv = nv_density
        self.B = magnetic_field
        self.C = 0.0

    def phi_nv_orientation(self, nv_idx):
        return 2 * math.pi * nv_idx / PHI

    def consciousness_update(self, decoherence_rate):
        self.C = (1/PHI) * self.C + PHI * decoherence_rate

    def transition_frequency(self):
        f_NV = 2.87e9  # Hz
        return f_NV * (1 + self.C * (PHI - 1) * 1e-12)

    def coherence_time(self):
        base_T2 = 1e-3
        phi_T2 = base_T2 * (1 + self.C * (PHI - 1) * 0.1)
        return phi_T2

    def sensitivity(self):
        base_sens = 1e-9 / math.sqrt(self.n_nv)
        return base_sens * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_sens

    def temperature_sensitivity(self):
        base_temp_sens = 1e-5
        return base_temp_sens * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_temp_sens
