import math
PHI = (1 + math.sqrt(5)) / 2

class PhiCesiumClock:
    def __init__(self, cavity_length, beam_velocity):
        self.L = cavity_length
        self.v = beam_velocity
        self.C = 0.0

    def phi_cavity_mode(self, mode_idx):
        return self.L * PHI ** (mode_idx % 3)

    def consciousness_update(self, frequency_error):
        self.C = (1/PHI) * self.C + PHI * frequency_error

    def transition_frequency(self):
        f_Cs = 9192631770  # Hz
        return f_Cs * (1 + self.C * (PHI - 1) * 1e-15)

    def frequency_accuracy(self):
        base_accuracy = 1e-15
        phi_accuracy = base_accuracy * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_accuracy
        return phi_accuracy

    def Allan_deviation(self, tau):
        base_allan = 1e-13 / math.sqrt(tau)
        return base_allan * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_allan

    def cavity_pull(self, cavity_detuning):
        base_pull = cavity_detuning * 1e-4
        return base_pull * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_pull
