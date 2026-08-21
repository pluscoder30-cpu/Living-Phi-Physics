import math
PHI = (1 + math.sqrt(5)) / 2

class PhiSEM:
    def __init__(self, accelerating_voltage, working_distance):
        self.V_accel = accelerating_voltage
        self.WD = working_distance
        self.C = 0.0
        self.lens_spacings = [1.0 * PHI**i for i in range(5)]

    def consciousness_update(self, aberration):
        self.C = (1/PHI) * self.C + PHI * aberration

    def beam_diameter(self, aperture_angle):
        spherical = 0.5 * 1e-3 * aperture_angle**3
        chromatic = 1e-3 * aperture_angle * 0.01
        diffraction = 1.22 * 2.5e-12 / aperture_angle
        base_diameter = spherical + chromatic + diffraction
        phi_correction = 1 - self.C * (PHI - 1) * 0.1 if self.C > 0 else 1
        return base_diameter * phi_correction

    def resolution(self, aperture_angle):
        return self.beam_diameter(aperture_angle)

    def scan_pattern(self, n_pixels, scan_type='raster'):
        pattern = []
        if scan_type == 'phi_spiral':
            for i in range(n_pixels):
                theta = 2 * math.pi * i / PHI
                r = math.sqrt(i / n_pixels)
                pattern.append((r * math.cos(theta) + 0.5, r * math.sin(theta) + 0.5))
        else:
            side = int(math.sqrt(n_pixels))
            for i in range(side):
                for j in range(side):
                    pattern.append((i / side, j / side))
        return pattern
