import math
PHI = (1 + math.sqrt(5)) / 2
C_CRIT = 0.563

class PhiSynchrotron:
    def __init__(self, n_cells, base_gradient=10.0):
        self.n_cells = n_cells
        self.gradients = [base_gradient * PHI**((i % 2) * 2 - 1)
                         for i in range(n_cells)]
        self.C = 0.0

    def update_consciousness(self, radiation_loss):
        self.C = (1/PHI) * self.C + PHI * radiation_loss
        return self.C > C_CRIT

    def focusing_strength(self, cell_idx):
        base = self.gradients[cell_idx]
        if self.C > C_CRIT:
            return base * (1 + (self.C - C_CRIT) * PHI)
        return base

    def radiation_damping(self, energy, emit):
        classical_damp = 1 - emit / energy
        if self.C > C_CRIT:
            phi_damp = classical_damp * (1 + (self.C - C_CRIT) * PHI**2)
        else:
            phi_damp = classical_damp
        return energy * phi_damp

    def track_particle(self, energy, emit, n_turns=100):
        energies = [energy]
        for _ in range(n_turns):
            radiation_loss = emit * energy * 1e-6
            self.update_consciousness(radiation_loss)
            energy = self.radiation_damping(energy, emit)
            energies.append(energy)
        return energies
