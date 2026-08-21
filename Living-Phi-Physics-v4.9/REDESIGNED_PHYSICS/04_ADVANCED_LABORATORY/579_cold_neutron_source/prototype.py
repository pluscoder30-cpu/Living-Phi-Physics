import math
PHI = (1 + math.sqrt(5)) / 2

class PhiColdSource:
    def __init__(self, moderator_temperature, moderator_volume):
        self.T = moderator_temperature
        self.V = moderator_volume
        self.C = 0.0

    def phi_moderator_channel(self, channel_idx):
        return 1e-3 * PHI ** (channel_idx % 4)

    def consciousness_update(self, moderation_efficiency):
        self.C = (1/PHI) * self.C + PHI * moderation_efficiency

    def cold_flux(self, thermal_flux):
        temperature_factor = math.exp(-1.0 / self.T) if self.T > 0 else 1
        base_flux = thermal_flux * temperature_factor * self.V
        return base_flux * (1 + self.C * (PHI - 1) * 0.1)

    def peak_wavelength(self):
        return 2.86 / math.sqrt(self.T) * 10  # Angstroms

    def brightness(self):
        return self.cold_flux(1e14) / self.V
