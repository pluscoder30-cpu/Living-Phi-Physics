import math
PHI = (1 + math.sqrt(5)) / 2

class PhiOrbitrap:
    def __init__(self, central_radius, outer_radius):
        self.Rc = central_radius
        self.Ro = outer_radius
        self.C = 0.0

    def consciousness_update(self, frequency_stability):
        self.C = (1/PHI) * self.C + PHI * frequency_stability

    def axial_frequency(self, m_z, charge):
        omega0 = math.sqrt(charge / m_z)
        return omega0 * (1 + self.C * (PHI - 1))

    def image_current(self, m_z, charge, n_ions, time):
        omega_z = self.axial_frequency(m_z, charge)
        omega_r = omega_z / math.sqrt(2)
        current = n_ions * charge * (math.sin(omega_z * time) + math.sin(omega_r * time)) * 1e-15
        self.consciousness_update(abs(math.sin(omega_z * time)))
        return current * (1 + self.C * (PHI - 1) * 0.1)

    def mass_resolution(self, m_z, charge, orbit_time):
        omega_z = self.axial_frequency(m_z, charge)
        return omega_z * orbit_time / (4 * math.pi)
