import math
PHI = (1 + math.sqrt(5)) / 2

class PhiNeutronChopper:
    def __init__(self, rotation_speed, n_slots):
        self.omega = rotation_speed
        self.n_slots = n_slots
        self.C = 0.0

    def phi_slot_width(self, slot_idx):
        base_width = 1e-3
        return base_width * PHI ** (slot_idx % 3)

    def consciousness_update(self, timing_error):
        self.C = (1/PHI) * self.C + PHI * timing_error

    def burst_time(self, slot_width):
        base_time = slot_width / (self.omega * 0.1)
        phi_time = base_time * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_time
        return phi_time

    def frame_overlap_limit(self):
        return 2 * math.pi / (self.omega * self.n_slots)

    def energy_resolution(self, wavelength):
        return self.burst_time(1e-3) / wavelength * 1e-3
