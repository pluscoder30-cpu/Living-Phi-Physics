import math
PHI = (1 + math.sqrt(5)) / 2

class PhiBeamline:
    def __init__(self, source_size, beam_divergence):
        self.source = source_size
        self.div = beam_divergence
        self.C = 0.0

    def phi_mirror_curvature(self, mirror_idx):
        return 1.0 * PHI ** (mirror_idx % 3)

    def consciousness_update(self, beam_position_error):
        self.C = (1/PHI) * self.C + PHI * beam_position_error

    def beam_size(self, distance):
        return self.source + self.div * distance

    def flux(self, energy, bandwidth):
        base_flux = 1e12 * energy * bandwidth
        phi_flux = base_flux * (1 + self.C * (PHI - 1) * 0.1)
        return phi_flux

    def energy_resolution(self, crystal_type):
        base_resolution = {'Si111': 1e-4, 'Si311': 3e-5, 'Ge111': 2e-4}
        res = base_resolution.get(crystal_type, 1e-4)
        return res * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else res
