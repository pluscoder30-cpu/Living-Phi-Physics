import math
PHI = (1 + math.sqrt(5)) / 2

class PhiPowerMeter:
    def __init__(self, frequency_range, dynamic_range):
        self.f_range = frequency_range
        self.DR = dynamic_range
        self.C = 0.0

    def phi_sensor_element(self, element_idx):
        return 1e-4 * PHI ** (element_idx % 4)

    def consciousness_update(self, calibration_drift):
        self.C = (1/PHI) * self.C + PHI * calibration_drift

    def accuracy(self):
        base_accuracy = 0.5  # dB
        phi_accuracy = base_accuracy * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_accuracy
        return phi_accuracy

    def noise_equivalent_power(self):
        base_NEP = 1e-12
        phi_NEP = base_NEP * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_NEP
        return phi_NEP

    def linearity(self):
        base_linearity = 0.1  # dB
        return base_linearity * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_linearity
