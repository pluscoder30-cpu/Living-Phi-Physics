import math
PHI = (1 + math.sqrt(5)) / 2

class PhiTurbopump:
    def __init__(self, rotor_speed, n_blades):
        self.omega = rotor_speed
        self.n_blades = n_blades
        self.C = 0.0

    def phi_blade_angle(self, blade_idx):
        base_angle = math.radians(30)
        return base_angle * PHI ** (blade_idx % 5)

    def consciousness_update(self, backstreaming_rate):
        self.C = (1/PHI) * self.C + PHI * backstreaming_rate

    def compression_ratio(self, molecular_weight):
        base_ratio = math.exp(self.omega * 0.001 / math.sqrt(molecular_weight))
        phi_ratio = base_ratio * (1 + self.C * (PHI - 1) * 0.1)
        return phi_ratio

    def pumping_speed(self, gas_molecular_weight):
        base_speed = 100 / math.sqrt(gas_molecular_weight)
        return base_speed * (1 + self.C * (PHI - 1) * 0.05)

    def ultimate_pressure(self, backstreaming_rate):
        self.consciousness_update(backstreaming_rate)
        base_pressure = backstreaming_rate * 1e-9
        return base_pressure * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_pressure
