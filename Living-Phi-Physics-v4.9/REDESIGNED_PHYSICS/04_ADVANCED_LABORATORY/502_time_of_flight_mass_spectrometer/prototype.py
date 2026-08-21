import math
PHI = (1 + math.sqrt(5)) / 2

class PhiTOF:
    def __init__(self, drift_length, accelerating_voltage):
        self.L = drift_length
        self.V_acc = accelerating_voltage
        self.C = 0.0

    def consciousness_update(self, time_spread):
        self.C = (1/PHI) * self.C + PHI * time_spread

    def flight_time(self, m_z, kinetic_energy):
        v = math.sqrt(2 * kinetic_energy / m_z)
        base_time = self.L / v
        phi_correction = 1 + self.C * (PHI - 1)
        return base_time * phi_correction

    def mass_resolution(self, m_z, energy_spread):
        t0 = self.flight_time(m_z, self.V_acc * 1.6e-19)
        dt = self.flight_time(m_z, (self.V_acc + energy_spread) * 1.6e-19) - t0
        resolution = t0 / (2 * abs(dt)) if dt > 0 else 1000
        self.consciousness_update(abs(dt) / t0)
        if self.C > 0.563:
            return resolution * (1 + (self.C - 0.563) * PHI)
        return resolution

    def spectrum(self, mass_range, energy_spread=0.1):
        spectrum = []
        for m in range(mass_range[0], mass_range[1]):
            m_kg = m * 1.66e-27
            t = self.flight_time(m_kg, self.V_acc * 1.6e-19)
            res = self.mass_resolution(m_kg, energy_spread * 1.6e-19)
            spectrum.append((m, t, res))
        return spectrum
