import math
PHI = (1 + math.sqrt(5)) / 2

class PhiTokamakDiagnostics:
    def __init__(self, plasma_radius, magnetic_field):
        self.a = plasma_radius
        self.B = magnetic_field
        self.C = 0.0

    def phi_sightline_angle(self, sightline_idx):
        base_angle = 15  # degrees
        return base_angle * PHI ** (sightline_idx % 4)

    def consciousness_update(self, measurement_error):
        self.C = (1/PHI) * self.C + PHI * measurement_error

    def thomson_scattering(self, electron_density, electron_temp):
        base_signal = electron_density * electron_temp
        return base_signal * (1 + self.C * (PHI - 1) * 0.1)

    def ece_frequency(self, major_radius, B_field):
        return 28e9 * B_field * (1 - 0.01 * (major_radius - 1.0))

    def spatial_resolution(self):
        base_res = self.a / 20
        phi_res = base_res * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_res
        return phi_res
