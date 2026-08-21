import math
PHI = (1 + math.sqrt(5)) / 2

class PhiFEL:
    def __init__(self, n_periods, K_0, electron_energy):
        self.n_periods = n_periods
        self.K_0 = K_0
        self.gamma = electron_energy / 0.511e-3
        self.C = 0.0

    def undulator_K(self, period_idx):
        return self.K_0 * PHI ** (period_idx / self.n_periods)

    def wavelength(self, period_idx):
        K = self.undulator_K(period_idx)
        return 2 * math.pi * 0.02 / (2 * self.gamma**2 / (1 + K**2/2))

    def consciousness_update(self, power_gain):
        self.C = (1/PHI) * self.C + PHI * power_gain

    def sase_gain(self, undulator_length):
        classical_gain = (undulator_length / 0.03)**(1/3)
        if self.C > 0.563:
            phi_gain = classical_gain * (1 + (self.C - 0.563) * PHI**2)
        else:
            phi_gain = classical_gain
        self.consciousness_update(phi_gain * 1e-5)
        return phi_gain

    def simulate(self, input_power=1e-3, n_segments=100):
        powers = [input_power]
        for i in range(n_segments):
            length = (i + 1) * 0.03
            gain = self.sase_gain(length)
            power = input_power * math.exp(gain)
            powers.append(power)
            self.consciousness_update(power * 1e-10)
        return powers
