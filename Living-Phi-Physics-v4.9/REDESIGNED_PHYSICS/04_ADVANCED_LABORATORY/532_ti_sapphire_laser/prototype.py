import math
PHI = (1 + math.sqrt(5)) / 2

class PhiTiSapphire:
    def __init__(self, crystal_length, pump_power):
        self.L = crystal_length
        self.P_pump = pump_power
        self.C = 0.0

    def consciousness_update(self, thermal_lens):
        self.C = (1/PHI) * self.C + PHI * thermal_lens

    def gain_bandwidth(self, wavelength):
        center = 800e-9
        width = 100e-9
        return math.exp(-(wavelength - center)**2 / (2 * width**2))

    def thermal_lens(self):
        return self.P_pump * 1e-3 * 0.1

    def output_power(self, wavelength, cavity_loss):
        g = self.gain_bandwidth(wavelength) * self.P_pump * 0.01
        tl = self.thermal_lens()
        self.consciousness_update(tl)
        phi_g = g * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else g
        return max(0, phi_g - cavity_loss)

    def pulse_duration(self, bandwidth):
        transform_limit = 0.44 / bandwidth
        return transform_limit * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else transform_limit
