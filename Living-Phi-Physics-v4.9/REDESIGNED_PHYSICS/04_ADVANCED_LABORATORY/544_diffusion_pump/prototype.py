import math
PHI = (1 + math.sqrt(5)) / 2

class PhiDiffusionPump:
    def __init__(self, nozzle_diameter, oil_type):
        self.d = nozzle_diameter
        self.oil = oil_type
        self.C = 0.0

    def phi_nozzle_profile(self, position):
        return self.d * PHI ** (position / 0.1)

    def consciousness_update(self, backstreaming):
        self.C = (1/PHI) * self.C + PHI * backstreaming

    def pumping_speed(self, gas_molecular_weight):
        base_speed = 10 * self.d**2 / math.sqrt(gas_molecular_weight)
        return base_speed * (1 + self.C * (PHI - 1) * 0.1)

    def compression_ratio(self, gas_molecular_weight):
        base_ratio = math.exp(20 / math.sqrt(gas_molecular_weight))
        return base_ratio * (1 + self.C * (PHI - 1) * 0.05)

    def backstreaming_rate(self, foreline_pressure):
        base_rate = foreline_pressure * 1e-4
        self.consciousness_update(base_rate)
        return base_rate * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_rate
