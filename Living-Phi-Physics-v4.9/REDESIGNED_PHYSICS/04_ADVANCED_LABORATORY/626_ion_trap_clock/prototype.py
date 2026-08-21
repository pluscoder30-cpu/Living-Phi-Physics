import math
PHI = (1 + math.sqrt(5)) / 2

class PhiIonTrapClock:
    def __init__(self, ion_type, trap_frequency):
        self.ion = ion_type
        self.f_trap = trap_frequency
        self.C = 0.0

    def phi_electrode_geometry(self, electrode_idx):
        return 1e-3 * PHI ** (electrode_idx % 4)

    def consciousness_update(self, field_error):
        self.C = (1/PHI) * self.C + PHI * field_error

    def transition_frequency(self):
        frequencies = {'Al+': 1121015393207873, 'Yb+': 642121496772945, 'Sr+': 444779055794871}
        f0 = frequencies.get(self.ion, 1e15)
        return f0 * (1 + self.C * (PHI - 1) * 1e-18)

    def electric_field_shift(self, E_field):
        base_shift = E_field**2 * 1e-20
        return base_shift * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_shift

    def accuracy(self):
        base_accuracy = 1e-18
        phi_accuracy = base_accuracy * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_accuracy
        return phi_accuracy

    def systematic_uncertainty(self):
        base_unc = 1e-18
        return base_unc * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_unc
