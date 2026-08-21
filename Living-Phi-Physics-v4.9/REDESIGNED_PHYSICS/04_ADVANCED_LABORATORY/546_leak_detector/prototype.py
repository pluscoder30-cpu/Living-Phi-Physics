import math
PHI = (1 + math.sqrt(5)) / 2

class PhiLeakDetector:
    def __init__(self, sensitivity, background_level):
        self.sensitivity = sensitivity
        self.background = background_level
        self.C = 0.0

    def phi_filament_geometry(self, filament_idx):
        return 1e-4 * PHI ** (filament_idx % 4)

    def consciousness_update(self, noise_level):
        self.C = (1/PHI) * self.C + PHI * noise_level

    def leak_rate(self, he_signal):
        corrected_signal = he_signal - self.background
        if corrected_signal > 0:
            self.consciousness_update(self.background / corrected_signal)
        else:
            self.consciousness_update(1.0)
        base_leak = corrected_signal * self.sensitivity
        return base_leak * (1 + self.C * (PHI - 1) * 0.1)

    def minimum_detectable_leak(self):
        base_mdl = self.background * self.sensitivity
        return base_mdl * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_mdl

    def sniffing_mode(self, distance, gas_flow):
        attenuation = math.exp(-distance / 0.1)
        base_signal = gas_flow * attenuation * 1e6
        return base_signal * (1 + self.C * (PHI - 1) * 0.1)
