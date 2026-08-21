import math
PHI = (1 + math.sqrt(5)) / 2

class PhiShieldingGasket:
    def __init__(self, gasket_length, material_conductivity):
        self.L = gasket_length
        self.sigma = material_conductivity
        self.C = 0.0

    def phi_contact_geometry(self, contact_idx):
        base_area = 1e-6
        return base_area * PHI ** (contact_idx % 3)

    def consciousness_update(self, contact_resistance):
        self.C = (1/PHI) * self.C + PHI * contact_resistance

    def contact_resistance(self, compression_force):
        base_R = 1e-3 / (compression_force * self.sigma)
        phi_R = base_R * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_R
        return phi_R

    def shielding_effectiveness(self, frequency):
        R = self.contact_resistance(10)
        base_SE = -20 * math.log10(R / 50)
        phi_SE = base_SE * (1 + self.C * (PHI - 1) * 0.1)
        return phi_SE

    def compression_set(self):
        base_set = 0.1
        return base_set * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_set
