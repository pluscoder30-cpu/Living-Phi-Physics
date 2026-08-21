import math
PHI = (1 + math.sqrt(5)) / 2

class PhiVanDeGraaff:
    def __init__(self, sphere_radius, belt_speed):
        self.R = sphere_radius
        self.v_belt = belt_speed
        self.C = 0.0

    def phi_helix_electrode(self, angle):
        return self.R * (1 + 0.1 * math.sin(PHI * angle))

    def consciousness_update(self, corona_current):
        self.C = (1/PHI) * self.C + PHI * corona_current

    def maximum_voltage(self):
        E_breakdown = 3e6  # V/m
        base_voltage = E_breakdown * self.R
        phi_voltage = base_voltage * (1 + self.C * (PHI - 1) * 0.1)
        return phi_voltage

    def charge_rate(self, belt_charge_density):
        return belt_charge_density * self.v_belt * 2 * math.pi * self.R

    def voltage_stability(self, load_current):
        base_stability = 1e-3
        phi_stability = base_stability * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_stability
        return phi_stability * load_current
