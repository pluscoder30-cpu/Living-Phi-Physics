import math
PHI = (1 + math.sqrt(5)) / 2

class PhiNeutronImaging:
    def __init__(self, source_size, detector_resolution):
        self.source = source_size
        self.det_res = detector_resolution
        self.C = 0.0

    def phi_collimator_aperture(self, position):
        return 1e-3 * PHI ** (position % 4)

    def consciousness_update(self, contrast_error):
        self.C = (1/PHI) * self.C + PHI * contrast_error

    def spatial_resolution(self, L/D_ratio):
        base_res = self.source / L/D_ratio
        phi_res = base_res * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_res
        return phi_res

    def contrast(self, material1_cross_section, material2_cross_section, thickness):
        base_contrast = abs(material1_cross_section - material2_cross_section) * thickness
        return base_contrast * (1 + self.C * (PHI - 1) * 0.1)

    def neutron_dose(self, flux, exposure_time):
        return flux * exposure_time * 1e-12
