import math
PHI = (1 + math.sqrt(5)) / 2

class PhiRFSignalGenerator:
    def __init__(self, center_frequency, output_power):
        self.f0 = center_frequency
        self.P_out = output_power
        self.C = 0.0

    def phi_pll_bandwidth(self, offset_frequency):
        base_bw = 1e3
        return base_bw * PHI ** (int(math.log10(offset_frequency + 1)) % 3)

    def consciousness_update(self, phase_noise):
        self.C = (1/PHI) * self.C + PHI * phase_noise

    def phase_noise(self, offset_frequency):
        base_noise = -100 - 20 * math.log10(offset_frequency / 1e3)
        phi_noise = base_noise - 10 * math.log10(1 + self.C * (PHI - 1) * 0.1)
        return phi_noise

    def spurious_free_dynamic_range(self):
        base_SFDR = 70  # dBc
        phi_SFDR = base_SFDR * (1 + self.C * (PHI - 1) * 0.1)
        return phi_SFDR

    def frequency_accuracy(self):
        base_accuracy = 1e-6
        return base_accuracy * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_accuracy
