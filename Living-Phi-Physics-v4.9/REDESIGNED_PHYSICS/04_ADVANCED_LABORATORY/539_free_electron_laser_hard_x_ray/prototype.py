import math
PHI = (1 + math.sqrt(5)) / 2

class PhiXFEL:
    def __init__(self, n_undulators, K_0, electron_energy):
        self.N = n_undulators
        self.K_0 = K_0
        self.gamma = electron_energy / 0.511e-3
        self.C = 0.0

    def phi_taper(self, undulator_idx):
        return self.K_0 * PHI ** (-undulator_idx / self.N)

    def consciousness_update(self, sase_noise):
        self.C = (1/PHI) * self.C + PHI * sase_noise

    def wavelength(self, undulator_idx):
        K = self.phi_taper(undulator_idx)
        return 2 * math.pi * 0.02 / (2 * self.gamma**2 / (1 + K**2/2))

    def gain_length(self, undulator_idx):
        K = self.phi_taper(undulator_idx)
        base_gain = 0.03 / (K**0.5)
        noise_factor = 1 + 0.1 * math.sin(undulator_idx)
        self.consciousness_update(abs(noise_factor - 1))
        phi_gain = base_gain * noise_factor * (1 + self.C * (PHI - 1) * 0.01)
        return phi_gain

    def simulate(self, input_power=1e-3, n_segments=50):
        powers = [input_power]
        for i in range(n_segments):
            gain_length = self.gain_length(i)
            power = powers[-1] * math.exp(0.03 / gain_length)
            powers.append(power)
        return powers
