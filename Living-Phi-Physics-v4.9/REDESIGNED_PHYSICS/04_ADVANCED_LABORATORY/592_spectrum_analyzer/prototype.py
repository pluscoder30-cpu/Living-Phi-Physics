import math
PHI = (1 + math.sqrt(5)) / 2

class PhiSpectrumAnalyzer:
    def __init__(self, frequency_range, resolution_bandwidth):
        self.f_range = frequency_range
        self.RBW = resolution_bandwidth
        self.C = 0.0

    def phi_window(self, sample_idx, n_samples):
        return 0.5 * (1 - math.cos(2 * math.pi * sample_idx / n_samples)) * PHI ** (sample_idx % 3)

    def consciousness_update(self, noise_floor):
        self.C = (1/PHI) * self.C + PHI * noise_floor

    def dynamic_range(self):
        base_DR = 80
        phi_DR = base_DR * (1 + self.C * (PHI - 1) * 0.1)
        return phi_DR

    def sensitivity(self):
        base_sens = -130  # dBm
        phi_sens = base_sens - 10 * math.log10(1 + self.C * (PHI - 1) * 0.1)
        return phi_sens

    def sweep_time(self, n_points):
        return n_points / self.RBW * (1 + self.C * (PHI - 1) * 0.05)
