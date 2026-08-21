import math
PHI = (1 + math.sqrt(5)) / 2

class PhiProtonSynchrotron:
    def __init__(self, circumference, max_energy):
        self.circumference = circumference
        self.max_energy = max_energy
        self.harmonics = [h0 * PHI**i for i, h0 in enumerate([1, 2, 3])]
        self.C = 0.0

    def revolution_frequency(self, energy):
        gamma = energy / 0.938e9
        v = 3e8 * math.sqrt(1 - 1/gamma**2)
        return v / self.circumference

    def space_charge_tune_shift(self, current, emittance):
        return current / (emittance * 1e6)

    def consciousness_update(self, tune_shift):
        self.C = (1/PHI) * self.C + PHI * tune_shift

    def accelerate(self, initial_energy, beam_current, n_turns=1000):
        energy = initial_energy
        energies = []
        for turn in range(n_turns):
            f_rev = self.revolution_frequency(energy)
            for h in self.harmonics:
                rf_phase = 2 * math.pi * h * f_rev
                energy += 1e6 * math.sin(rf_phase)
            tune_shift = self.space_charge_tune_shift(beam_current, 1e-6)
            self.consciousness_update(tune_shift)
            if self.C > 0.563:
                energy *= 1 - (self.C - 0.563) * 0.1
            energies.append(energy)
            if energy >= self.max_energy:
                break
        return energies
