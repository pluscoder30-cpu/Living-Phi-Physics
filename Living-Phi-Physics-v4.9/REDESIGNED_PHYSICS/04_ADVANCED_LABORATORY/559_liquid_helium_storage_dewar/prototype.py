import math
PHI = (1 + math.sqrt(5)) / 2

class PhiLHeDewar:
    def __init__(self, volume, neck_diameter):
        self.V = volume
        self.d0 = neck_diameter
        self.C = 0.0

    def phi_neck_diameter(self, position):
        return self.d0 * PHI ** (position / 0.5)

    def consciousness_update(self, boil_off_rate):
        self.C = (1/PHI) * self.C + PHI * boil_off_rate

    def heat_leak(self):
        base_leak = 1e-3 * self.d0**2
        phi_leak = base_leak * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_leak
        return phi_leak

    def boil_off_rate(self):
        latent_heat = 20.9e3  # J/L
        return self.heat_leak() / latent_heat

    def hold_time(self):
        rate = self.boil_off_rate()
        return self.V / rate if rate > 0 else float('inf')
