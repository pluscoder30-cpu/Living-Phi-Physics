import math
PHI = (1 + math.sqrt(5)) / 2
C_CRIT = 0.563

class PhiTEM:
    def __init__(self, accelerating_voltage, objective_aperture):
        self.V_accel = accelerating_voltage
        self.aperture = objective_aperture
        self.C = 0.0

    def consciousness_update(self, phase_error):
        self.C = (1/PHI) * self.C + PHI * phase_error

    def spherical_aberration(self):
        Cs = 1e-3
        return Cs * (1 - self.C * (PHI - 1) * 0.1) if self.C > C_CRIT else Cs

    def point_resolution(self):
        wavelength = 2.5e-12
        Cs = self.spherical_aberration()
        return 0.66 * (Cs * wavelength**3)**0.25

    def contrast_transfer(self, spatial_frequency):
        Cs = self.spherical_aberration()
        wavelength = 2.5e-12
        chi = math.pi * Cs * wavelength**3 * spatial_frequency**4 / 2
        return math.sin(chi) * (1 + self.C * (PHI - 1) * 0.01)

    def phase_contrast(self, specimen_thickness, defocus):
        wavelength = 2.5e-12
        Cs = self.spherical_aberration()
        self.consciousness_update(abs(defocus) / 1e-6)
        phi_defocus = defocus * (1 + self.C * (PHI - 1) * 0.01)
        phase = 2 * math.pi * specimen_thickness * 0.01 / wavelength
        return math.sin(phase + math.pi * Cs * wavelength * phi_defocus**2)
