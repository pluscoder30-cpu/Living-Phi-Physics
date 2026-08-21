import math
PHI = (1 + math.sqrt(5)) / 2

class PhiElectrostaticPrecipitator:
    def __init__(self, plate_area, wire_spacing):
        self.A = plate_area
        self.d = wire_spacing
        self.C = 0.0

    def phi_wire_spacing(self, wire_idx):
        return self.d * PHI ** (wire_idx % 3)

    def consciousness_update(self, collection_error):
        self.C = (1/PHI) * self.C + PHI * collection_error

    def collection_efficiency(self, particle_size, gas_velocity):
        base_eff = 1 - math.exp(-particle_size * 1e-6 / gas_velocity)
        phi_eff = base_eff * (1 + self.C * (PHI - 1) * 0.1)
        return min(phi_eff, 1.0)

    def corona_power(self, voltage):
        return voltage**2 / (self.d * 1e6)

    def particle_charge(self, particle_diameter, voltage):
        base_charge = particle_diameter**2 * voltage / (4 * math.pi * 8.85e-12 * self.d)
        return base_charge * (1 + self.C * (PHI - 1) * 0.1)
