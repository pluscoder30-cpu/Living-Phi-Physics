import math
PHI = (1 + math.sqrt(5)) / 2

class PhiSolidStateLaser:
    def __init__(self, crystal_length, dopant_concentration):
        self.L = crystal_length
        self.N0 = dopant_concentration
        self.C = 0.0

    def phi_dopant_profile(self, position):
        return self.N0 * PHI ** (position / self.L)

    def consciousness_update(self, thermal_distortion):
        self.C = (1/PHI) * self.C + PHI * thermal_distortion

    def gain(self, position, pump_power):
        N = self.phi_dopant_profile(position)
        return N * pump_power * 1e-6 * (1 - self.C * (PHI - 1) * 0.05) if self.C > 0 else N * pump_power * 1e-6

    def thermal_lens(self, pump_power):
        base_lens = pump_power * 1e-3
        return base_lens * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_lens

    def output_energy(self, pump_energy, extraction_efficiency):
        gain = self.gain(self.L / 2, pump_energy)
        return gain * extraction_efficiency * (1 + self.C * (PHI - 1) * 0.01)
