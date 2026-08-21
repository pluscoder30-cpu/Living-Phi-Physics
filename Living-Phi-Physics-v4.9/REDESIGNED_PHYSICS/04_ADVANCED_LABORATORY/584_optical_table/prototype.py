import math
PHI = (1 + math.sqrt(5)) / 2

class PhiOpticalTable:
    def __init__(self, table_length, table_width):
        self.L = table_length
        self.W = table_width
        self.C = 0.0

    def phi_honeycomb_cell(self, cell_idx):
        base_size = 1e-2
        return base_size * PHI ** (cell_idx % 3)

    def consciousness_update(self, vibration_amplitude):
        self.C = (1/PHI) * self.C + PHI * vibration_amplitude

    def vibration_transfer_function(self, frequency):
        base_tf = 1 / (1 + (frequency / 10)**2)
        phi_tf = base_tf * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_tf
        return phi_tf

    def resonance_frequency(self):
        base_freq = 1.5
        return base_freq * (1 + self.C * (PHI - 1) * 0.05)

    def damping_ratio(self):
        base_damping = 0.1
        return base_damping * (1 + self.C * (PHI - 1) * 0.1)
