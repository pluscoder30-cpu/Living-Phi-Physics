import math
PHI = (1 + math.sqrt(5)) / 2
C_CRIT = 0.563

class PhiESI_FIB:
    def __init__(self, emission_current, beam_energy):
        self.I_emission = emission_current
        self.E_beam = beam_energy
        self.C = 0.0

    def consciousness_update(self, current_stability):
        self.C = (1/PHI) * self.C + PHI * current_stability

    def beam_current(self, extraction_voltage):
        base_current = self.I_emission * math.exp(-3.5 / extraction_voltage)
        self.consciousness_update(abs(base_current - self.I_emission) / self.I_emission)
        if self.C > C_CRIT:
            return base_current * (1 + (self.C - C_CRIT) * PHI * 0.1)
        return base_current

    def spot_size(self, working_distance, aberration):
        classical_spot = math.sqrt(aberration * working_distance**3)
        return classical_spot * (1 - self.C * (PHI - 1) * 0.05) if self.C > 0 else classical_spot
