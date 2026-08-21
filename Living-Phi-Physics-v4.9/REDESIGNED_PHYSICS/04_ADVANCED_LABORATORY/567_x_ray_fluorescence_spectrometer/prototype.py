import math
PHI = (1 + math.sqrt(5)) / 2

class PhiXRF:
    def __init__(self, excitation_energy, detector_type):
        self.E_exc = excitation_energy
        self.detector = detector_type
        self.C = 0.0

    def phi_excitation_angle(self):
        return math.radians(45) / PHI

    def consciousness_update(self, background_level):
        self.C = (1/PHI) * self.C + PHI * background_level

    def fluorescence_yield(self, element_z):
        base_yield = element_z**4 * 1e-8
        return base_yield * (1 + self.C * (PHI - 1) * 0.1)

    def sensitivity(self, element_z, matrix_effect):
        base_sensitivity = self.fluorescence_yield(element_z) / matrix_effect
        return base_sensitivity * (1 + self.C * (PHI - 1) * 0.1)

    def detection_limit(self, element_z, matrix_effect, counting_time):
        signal = self.sensitivity(element_z, matrix_effect)
        background = signal * 0.01
        return background / math.sqrt(counting_time) * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else background / math.sqrt(counting_time)
