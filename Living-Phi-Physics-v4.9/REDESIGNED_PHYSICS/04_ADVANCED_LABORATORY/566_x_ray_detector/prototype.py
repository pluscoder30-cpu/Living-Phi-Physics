import math
PHI = (1 + math.sqrt(5)) / 2

class PhiXrayDetector:
    def __init__(self, pixel_size, n_pixels):
        self.pixel_size = pixel_size
        self.n_pixels = n_pixels
        self.C = 0.0

    def phi_pixel_position(self, pixel_idx):
        return pixel_idx * self.pixel_size * PHI ** (pixel_idx % 5)

    def consciousness_update(self, noise_level):
        self.C = (1/PHI) * self.C + PHI * noise_level

    def detective_quantum_efficiency(self, energy):
        base_dqe = 0.8 * math.exp(-energy / 20)
        phi_dqe = base_dqe * (1 + self.C * (PHI - 1) * 0.1)
        return min(phi_dqe, 1.0)

    def count_rate(self, incident_rate):
        base_rate = incident_rate * 0.9
        return base_rate * (1 + self.C * (PHI - 1) * 0.05)

    def energy_resolution(self, energy):
        base_res = math.sqrt(energy) * 0.1
        phi_res = base_res * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_res
        return phi_res
