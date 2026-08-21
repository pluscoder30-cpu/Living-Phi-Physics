import math
PHI = (1 + math.sqrt(5)) / 2

class PhiGMCooler:
    def __init__(self, compressor_power, regenerator_type):
        self.P = compressor_power
        self.regenerator = regenerator_type
        self.C = 0.0

    def phi_displacer_volume(self, position):
        return 1e-4 * PHI ** (position % 3)

    def consciousness_update(self, expansion_efficiency):
        self.C = (1/PHI) * self.C + PHI * expansion_efficiency

    def cooling_power(self, temperature):
        base_power = self.P * 0.1 * (80 - temperature) / 80
        phi_power = base_power * (1 + self.C * (PHI - 1) * 0.1)
        return max(phi_power, 0)

    def cold_head_temperature(self):
        T_cold = 80 - self.P * 5
        return max(T_cold, 30)

    def efficiency(self, hot_T, cold_T):
        carnot = 1 - cold_T / hot_T
        base_eff = carnot * 0.2
        self.consciousness_update(abs(base_eff - carnot) / carnot if carnot > 0 else 0)
        return base_eff * (1 + self.C * (PHI - 1) * 0.05)
