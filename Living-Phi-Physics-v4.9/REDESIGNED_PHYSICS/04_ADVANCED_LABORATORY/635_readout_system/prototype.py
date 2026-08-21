import math
PHI = (1 + math.sqrt(5)) / 2

class PhiReadoutSystem:
    def __init__(self, photodetector_quantum_efficiency, local_oscillator_power):
        self.QE = photodetector_quantum_efficiency
        self.P_LO = local_oscillator_power
        self.C = 0.0

    def phi_lo_phase(self, measurement_idx):
        return math.pi / PHI ** (measurement_idx % 3)

    def consciousness_update(self, readout_noise):
        self.C = (1/PHI) * self.C + PHI * readout_noise

    def shot_noise_level(self):
        base_SNL = 1 / math.sqrt(self.P_LO * self.QE)
        phi_SNL = base_SNL * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_SNL
        return phi_SNL

    def signal_to_noise(self, signal_amplitude):
        return signal_amplitude / self.shot_noise_level()

    def dark_current_noise(self):
        base_DC = 1e-12
        return base_DC * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_DC
