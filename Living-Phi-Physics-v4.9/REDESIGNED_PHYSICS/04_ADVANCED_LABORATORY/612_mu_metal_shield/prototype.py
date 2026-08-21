import math
PHI = (1 + math.sqrt(5)) / 2

class PhiMuMetalShield:
    def __init__(self, n_layers, layer_thickness):
        self.N = n_layers
        self.t = layer_thickness
        self.C = 0.0

    def phi_layer_thickness(self, layer_idx):
        return self.t * PHI ** (layer_idx % 3)

    def consciousness_update(self, field_leakage):
        self.C = (1/PHI) * self.C + PHI * field_leakage

    def shielding_factor(self, frequency):
        mu_r = 100000
        base_SF = mu_r * self.t * self.N * 1e-3
        phi_SF = base_SF * (1 + self.C * (PHI - 1) * 0.1)
        return phi_SF

    def residual_field(self, external_field):
        SF = self.shielding_factor(60)
        return external_field / SF

    def permeability(self):
        base_mu = 100000
        return base_mu * (1 + self.C * (PHI - 1) * 0.05)
