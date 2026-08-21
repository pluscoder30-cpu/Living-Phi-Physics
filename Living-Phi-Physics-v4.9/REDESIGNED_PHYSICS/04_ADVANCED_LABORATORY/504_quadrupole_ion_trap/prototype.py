import math
PHI = (1 + math.sqrt(5)) / 2
C_CRIT = 0.563

class PhiIonTrap:
    def __init__(self, trap_radius, rf_voltage, rf_freq):
        self.r0 = trap_radius
        self.V_rf = rf_voltage
        self.freq = rf_freq
        self.C = 0.0
        self.ions = []

    def mathieu_params(self, m_z):
        q = 4 * 1.6e-19 * self.V_rf / (m_z * 1.66e-27 * (2 * math.pi * self.freq)**2 * self.r0**2)
        return 0, q

    def consciousness_update(self, space_charge_shift):
        self.C = (1/PHI) * self.C + PHI * space_charge_shift

    def secular_frequency(self, m_z):
        a, q = self.mathieu_params(m_z)
        omega = self.freq * q / (2 * math.sqrt(2))
        return omega * (1 + self.C * (PHI - 1))

    def space_charge_shift(self, n_ions):
        classical_shift = n_ions * 1e-10
        self.consciousness_update(classical_shift)
        if self.C > C_CRIT:
            return classical_shift * (1 - (self.C - C_CRIT) * PHI * 0.1)
        return classical_shift

    def add_ion(self, m_z, position, velocity):
        self.ions.append({'m': m_z, 'r': position, 'v': velocity})

    def simulate(self, dt=1e-6, n_steps=1000):
        trajectories = []
        for ion in self.ions:
            r, v, m = ion['r'], ion['v'], ion['m']
            path = [(r, v)]
            for _ in range(n_steps):
                omega_sec = self.secular_frequency(m)
                force = -omega_sec**2 * r + self.space_charge_shift(len(self.ions)) * 1e3
                v += force * dt
                r += v * dt
                path.append((r, v))
            trajectories.append(path)
        return trajectories
