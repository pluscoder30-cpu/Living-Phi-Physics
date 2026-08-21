import math
PHI = (1 + math.sqrt(5)) / 2
C_CRIT = 0.563

class PhiICPMS:
    def __init__(self, rf_power, plasma_gas_flow):
        self.rf_power = rf_power
        self.gas_flow = plasma_gas_flow
        self.C = 0.0
        self.interference_map = {}

    def consciousness_update(self, interference_level):
        self.C = (1/PHI) * self.C + PHI * interference_level

    def ionization_efficiency(self, ionization_energy):
        plasma_temp = self.rf_power * 1e-3
        return math.exp(-ionization_energy / (plasma_temp * 8.6e-5))

    def signal(self, analyte_mz, concentration, matrix_element=None):
        base_signal = concentration * self.ionization_efficiency(10) * 1e6
        if matrix_element:
            key = f"{analyte_mz}_{matrix_element}"
            if key not in self.interference_map:
                self.interference_map[key] = 0.1 * math.exp(-analyte_mz / 100)
            interference = self.interference_map[key]
            base_signal *= (1 - interference)
            self.consciousness_update(interference)
        if self.C > C_CRIT:
            return base_signal * (1 + (self.C - C_CRIT) * PHI)
        return base_signal
