import math
PHI = (1 + math.sqrt(5)) / 2

class PhiRFFilter:
    def __init__(self, cutoff_frequency, n_stages):
        self.fc = cutoff_frequency
        self.N = n_stages
        self.C = 0.0

    def phi_capacitor_value(self, stage_idx):
        base_C = 1e-12
        return base_C * PHI ** (stage_idx % 3)

    def consciousness_update(self, insertion_loss):
        self.C = (1/PHI) * self.C + PHI * insertion_loss

    def insertion_loss(self, frequency):
        base_IL = 20 * self.N * math.log10(frequency / self.fc)
        phi_IL = base_IL * (1 + self.C * (PHI - 1) * 0.1)
        return phi_IL

    def cutoff_frequency(self):
        return self.fc * (1 + self.C * (PHI - 1) * 0.05)

    def return_loss(self, frequency):
        return self.insertion_loss(frequency) * 0.5
