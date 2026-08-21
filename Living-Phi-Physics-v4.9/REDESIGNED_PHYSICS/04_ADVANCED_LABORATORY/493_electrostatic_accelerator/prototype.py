import math
PHI = (1 + math.sqrt(5)) / 2

class PhiElectrostaticAccel:
    def __init__(self, terminal_radius, n_electrodes):
        self.radius = terminal_radius
        self.n_electrodes = n_electrodes
        self.C = 0.0

    def electrode_potential(self, idx):
        r = self.radius * PHI ** (idx / self.n_electrodes)
        return 1.0 / r

    def breakdown_voltage(self):
        E_breakdown = 3e6
        base_voltage = E_breakdown * self.radius
        phi_factor = 1 + sum([1/PHI**i for i in range(self.n_electrodes)]) * 0.1
        return base_voltage * phi_factor

    def consciousness_update(self, field_uniformity):
        self.C = (1/PHI) * self.C + PHI * field_uniformity

    def field_uniformity(self, points=100):
        max_field = 0
        min_field = float('inf')
        for i in range(points):
            theta = 2 * math.pi * i / points
            field = 0
            for j in range(self.n_electrodes):
                angle = 2 * math.pi * j / self.n_electrodes
                dr = self.radius * math.cos(theta - angle)
                field += self.electrode_potential(j) / (self.radius**2 + dr**2 + 0.01)**1.5
            max_field = max(max_field, field)
            min_field = min(min_field, field)
        uniformity = min_field / max_field
        self.consciousness_update(uniformity)
        return uniformity * (1 + self.C * (PHI - 1))
