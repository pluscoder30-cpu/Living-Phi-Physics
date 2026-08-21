import math
PHI = (1 + math.sqrt(5)) / 2
C_CRIT = 0.563

class PhiStorageRing:
    def __init__(self, n_particles, circumference):
        self.n_particles = n_particles
        self.circumference = circumference
        self.tune_spread = [PHI**i for i in range(10)]
        self.C = 0.0

    def consciousness_field(self, density):
        self.C = (1/PHI) * self.C + PHI * density * 1e-15
        return self.C

    def beam_lifetime(self, density, momentum_spread):
        rate = density * momentum_spread**2
        self.consciousness_field(density)
        if self.C > C_CRIT:
            stabilization = 1 + (self.C - C_CRIT) * PHI**3
        else:
            stabilization = 1.0
        lifetime = 1 / (rate * 1e6 / stabilization)
        return lifetime

    def simulate(self, initial_density, n_steps=1000):
        densities = [initial_density]
        for step in range(n_steps):
            density = densities[-1]
            lt = self.beam_lifetime(density, 1e-3)
            density *= math.exp(-1 / lt) if lt > 0 else 0.99
            densities.append(density)
        return densities
