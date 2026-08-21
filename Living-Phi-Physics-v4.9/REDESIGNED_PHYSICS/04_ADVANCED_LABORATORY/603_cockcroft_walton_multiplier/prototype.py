import math
PHI = (1 + math.sqrt(5)) / 2

class PhiCockcroftWalton:
    def __init__(self, n_stages, input_voltage):
        self.N = n_stages
        self.V_in = input_voltage
        self.C = 0.0

    def phi_capacitance(self, stage_idx):
        base_C = 1e-9
        return base_C * PHI ** (stage_idx % 3)

    def consciousness_update(self, ripple_voltage):
        self.C = (1/PHI) * self.C + PHI * ripple_voltage

    def output_voltage(self, load_current):
        base_voltage = 2 * self.N * self.V_in
        drop = load_current / (60 * 1e-9) * (self.N**3 + self.N**2) / 2
        phi_drop = drop * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else drop
        return base_voltage - phi_drop

    def ripple_voltage(self, load_current, frequency):
        base_ripple = load_current / (frequency * 1e-9) * self.N * (self.N + 1) / 4
        phi_ripple = base_ripple * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_ripple
        return phi_ripple

    def voltage_regulation(self, load_current):
        base_reg = self.N**2 / (frequency * 1e-9 * 1e-9)
        return base_reg * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_reg
