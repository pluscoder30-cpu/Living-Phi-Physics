import math
PHI = (1 + math.sqrt(5)) / 2

class PhiLidar:
    def __init__(self, pulse_energy, pulse_width):
        self.E = pulse_energy
        self.tau = pulse_width
        self.C = 0.0

    def phi_pulse_code(self, pulse_idx):
        return self.tau * PHI ** (pulse_idx % 5)

    def consciousness_update(self, range_error):
        self.C = (1/PHI) * self.C + PHI * range_error

    def range_resolution(self):
        base_res = 3e8 * self.tau / 2
        phi_res = base_res * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_res
        return phi_res

    def maximum_range(self, target_reflectivity, atmospheric_transmission):
        base_range = math.sqrt(self.E * target_reflectivity * atmospheric_transmission / 1e-12)
        return base_range * (1 + self.C * (PHI - 1) * 0.05)

    def point_density(self, scan_rate, range):
        base_density = scan_rate / (4 * math.pi * range**2)
        return base_density * (1 + self.C * (PHI - 1) * 0.1)
