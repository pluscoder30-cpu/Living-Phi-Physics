import math
PHI = (1 + math.sqrt(5)) / 2

class PhiResearchReactor:
    def __init__(self, thermal_power, core_volume):
        self.P = thermal_power
        self.V = core_volume
        self.C = 0.0

    def phi_enrichment(self, position):
        base_enrichment = 0.20
        return base_enrichment * PHI ** (position / 10)

    def consciousness_update(self, flux_error):
        self.C = (1/PHI) * self.C + PHI * flux_error

    def neutron_flux(self):
        base_flux = self.P / self.V * 1e14
        phi_flux = base_flux * (1 + self.C * (PHI - 1) * 0.1)
        return phi_flux

    def flux_homogeneity(self):
        base_homog = 0.9
        phi_homog = base_homog * (1 + self.C * (PHI - 1) * 0.05)
        return min(phi_homog, 1.0)

    def safety_margin(self):
        base_margin = 1.5
        return base_margin * (1 + self.C * (PHI - 1) * 0.05)
