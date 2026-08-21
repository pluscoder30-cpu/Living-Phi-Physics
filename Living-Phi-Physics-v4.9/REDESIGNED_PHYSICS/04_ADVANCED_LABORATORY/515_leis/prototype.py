import math
PHI = (1 + math.sqrt(5)) / 2

class PhiLEIS:
    def __init__(self, beam_energy, incidence_angle):
        self.E_beam = beam_energy
        self.angle = incidence_angle
        self.C = 0.0

    def phi_beam_intensity(self, time):
        tau = 1e-3
        return self.E_beam * PHI ** (-time / tau)

    def consciousness_update(self, surface_sensitivity):
        self.C = (1/PHI) * self.C + PHI * surface_sensitivity

    def energy_spectrum(self, n_energies=100):
        spectrum = []
        for i in range(n_energies):
            E = self.E_beam * i / n_energies
            yield_ = self.E_beam / (2 * 3.0) * 0.01
            signal = yield_ * math.exp(-E / self.E_beam)
            self.consciousness_update(signal / self.E_beam)
            spectrum.append((E, signal * (1 + self.C * (PHI - 1) * 0.1)))
        return spectrum
