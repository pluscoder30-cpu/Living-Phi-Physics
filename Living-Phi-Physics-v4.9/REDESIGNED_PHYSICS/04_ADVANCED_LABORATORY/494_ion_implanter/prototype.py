import math
PHI = (1 + math.sqrt(5)) / 2
C_CRIT = 0.563

class PhiIonImplanter:
    def __init__(self, max_energy, max_current):
        self.max_energy = max_energy
        self.max_current = max_current
        self.C = 0.0
        self.total_dose = 0

    def phi_dose_profile(self, depth, lambda_char):
        return math.exp(-depth / (lambda_char * PHI))

    def consciousness_update(self, dose_error):
        self.C = (1/PHI) * self.C + PHI * dose_error

    def implant(self, target_dose, energy, n_steps=100):
        current_dose = 0
        profile = []
        for step in range(n_steps):
            depth = step * 1e-7
            target_at_depth = self.phi_dose_profile(depth, 1e-6) * target_dose
            current_dose += self.max_current * 1e-9
            dose_error = abs(current_dose - target_at_depth) / target_at_depth if target_at_depth > 0 else 0
            self.consciousness_update(dose_error)
            if self.C > C_CRIT:
                correction = 1 - (self.C - C_CRIT) * 0.5
                current_dose *= correction
            profile.append((depth, current_dose))
        self.total_dose += current_dose
        return profile
