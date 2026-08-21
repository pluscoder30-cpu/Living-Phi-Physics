import math
PHI = (1 + math.sqrt(5)) / 2

class PhiXRD:
    def __init__(self, xray_wavelength, goniometer_radius):
        self.wavelength = xray_wavelength
        self.R = goniometer_radius
        self.C = 0.0

    def phi_goniometer_axis(self, axis_idx):
        return self.R * PHI ** (axis_idx % 3)

    def consciousness_update(self, angular_error):
        self.C = (1/PHI) * self.C + PHI * angular_error

    def bragg_angle(self, d_spacing):
        return math.asin(self.wavelength / (2 * d_spacing))

    def peak_width(self, crystallite_size):
        base_width = 0.9 * self.wavelength / (crystallite_size * math.cos(0.2))
        phi_width = base_width * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_width
        return phi_width

    def resolution(self, two_theta):
        base_res = 0.01
        phi_res = base_res * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_res
        return phi_res
