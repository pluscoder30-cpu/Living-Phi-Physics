import math
PHI = (1 + math.sqrt(5)) / 2

class PhiGasLaser:
    def __init__(self, gas_type, tube_length):
        self.gas = gas_type
        self.L = tube_length
        self.C = 0.0

    def phi_electrode_spacing(self, segment_idx):
        return self.L * PHI ** (segment_idx % 5) / 10

    def consciousness_update(self, discharge_stability):
        self.C = (1/PHI) * self.C + PHI * discharge_stability

    def gain(self, pressure, discharge_current):
        base_gain = pressure * discharge_current * 1e-3
        return base_gain * (1 + self.C * (PHI - 1) * 0.1)

    def output_power(self, pressure, discharge_current, mirror_loss):
        g = self.gain(pressure, discharge_current)
        return max(0, g - mirror_loss)

    def wavelength_stability(self, temperature):
        base_drift = 1e-9
        return base_drift * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_drift
