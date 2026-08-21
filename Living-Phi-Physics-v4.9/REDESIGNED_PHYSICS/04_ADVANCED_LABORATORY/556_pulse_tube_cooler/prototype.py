import math
PHI = (1 + math.sqrt(5)) / 2

class PhiPulseTubeCooler:
    def __init__(self, regenerator_length, working_gas):
        self.L = regenerator_length
        self.gas = working_gas
        self.C = 0.0

    def phi_regenerator_pore(self, layer_idx):
        return 1e-4 * PHI ** (layer_idx % 5)

    def consciousness_update(self, regeneration_efficiency):
        self.C = (1/PHI) * self.C + PHI * regeneration_efficiency

    def cooling_power(self, cold_temperature):
        base_power = 1.0 * (80 - cold_temperature) / 80
        phi_power = base_power * (1 + self.C * (PHI - 1) * 0.1)
        return max(phi_power, 0)

    def coefficient_of_performance(self, cold_T, hot_T):
        carnot = cold_T / (hot_T - cold_T)
        base_cop = carnot * 0.3
        self.consciousness_update(abs(base_cop - carnot) / carnot if carnot > 0 else 0)
        return base_cop * (1 + self.C * (PHI - 1) * 0.05)

    def cold_head_temperature(self, input_power):
        T_cold = 80 - input_power * 10
        return max(T_cold, 4.2)
