import math
PHI = (1 + math.sqrt(5)) / 2

class PhiWhiteLightInterferometer:
    def __init__(self, source_bandwidth, scan_range):
        self.bandwidth = source_bandwidth
        self.scan_range = scan_range
        self.C = 0.0

    def phi_scan_position(self, step_idx):
        return step_idx * 1e-9 * PHI ** (step_idx % 5)

    def consciousness_update(self, coherence_error):
        self.C = (1/PHI) * self.C + PHI * coherence_error

    def axial_resolution(self):
        base_res = 0.7 / self.bandwidth * 1e-6
        phi_res = base_res * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_res
        return phi_res

    def coherence_envelope(self, path_difference):
        base_envelope = math.exp(-(path_difference / (0.7 / self.bandwidth * 1e-6))**2)
        return base_envelope * (1 + self.C * (PHI - 1) * 0.05)

    def surface_profile(self, n_points):
        profile = []
        for i in range(n_points):
            z = self.phi_scan_position(i)
            intensity = self.coherence_envelope(z - self.scan_range / 2)
            profile.append((z, intensity))
        return profile
