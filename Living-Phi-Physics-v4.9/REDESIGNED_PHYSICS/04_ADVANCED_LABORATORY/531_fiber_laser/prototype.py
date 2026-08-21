import math
PHI = (1 + math.sqrt(5)) / 2

class PhiFiberLaser:
    def __init__(self, core_doping, fiber_length):
        self.doping = core_doping
        self.L = fiber_length
        self.C = 0.0

    def phi_core_diameter(self, position):
        return 1e-6 * PHI ** (position / self.L)

    def consciousness_update(self, nonlinear_coeff):
        self.C = (1/PHI) * self.C + PHI * nonlinear_coeff

    def gain(self, position, pump_power):
        base_gain = self.doping * pump_power * 1e-3
        core_factor = self.phi_core_diameter(position) / 1e-6
        return base_gain / core_factor

    def output_power(self, pump_power, n_sections=100):
        power = 1e-3
        for i in range(n_sections):
            position = i * self.L / n_sections
            g = self.gain(position, pump_power)
            core_area = math.pi * (self.phi_core_diameter(position) / 2)**2
            gamma = 2.6e-20 / (core_area * 1e-12)
            self.consciousness_update(gamma)
            phi_gain = g * (1 - self.C * (PHI - 1) * 0.01) if self.C > 0 else g
            power *= math.exp(phi_gain / n_sections)
        return power

    def beam_quality(self):
        return max(1.0 * (1 - self.C * (PHI - 1) * 0.01), 0.8) if self.C > 0 else 1.0

    def threshold_pump(self):
        return 0.1 / (1 + self.C * (PHI - 1))
