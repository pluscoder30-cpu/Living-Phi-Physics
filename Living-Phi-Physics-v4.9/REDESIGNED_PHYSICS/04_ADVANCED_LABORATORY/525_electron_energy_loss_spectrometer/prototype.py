import math
PHI = (1 + math.sqrt(5)) / 2

class PhiEELS:
    def __init__(self, energy_resolution, collection_angle):
        self.delta_E = energy_resolution
        self.alpha = collection_angle
        self.C = 0.0

    def consciousness_update(self, energy_blur):
        self.C = (1/PHI) * self.C + PHI * energy_blur

    def energy_resolution(self):
        base_resolution = self.delta_E
        return base_resolution * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_resolution

    def core_loss_edge(self, binding_energy, energy_loss):
        return 1e-20 / (energy_loss - binding_energy)**2 if energy_loss > binding_energy else 0

    def plasmon_peak(self, energy_loss, plasmon_energy):
        return math.exp(-(energy_loss - plasmon_energy)**2 / (2 * self.delta_E**2))

    def spectrum(self, energy_range, n_points=500):
        spectrum = []
        for i in range(n_points):
            E = energy_range[0] + i * (energy_range[1] - energy_range[0]) / n_points
            signal = self.plasmon_peak(E, 15)
            for edge_E in [284, 532, 1840]:
                signal += self.core_loss_edge(edge_E, E) * 1000
            spectrum.append((E, signal * (1 + self.C * (PHI - 1) * 0.1)))
        return spectrum
