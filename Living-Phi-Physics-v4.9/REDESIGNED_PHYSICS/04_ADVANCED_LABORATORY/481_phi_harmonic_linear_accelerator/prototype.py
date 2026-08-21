import math
PHI = (1 + math.sqrt(5)) / 2

class PhiLinac:
    def __init__(self, n_cavities, f_base=1e9):
        self.n_cavities = n_cavities
        self.frequencies = [f_base * PHI**i for i in range(n_cavities)]
        self.coupling = 0.618
        self.C = 0.0

    def consciousness_update(self, Psi_gradient):
        self.C = (1/PHI) * self.C + PHI * Psi_gradient

    def energy_gain(self, cavity_idx, particle_velocity):
        f = self.frequencies[cavity_idx]
        sync_factor = math.sin(2 * math.pi * f * particle_velocity)
        awareness = 1 + self.coupling * (PHI - 1)
        return sync_factor * awareness

    def accelerate(self, initial_energy, n_passes=10):
        energy = initial_energy
        for _ in range(n_passes):
            for i in range(self.n_cavities):
                v = math.sqrt(2 * energy / 1.67e-27)
                gain = self.energy_gain(i, v)
                self.consciousness_update(gain * 1e-10)
                energy += abs(gain) * 1e-13
        return energy
