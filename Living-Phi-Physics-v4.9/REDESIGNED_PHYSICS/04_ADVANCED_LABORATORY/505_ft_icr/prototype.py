import math
PHI = (1 + math.sqrt(5)) / 2

class PhiFTICR:
    def __init__(self, magnetic_field, trap_length):
        self.B = magnetic_field
        self.L = trap_length
        self.C = 0.0

    def cyclotron_frequency(self, m_z, charge):
        return charge * self.B / (2 * math.pi * m_z)

    def consciousness_update(self, signal_strength):
        self.C = (1/PHI) * self.C + PHI * signal_strength

    def image_current(self, m_z, charge, n_ions):
        omega_c = self.cyclotron_frequency(m_z, charge)
        base_current = n_ions * charge * omega_c * 1e-15
        return base_current * (1 + self.C * (PHI - 1))

    def mass_resolution(self, m_z, charge, detection_time):
        omega_c = self.cyclotron_frequency(m_z, charge)
        base_resolution = omega_c * detection_time / (2 * math.pi)
        self.consciousness_update(1 / detection_time)
        if self.C > 0.563:
            return base_resolution * (1 + (self.C - 0.563) * PHI)
        return base_resolution
