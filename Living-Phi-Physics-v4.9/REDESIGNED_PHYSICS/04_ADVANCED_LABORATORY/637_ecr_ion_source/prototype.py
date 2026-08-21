import math
PHI = (1 + math.sqrt(5)) / 2

class PhiECRIonSource:
    def __init__(self, rf_frequency, magnetic_field):
        self.f_RF = rf_frequency
        self.B = magnetic_field
        self.C = 0.0

    def phi_magnetic_geometry(self, position):
        return self.B * PHI ** (position % 4)

    def consciousness_update(self, charge_state_error):
        self.C = (1/PHI) * self.C + PHI * charge_state_error

    def ecr_condition(self):
        f_ce = 28e9 * self.B
        return abs(f_ce - self.f_RF) / self.f_RF

    def charge_state_distribution(self, ion_mass):
        mean_charge = math.sqrt(ion_mass) * 0.3
        spread = mean_charge * 0.2
        phi_spread = spread * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else spread
        return mean_charge, phi_spread

    def extraction_efficiency(self):
        base_eff = 0.1
        return base_eff * (1 + self.C * (PHI - 1) * 0.1)
