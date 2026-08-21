import math
PHI = (1 + math.sqrt(5)) / 2

class PhiElectronDiffraction:
    def __init__(self, accelerating_voltage, camera_length):
        self.V_accel = accelerating_voltage
        self.L = camera_length
        self.C = 0.0

    def consciousness_update(self, dynamic_error):
        self.C = (1/PHI) * self.C + PHI * dynamic_error

    def d_spacing(self, reflection_index, lattice_parameter):
        h, k, l = reflection_index
        return lattice_parameter / math.sqrt(h**2 + k**2 + l**2)

    def diffraction_pattern(self, lattice_parameter, n_reflections=20):
        pattern = []
        for h in range(n_reflections):
            for k in range(n_reflections):
                for l in range(n_reflections):
                    if h**2 + k**2 + l**2 > 0 and h**2 + k**2 + l**2 < 50:
                        d = self.d_spacing((h, k, l), lattice_parameter)
                        intensity = 1.0 / d**2
                        self.consciousness_update(abs(intensity - 1.0))
                        pattern.append(((h, k, l), d, intensity * (1 + self.C * (PHI - 1) * 0.1)))
        return pattern
