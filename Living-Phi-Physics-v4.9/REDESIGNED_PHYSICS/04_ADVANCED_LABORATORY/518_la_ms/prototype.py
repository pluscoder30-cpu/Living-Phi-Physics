import math
PHI = (1 + math.sqrt(5)) / 2

class PhiLA_MS:
    def __init__(self, laser_energy, spot_size):
        self.E_laser = laser_energy
        self.w = spot_size
        self.C = 0.0

    def phi_beam_profile(self, r):
        return self.E_laser * PHI ** (-r**2 / self.w**2)

    def consciousness_update(self, ablation_precision):
        self.C = (1/PHI) * self.C + PHI * ablation_precision

    def ion_signal(self, r, element, ionization_energy):
        intensity = self.phi_beam_profile(r)
        T = 1e4 * (intensity / self.E_laser)**0.5
        ionization = math.exp(-ionization_energy / (8.6e-5 * T))
        signal = (intensity / 3.0)**0.5 * ionization * 1e6 if intensity > 3e-3 else 0
        self.consciousness_update(signal / 1e6 if signal > 0 else 0)
        return signal * (1 + self.C * (PHI - 1) * 0.1)

    def spatial_resolution(self):
        classical_res = self.w / 2
        return classical_res * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else classical_res
