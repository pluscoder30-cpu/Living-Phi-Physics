import math
PHI = (1 + math.sqrt(5)) / 2

class PhiPhaseNoiseAnalyzer:
    def __init__(self, reference_frequency, measurement_bandwidth):
        self.f_ref = reference_frequency
        self.BW = measurement_bandwidth
        self.C = 0.0

    def phi_reference_stabilization(self, aging_time):
        base_drift = 1e-10 * aging_time
        return base_drift * PHI ** (-aging_time / 172800)

    def consciousness_update(self, measurement_noise):
        self.C = (1/PHI) * self.C + PHI * measurement_noise

    def sensitivity(self, offset_frequency):
        base_sens = -160 - 20 * math.log10(offset_frequency / 1e3)
        phi_sens = base_sens - 10 * math.log10(1 + self.C * (PHI - 1) * 0.1)
        return phi_sens

    def cross_correlation_improvement(self, n_correlations):
        return 10 * math.log10(math.sqrt(n_correlations)) * (1 + self.C * (PHI - 1) * 0.1)

    def measurement_accuracy(self):
        base_accuracy = 0.5  # dB
        return base_accuracy * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_accuracy
