import math
PHI = (1 + math.sqrt(5)) / 2
C_CRIT = 0.563

class PhiQuadrupole:
    def __init__(self, length, rf_freq):
        self.length = length
        self.freq = rf_freq
        self.C = 0.0

    def stability_parameter(self, m_z, V_rf, V_dc):
        q = 4 * 1.6e-19 * V_rf / (m_z * 1.66e-27 * (2 * math.pi * self.freq)**2 * self.length**2)
        a = 8 * 1.6e-19 * V_dc / (m_z * 1.66e-27 * (2 * math.pi * self.freq)**2 * self.length**2)
        return q, a

    def consciousness_update(self, transmission):
        self.C = (1/PHI) * self.C + PHI * transmission

    def transmission(self, m_z, V_rf, V_dc):
        q, a = self.stability_parameter(m_z, V_rf, V_dc)
        in_stability = (q < 0.706) and (abs(a) < 0.237)
        if in_stability:
            base_trans = 1.0 - abs(q - 0.35) * 2
            self.consciousness_update(base_trans)
            if self.C > C_CRIT:
                return base_trans * (1 + (self.C - C_CRIT) * PHI)
            return base_trans
        return 0.0

    def mass_spectrum(self, mass_range, V_rf, V_dc):
        spectrum = []
        for m_z in range(mass_range[0], mass_range[1]):
            trans = self.transmission(m_z * 1.66e-27, V_rf, V_dc)
            spectrum.append((m_z, trans))
        return spectrum
