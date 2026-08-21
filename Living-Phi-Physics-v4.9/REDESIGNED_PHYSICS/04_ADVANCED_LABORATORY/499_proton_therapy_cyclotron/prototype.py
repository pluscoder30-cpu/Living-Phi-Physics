import math
PHI = (1 + math.sqrt(5)) / 2
C_CRIT = 0.563

class PhiProtonTherapy:
    def __init__(self, extraction_energy, beam_current):
        self.energy = extraction_energy * 1e6
        self.current = beam_current
        self.C = 0.0

    def consciousness_update(self, dose_deviation):
        self.C = (1/PHI) * self.C + PHI * dose_deviation

    def dose_rate(self, depth):
        peak_depth = self.energy / 1e6 * 0.003
        return 1.0 if depth < peak_depth else math.exp(-(depth - peak_depth) / 0.01)

    def treatment_plan(self, target_depth, fraction_dose, n_fractions=30):
        doses = []
        for frac in range(n_fractions):
            actual_dose = fraction_dose * self.dose_rate(target_depth)
            deviation = abs(actual_dose - fraction_dose) / fraction_dose
            self.consciousness_update(deviation)
            if self.C > C_CRIT:
                actual_dose *= 1 + (self.C - C_CRIT) * (PHI - 1) * 0.1
            doses.append(actual_dose)
        return doses
