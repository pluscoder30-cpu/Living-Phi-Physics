import math
PHI = (1 + math.sqrt(5)) / 2

class PhiNeutronDetector:
    def __init__(self, detector_type, active_area):
        self.type = detector_type
        self.A = active_area
        self.C = 0.0

    def phi_detector_element(self, element_idx):
        return self.A * PHI ** (element_idx % 5) / 10

    def consciousness_update(self, efficiency_error):
        self.C = (1/PHI) * self.C + PHI * efficiency_error

    def efficiency(self, neutron_wavelength):
        absorption = {'He3': 5.3e3, 'B10': 3.8e3, 'Gd': 49e3}
        sigma = absorption.get(self.type, 5e3)
        base_eff = 1 - math.exp(-sigma * neutron_wavelength / 1e10)
        phi_eff = base_eff * (1 + self.C * (PHI - 1) * 0.1)
        return min(phi_eff, 1.0)

    def count_rate(self, neutron_flux):
        return neutron_flux * self.A * self.efficiency(1.8)

    def spatial_resolution(self):
        base_res = 1e-3
        return base_res * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_res
