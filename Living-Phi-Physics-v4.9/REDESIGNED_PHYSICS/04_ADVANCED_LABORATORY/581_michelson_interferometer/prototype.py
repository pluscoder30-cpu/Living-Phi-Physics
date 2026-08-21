import math
PHI = (1 + math.sqrt(5)) / 2

class PhiMichelsonInterferometer:
    def __init__(self, wavelength, coherence_length):
        self.wavelength = wavelength
        self.Lc = coherence_length
        self.C = 0.0

    def phi_mirror_adjustment(self, adjustment_idx):
        return 1e-9 * PHI ** (adjustment_idx % 3)

    def consciousness_update(self, alignment_error):
        self.C = (1/PHI) * self.C + PHI * alignment_error

    def fringe_visibility(self, path_difference):
        base_vis = math.exp(-path_difference / self.Lc)
        phi_vis = base_vis * (1 + self.C * (PHI - 1) * 0.1)
        return min(phi_vis, 1.0)

    def phase_sensitivity(self):
        base_sens = self.wavelength / 1000
        return base_sens * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_sens

    def fringe_pattern(self, path_differences):
        pattern = []
        for d in path_differences:
            vis = self.fringe_visibility(d)
            intensity = 0.5 * (1 + vis * math.cos(2 * math.pi * d / self.wavelength))
            pattern.append(intensity)
        return pattern
