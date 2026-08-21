import math
PHI = (1 + math.sqrt(5)) / 2

class PhiHighVoltageSwitch:
    def __init__(self, voltage_rating, switching_speed):
        self.V_rating = voltage_rating
        self.t_switch = switching_speed
        self.C = 0.0

    def phi_electrode_profile(self, angle):
        return 1e-3 * PHI ** (int(angle / math.pi) % 3)

    def consciousness_update(self, switching_error):
        self.C = (1/PHI) * self.C + PHI * switching_error

    def breakdown_voltage(self, gap_distance):
        base_V = 3e6 * gap_distance
        phi_V = base_V * (1 + self.C * (PHI - 1) * 0.1)
        return phi_V

    def switching_jitter(self):
        base_jitter = 1e-9
        phi_jitter = base_jitter * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_jitter
        return phi_jitter

    def lifetime(self, n_switches):
        base_lifetime = 1e6
        return base_lifetime * (1 + self.C * (PHI - 1) * 0.1)
