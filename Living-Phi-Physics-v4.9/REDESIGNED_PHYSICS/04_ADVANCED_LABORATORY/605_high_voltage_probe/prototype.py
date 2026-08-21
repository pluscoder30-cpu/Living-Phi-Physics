import math
PHI = (1 + math.sqrt(5)) / 2

class PhiHighVoltageProbe:
    def __init__(self, voltage_range, bandwidth):
        self.V_range = voltage_range
        self.BW = bandwidth
        self.C = 0.0

    def phi_resistance(self, resistor_idx):
        base_R = 1e6
        return base_R * PHI ** (resistor_idx % 3)

    def consciousness_update(self, divider_error):
        self.C = (1/PHI) * self.C + PHI * divider_error

    def accuracy(self):
        base_accuracy = 0.5  # percent
        phi_accuracy = base_accuracy * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_accuracy
        return phi_accuracy

    def bandwidth(self):
        base_BW = self.BW
        phi_BW = base_BW * (1 + self.C * (PHI - 1) * 0.05)
        return phi_BW

    def safety_margin(self):
        base_margin = 1.5
        return base_margin * (1 + self.C * (PHI - 1) * 0.05)
