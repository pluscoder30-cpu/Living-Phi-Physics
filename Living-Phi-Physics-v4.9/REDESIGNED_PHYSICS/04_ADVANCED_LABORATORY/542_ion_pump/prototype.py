import math
PHI = (1 + math.sqrt(5)) / 2

class PhiIonPump:
    def __init__(self, voltage, cathode_area):
        self.V = voltage
        self.A = cathode_area
        self.C = 0.0

    def phi_cathode_topology(self, position_idx):
        theta = 2 * math.pi * position_idx / PHI
        r = math.sqrt(position_idx)
        return r * math.cos(theta), r * math.sin(theta)

    def consciousness_update(self, ionization_efficiency):
        self.C = (1/PHI) * self.C + PHI * ionization_efficiency

    def ionization_rate(self, pressure):
        base_rate = self.V * self.A * pressure * 1e-12
        return base_rate * (1 + self.C * (PHI - 1) * 0.1)

    def pumping_speed(self, pressure):
        base_speed = self.A * 1e-4
        efficiency = 1 - math.exp(-pressure / 1e-6)
        self.consciousness_update(efficiency)
        return base_speed * efficiency * (1 + self.C * (PHI - 1) * 0.05)

    def ultimate_pressure(self, outgassing_rate):
        base_pressure = outgassing_rate / (self.A * 1e-4)
        return base_pressure * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_pressure
