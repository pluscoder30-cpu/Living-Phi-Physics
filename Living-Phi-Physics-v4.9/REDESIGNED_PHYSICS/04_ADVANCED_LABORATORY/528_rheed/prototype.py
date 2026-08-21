import math
PHI = (1 + math.sqrt(5)) / 2
C_CRIT = 0.563

class PhiRHEED:
    def __init__(self, beam_energy, grazing_angle):
        self.E_beam = beam_energy
        self.angle = grazing_angle
        self.C = 0.0

    def consciousness_update(self, growth_rate):
        self.C = (1/PHI) * self.C + PHI * growth_rate

    def streak_intensity(self, surface_roughness):
        return 1.0 / (1 + surface_roughness**2)

    def growth_monitoring(self, n_monolayers, growth_rate):
        oscillations = []
        for ml in range(n_monolayers):
            intensity = self.streak_intensity(0.1) * (1 + 0.5 * math.cos(2 * math.pi * ml))
            self.consciousness_update(growth_rate)
            if self.C > C_CRIT:
                intensity *= (1 + (self.C - C_CRIT) * PHI * 0.1)
            oscillations.append((ml, intensity))
        return oscillations

    def growth_rate_measurement(self, oscillation_period):
        rate = 1.0 / oscillation_period if oscillation_period > 0 else 0
        return rate * (1 + self.C * (PHI - 1) * 0.01)
