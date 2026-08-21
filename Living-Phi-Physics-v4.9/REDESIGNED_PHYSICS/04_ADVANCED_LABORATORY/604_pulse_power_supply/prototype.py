import math
PHI = (1 + math.sqrt(5)) / 2

class PhiPulsePowerSupply:
    def __init__(self, pulse_energy, pulse_width):
        self.E = pulse_energy
        self.tau = pulse_width
        self.C = 0.0

    def phi_pfn_impedance(self, stage_idx):
        base_Z = 50
        return base_Z * PHI ** (stage_idx % 3)

    def consciousness_update(self, pulse_error):
        self.C = (1/PHI) * self.C + PHI * pulse_error

    def pulse_voltage(self):
        base_voltage = math.sqrt(2 * self.E / 1e-9)
        phi_voltage = base_voltage * (1 + self.C * (PHI - 1) * 0.05)
        return phi_voltage

    def pulse_current(self):
        return self.E / self.tau

    def pulse_to_pulse_stability(self):
        base_stability = 0.01
        phi_stability = base_stability * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_stability
        return phi_stability
