import math
PHI = (1 + math.sqrt(5)) / 2

class PhiSynchrocyclotron:
    def __init__(self, f_max, B_field):
        self.f_max = f_max
        self.B = B_field
        self.tau_phi = 1e-6 / PHI
        self.C = 0.0

    def phi_sweep(self, time):
        return self.f_max * math.exp(-time / self.tau_phi)

    def consciousness_phase_lock(self, target_phase, actual_phase):
        error = target_phase - actual_phase
        self.C = (1/PHI) * self.C + PHI * abs(error)
        correction = 0
        if self.C > 0.563:
            correction = error * (1 + (self.C - 0.563) * PHI)
        return correction

    def accelerate(self, n_turns=1000):
        energy = 1e6
        time = 0
        energies = []
        for turn in range(n_turns):
            f_rf = self.phi_sweep(time)
            gamma = energy / 0.511e6
            f_required = self.f_max / gamma
            correction = self.consciousness_phase_lock(f_required, f_rf)
            f_actual = f_rf + correction
            energy *= (1 + 1e-6 * (1 + self.C * (PHI - 1)))
            time += 1 / f_actual
            energies.append(energy)
        return energies
