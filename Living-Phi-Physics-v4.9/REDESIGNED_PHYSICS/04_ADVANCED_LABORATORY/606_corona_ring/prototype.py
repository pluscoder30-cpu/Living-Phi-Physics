import math
PHI = (1 + math.sqrt(5)) / 2

class PhiCoronaRing:
    def __init__(self, ring_diameter, wire_diameter):
        self.D = ring_diameter
        self.d = wire_diameter
        self.C = 0.0

    def phi_ring_profile(self, angle):
        return self.D / 2 * (1 + 0.1 * math.sin(PHI * angle))

    def consciousness_update(self, field_enhancement):
        self.C = (1/PHI) * self.C + PHI * field_enhancement

    def maximum_field(self, applied_voltage):
        base_field = applied_voltage / (self.D / 2)
        phi_field = base_field * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_field
        return phi_field

    def corona_inception_voltage(self):
        base_V = 3e6 * self.d / 2
        phi_V = base_V * (1 + self.C * (PHI - 1) * 0.1)
        return phi_V

    def field_uniformity(self):
        base_uniformity = 0.9
        return base_uniformity * (1 + self.C * (PHI - 1) * 0.05)
