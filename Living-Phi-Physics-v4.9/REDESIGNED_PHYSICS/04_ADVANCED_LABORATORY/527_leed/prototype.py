import math
PHI = (1 + math.sqrt(5)) / 2

class PhiLEED:
    def __init__(self, beam_energy, sample_temperature):
        self.E_beam = beam_energy
        self.T_sample = sample_temperature
        self.C = 0.0

    def consciousness_update(self, multiple_scattering):
        self.C = (1/PHI) * self.C + PHI * multiple_scattering

    def electron_wavelength(self):
        return 1.23e-9 / math.sqrt(self.E_beam)

    def diffraction_spots(self, surface_vectors, n_orders=5):
        spots = []
        for h in range(-n_orders, n_orders + 1):
            for k in range(-n_orders, n_orders + 1):
                if h**2 + k**2 > 0:
                    intensity = 1.0 / (h**2 + k**2 + 1)
                    self.consciousness_update(intensity * 0.1)
                    spots.append(((h, k), intensity * (1 + self.C * (PHI - 1) * 0.1)))
        return spots
