import math
PHI = (1 + math.sqrt(5)) / 2

class PhiFaradayCage:
    def __init__(self, cage_dimensions, mesh_wire_diameter):
        self.dims = cage_dimensions
        self.d_wire = mesh_wire_diameter
        self.C = 0.0

    def phi_mesh_spacing(self, position):
        base_spacing = 1e-2
        return base_spacing * PHI ** (position % 3)

    def consciousness_update(self, field_leakage):
        self.C = (1/PHI) * self.C + PHI * field_leakage

    def shielding_effectiveness(self, frequency):
        base_SE = 20 * math.log10(1 / (self.phi_mesh_spacing(0) * frequency / 3e8))
        phi_SE = base_SE * (1 + self.C * (PHI - 1) * 0.1)
        return phi_SE

    def aperture_resonance(self):
        return 3e8 / (2 * self.phi_mesh_spacing(0))

    def field_attenuation(self, frequency):
        SE = self.shielding_effectiveness(frequency)
        return 10 ** (-SE / 20)
