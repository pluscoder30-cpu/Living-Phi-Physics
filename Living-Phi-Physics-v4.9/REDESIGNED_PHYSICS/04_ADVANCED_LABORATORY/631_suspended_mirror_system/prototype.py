import math
PHI = (1 + math.sqrt(5)) / 2

class PhiSuspendedMirror:
    def __init__(self, mirror_mass, n_stages):
        self.m = mirror_mass
        self.N = n_stages
        self.C = 0.0

    def phi_fiber_length(self, stage_idx):
        base_length = 0.3
        return base_length * PHI ** (stage_idx % 4)

    def consciousness_update(self, thermal_noise):
        self.C = (1/PHI) * self.C + PHI * thermal_noise

    def pendulum_frequency(self, stage_idx):
        L = self.phi_fiber_length(stage_idx)
        return 1 / (2 * math.pi) * math.sqrt(9.81 / L)

    def seismic_isolation(self, frequency):
        base_iso = 1 / (frequency / 0.1)**(2 * self.N)
        phi_iso = base_iso * (1 + self.C * (PHI - 1) * 0.1)
        return phi_iso

    def thermal_noise(self, temperature):
        k_B = 1.38e-23
        base_noise = math.sqrt(k_B * temperature / self.m)
        return base_noise * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_noise
