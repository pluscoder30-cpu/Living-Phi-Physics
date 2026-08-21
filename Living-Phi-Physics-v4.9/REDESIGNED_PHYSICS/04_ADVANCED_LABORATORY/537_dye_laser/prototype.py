import math
PHI = (1 + math.sqrt(5)) / 2

class PhiDyeLaser:
    def __init__(self, dye_concentration, flow_rate):
        self.conc = dye_concentration
        self.Q = flow_rate
        self.C = 0.0

    def phi_flow_channel(self, position):
        return 1e-3 * PHI ** (position % 5)

    def consciousness_update(self, dye_degradation):
        self.C = (1/PHI) * self.C + PHI * dye_degradation

    def gain(self, wavelength, pump_power):
        center_wl = 590e-9
        bandwidth = 50e-9
        spectral_overlap = math.exp(-(wavelength - center_wl)**2 / (2 * bandwidth**2))
        base_gain = self.conc * pump_power * spectral_overlap * 1e-3
        return base_gain * (1 + self.C * (PHI - 1) * 0.1)

    def dye_lifetime(self, pump_power):
        base_lifetime = 1e6 / pump_power
        return base_lifetime * (1 + self.C * (PHI - 1))

    def tunability(self, wavelength_range):
        tuning = []
        for wl in range(wavelength_range[0], wavelength_range[1], 10):
            g = self.gain(wl * 1e-9, 1.0)
            tuning.append((wl, g))
        return tuning
