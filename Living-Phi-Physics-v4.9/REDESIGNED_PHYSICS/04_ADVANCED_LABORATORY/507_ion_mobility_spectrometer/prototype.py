import math
PHI = (1 + math.sqrt(5)) / 2

class PhiIonMobility:
    def __init__(self, drift_length, E_field, gas_pressure):
        self.L = drift_length
        self.E = E_field
        self.P = gas_pressure
        self.C = 0.0

    def consciousness_update(self, field_inhomogeneity):
        self.C = (1/PHI) * self.C + PHI * field_inhomogeneity

    def drift_time(self, collision_cross_section):
        mu = 1.6e-19 / (self.P * collision_cross_section)
        t = self.L / (mu * self.E)
        self.consciousness_update(0.01)
        return t * (1 + self.C * (PHI - 1) * 0.01)

    def resolution(self, cs1, cs2):
        t1 = self.drift_time(cs1)
        t2 = self.drift_time(cs2)
        return abs(t1 - t2) / (2 * min(t1, t2))
