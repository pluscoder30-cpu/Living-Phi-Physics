import math
PHI = (1 + math.sqrt(5)) / 2

class PhiNTD:
    def __init__(self, neutron_flux, irradiation_time):
        self.flux = neutron_flux
        self.time = irradiation_time
        self.C = 0.0

    def phi_sample_position(self, sample_idx):
        theta = 2 * math.pi * sample_idx / PHI
        r = math.sqrt(sample_idx)
        return r * math.cos(theta), r * math.sin(theta)

    def consciousness_update(self, uniformity_error):
        self.C = (1/PHI) * self.C + PHI * uniformity_error

    def dopant_concentration(self):
        base_conc = self.flux * self.time * 1e-24
        return base_conc * (1 + self.C * (PHI - 1) * 0.05)

    def resistivity(self, dopant_concentration):
        return 1.0 / (dopant_concentration * 1.6e-19 * 1500)

    def uniformity(self):
        base_error = 0.05
        phi_error = base_error * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_error
        return phi_error
