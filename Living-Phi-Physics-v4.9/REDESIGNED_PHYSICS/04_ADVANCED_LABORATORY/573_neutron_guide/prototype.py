import math
PHI = (1 + math.sqrt(5)) / 2

class PhiNeutronGuide:
    def __init__(self, guide_length, cross_section):
        self.L = guide_length
        self.A = cross_section
        self.C = 0.0

    def phi_guide_width(self, position):
        return math.sqrt(self.A) * PHI ** (position / self.L)

    def consciousness_update(self, transmission_loss):
        self.C = (1/PHI) * self.C + PHI * transmission_loss

    def transmission(self, neutron_wavelength):
        base_trans = 0.9 * math.exp(-self.L / 100)
        phi_trans = base_trans * (1 + self.C * (PHI - 1) * 0.1)
        return min(phi_trans, 1.0)

    def critical_angle(self, wavelength):
        base_angle = 0.1 * wavelength
        return base_angle * (1 + self.C * (PHI - 1) * 0.05)

    def flux_at_sample(self, source_flux):
        return source_flux * self.transmission(1.8) * self.A
