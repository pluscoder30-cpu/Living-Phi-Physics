import math
PHI = (1 + math.sqrt(5)) / 2

class PhiQueriedInterferometer:
    def __init__(self, arm_length, beam_power):
        self.L = arm_length
        self.P = beam_power
        self.C = 0.0

    def phi_coupling_coefficient(self, cavity_idx):
        base_coupling = 0.5
        return base_coupling * PHI ** (cavity_idx % 2)

    def consciousness_update(self, quantum_noise):
        self.C = (1/PHI) * self.C + PHI * quantum_noise

    def shot_noise(self, detection_efficiency):
        base_noise = 1 / math.sqrt(self.P * detection_efficiency)
        return base_noise * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_noise

    def radiation_pressure_noise(self):
        base_noise = math.sqrt(self.P) / self.L
        return base_noise * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_noise

    def standard_quantum_limit(self, detection_efficiency):
        shot = self.shot_noise(detection_efficiency)
        rp = self.radiation_pressure_noise()
        return shot * rp
