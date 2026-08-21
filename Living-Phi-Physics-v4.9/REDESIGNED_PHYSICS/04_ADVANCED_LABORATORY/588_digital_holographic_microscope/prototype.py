import math
PHI = (1 + math.sqrt(5)) / 2

class PhiDigitalHolographicMicroscope:
    def __init__(self, numerical_aperture, wavelength):
        self.NA = numerical_aperture
        self.wavelength = wavelength
        self.C = 0.0

    def phi_sampling(self, pixel_idx):
        base_sampling = self.wavelength / (2 * self.NA)
        return base_sampling * PHI ** (pixel_idx % 4)

    def consciousness_update(self, phase_error):
        self.C = (1/PHI) * self.C + PHI * phase_error

    def lateral_resolution(self):
        base_res = 0.61 * self.wavelength / self.NA
        phi_res = base_res * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_res
        return phi_res

    def axial_resolution(self):
        base_res = 2 * self.wavelength / self.NA**2
        phi_res = base_res * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_res
        return phi_res

    def phase_accuracy(self):
        base_accuracy = 0.01
        return base_accuracy * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_accuracy
