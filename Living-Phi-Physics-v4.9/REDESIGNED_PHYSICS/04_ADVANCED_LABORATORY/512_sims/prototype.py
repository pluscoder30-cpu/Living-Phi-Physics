import math
PHI = (1 + math.sqrt(5)) / 2

class PhiSIMS:
    def __init__(self, beam_energy, primary_ion):
        self.E_beam = beam_energy
        self.ion = primary_ion
        self.C = 0.0

    def phi_raster(self, point_idx, n_points):
        theta = 2 * math.pi * point_idx / n_points * PHI
        r = math.sqrt(point_idx / n_points)
        return r * math.cos(theta), r * math.sin(theta)

    def consciousness_update(self, topography_variation):
        self.C = (1/PHI) * self.C + PHI * topography_variation

    def depth_profile(self, n_layers, binding_energy, ionization_prob):
        profile = []
        for layer in range(n_layers):
            x, y = self.phi_raster(layer, n_layers)
            yield_ = self.E_beam / (2 * binding_energy) * 0.1
            signal = ionization_prob * yield_ * 1e6
            self.consciousness_update(abs(signal - 1e6) / 1e6)
            phi_signal = signal * (1 + self.C * (PHI - 1) * 0.1)
            profile.append((layer, phi_signal))
        return profile
