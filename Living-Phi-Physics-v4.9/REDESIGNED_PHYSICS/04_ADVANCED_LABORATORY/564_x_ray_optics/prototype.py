import math
PHI = (1 + math.sqrt(5)) / 2

class PhiXrayOptics:
    def __init__(self, focal_length, aperture):
        self.f = focal_length
        self.D = aperture
        self.C = 0.0

    def phi_surface_profile(self, position):
        return 1e-9 * PHI ** (abs(position) / (self.D / 2))

    def consciousness_update(self, figure_error):
        self.C = (1/PHI) * self.C + PHI * figure_error

    def spot_size(self, source_size, distance):
        base_spot = source_size * self.f / distance
        phi_spot = base_spot * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_spot
        return phi_spot

    def transmission(self, energy):
        base_trans = 0.7
        return base_trans * (1 + self.C * (PHI - 1) * 0.05)

    def numerical_aperture(self):
        return self.D / (2 * self.f) * (1 + self.C * (PHI - 1) * 0.01)
