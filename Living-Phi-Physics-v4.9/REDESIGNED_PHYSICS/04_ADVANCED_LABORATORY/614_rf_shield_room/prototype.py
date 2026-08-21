import math
PHI = (1 + math.sqrt(5)) / 2

class PhiRFShieldRoom:
    def __init__(self, room_dimensions, wall_thickness):
        self.dims = room_dimensions
        self.t = wall_thickness
        self.C = 0.0

    def phi_door_seal(self, seal_idx):
        base_finger = 1e-3
        return base_finger * PHI ** (seal_idx % 3)

    def consciousness_update(self, seal_leakage):
        self.C = (1/PHI) * self.C + PHI * seal_leakage

    def shielding_effectiveness(self, frequency):
        base_SE = 80 + 20 * math.log10(frequency / 1e6)
        phi_SE = base_SE * (1 + self.C * (PHI - 1) * 0.05)
        return phi_SE

    def door_shielding(self):
        base_door_SE = 60
        return base_door_SE * (1 + self.C * (PHI - 1) * 0.1)

    def penetration_loss(self, cable_type):
        base_loss = 40  # dB
        return base_loss * (1 + self.C * (PHI - 1) * 0.05)
