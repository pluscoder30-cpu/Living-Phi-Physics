import math
PHI = (1 + math.sqrt(5)) / 2

class PhiMALDI:
    def __init__(self, laser_energy, matrix_type):
        self.E_laser = laser_energy
        self.matrix = matrix_type
        self.C = 0.0
        self.shot_history = []

    def consciousness_update(self, signal_variation):
        self.C = (1/PHI) * self.C + PHI * signal_variation

    def phi_crystal_size(self, position):
        return 1e-6 * PHI ** (position % 10)

    def single_shot(self, crystal_position, analyte_mw):
        crystal_size = self.phi_crystal_size(crystal_position)
        yield_ = self.E_laser * 1e-6 / (crystal_size * analyte_mw)
        self.shot_history.append(yield_)
        if len(self.shot_history) > 1:
            variation = abs(yield_ - self.shot_history[-2]) / max(self.shot_history[-2], 1e-10)
            self.consciousness_update(variation)
        return yield_ * (1 + self.C * (PHI - 1) * 0.1)

    def shot_to_shot_rsd(self):
        if len(self.shot_history) < 2:
            return 0
        mean = sum(self.shot_history) / len(self.shot_history)
        variance = sum((x - mean)**2 for x in self.shot_history) / len(self.shot_history)
        return math.sqrt(variance) / mean if mean > 0 else 0
