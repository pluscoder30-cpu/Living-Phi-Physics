import math
PHI = (1 + math.sqrt(5)) / 2

class PhiBevatron:
    def __init__(self, circumference, max_energy):
        self.circumference = circumference
        self.max_energy = max_energy
        self.n_sectors = 8
        self.gradients = [1.0 * PHI**(i/self.n_sectors)
                         for i in range(self.n_sectors)]
        self.C = 0.0

    def consciousness_update(self, production_rate):
        self.C = (1/PHI) * self.C + PHI * production_rate

    def antiproton_production(self, beam_energy, target_thickness):
        classical_yield = beam_energy * target_thickness * 1e-28
        self.consciousness_update(classical_yield * 1e10)
        if self.C > 0.563:
            phi_yield = classical_yield * (1 + (self.C - 0.563) * PHI**2)
        else:
            phi_yield = classical_yield
        return phi_yield

    def energy_ramp(self, n_turns, initial_energy):
        energy = initial_energy
        energies = []
        for turn in range(n_turns):
            sector = turn % self.n_sectors
            grad = self.gradients[sector]
            energy *= (1 + grad * 1e-6)
            energies.append(min(energy, self.max_energy))
        return energies
