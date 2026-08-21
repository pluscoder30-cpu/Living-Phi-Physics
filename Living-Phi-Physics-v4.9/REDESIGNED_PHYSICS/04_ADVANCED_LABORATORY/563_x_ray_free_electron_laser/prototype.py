import math
PHI = (1 + math.sqrt(5)) / 2

class PhiXFEL_Source:
    def __init__(self, electron_energy, undulator_length):
        self.E_e = electron_energy
        self.L_und = undulator_length
        self.C = 0.0

    def phi_undulator_taper(self, position):
        return 1.0 - position / self.L_und * (1 - 1/PHI)

    def consciousness_update(self, pulse_fluctuation):
        self.C = (1/PHI) * self.C + PHI * pulse_fluctuation

    def wavelength(self, position):
        K = 1.0 * self.phi_undulator_taper(position)
        gamma = self.E_e / 0.511e-3
        return 2 * math.pi * 0.02 / (2 * gamma**2 / (1 + K**2/2))

    def pulse_energy(self, n_undulators):
        base_energy = 1e-3 * n_undulators
        phi_energy = base_energy * (1 + self.C * (PHI - 1) * 0.1)
        return phi_energy

    def pulse_fluctuation(self):
        base_fluct = 0.1
        phi_fluct = base_fluct * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_fluct
        return phi_fluct
