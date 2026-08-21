import math
PHI = (1 + math.sqrt(5)) / 2

class PhiHe3Refrigerator:
    def __init__(self, he3_volume, pumping_speed):
        self.V = he3_volume
        self.S = pumping_speed
        self.C = 0.0

    def phi_pump_line(self, position):
        return 1e-3 * PHI ** (position / 0.5)

    def consciousness_update(self, vapor_pressure):
        self.C = (1/PHI) * self.C + PHI * vapor_pressure

    def temperature(self, pumping_rate):
        base_T = 0.3 * (1e-3 / max(pumping_rate, 1e-6))**0.5
        self.consciousness_update(base_T / 0.3)
        return base_T * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_T

    def cooling_power(self, temperature):
        base_power = self.S * 1e-9 * temperature**2
        return base_power * (1 + self.C * (PHI - 1) * 0.1)

    def hold_time(self, heat_leak):
        total_he3 = self.V * 81  # moles/m3 * density
        cooling = self.cooling_power(0.3)
        return total_he3 * 20.9e3 / max(heat_leak - cooling, 1e-12)
