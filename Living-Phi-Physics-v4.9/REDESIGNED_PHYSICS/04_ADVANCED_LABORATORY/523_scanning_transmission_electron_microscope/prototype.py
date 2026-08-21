import math
PHI = (1 + math.sqrt(5)) / 2

class PhiSTEM:
    def __init__(self, accelerating_voltage, convergence_angle):
        self.V_accel = accelerating_voltage
        self.alpha = convergence_angle
        self.C = 0.0

    def consciousness_update(self, probe_size):
        self.C = (1/PHI) * self.C + PHI * probe_size

    def probe_size(self):
        wavelength = 2.5e-12
        Cs = 1e-3 * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else 1e-3
        diffraction = 0.61 * wavelength / self.alpha
        spherical = 0.5 * Cs * self.alpha**3
        probe = math.sqrt(diffraction**2 + spherical**2)
        self.consciousness_update(probe)
        return probe

    def haadf_intensity(self, atomic_number, thickness):
        return atomic_number**1.7 * thickness * 1e-3

    def spatial_resolution(self):
        return self.probe_size()

    def elemental_mapping(self, elements, thickness, dwell_time):
        mapping = {}
        for Z in elements:
            intensity = self.haadf_intensity(Z, thickness) * dwell_time
            mapping[Z] = intensity * (1 + self.C * (PHI - 1) * 0.1)
        return mapping
