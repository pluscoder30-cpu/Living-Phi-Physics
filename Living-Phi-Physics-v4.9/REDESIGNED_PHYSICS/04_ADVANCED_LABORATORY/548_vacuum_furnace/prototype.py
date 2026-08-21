import math
PHI = (1 + math.sqrt(5)) / 2

class PhiVacuumFurnace:
    def __init__(self, max_temperature, chamber_volume):
        self.T_max = max_temperature
        self.V = chamber_volume
        self.C = 0.0
        self.n_zones = 5

    def phi_zone_boundary(self, zone_idx):
        return zone_idx * PHI / self.n_zones

    def consciousness_update(self, temperature_uniformity):
        self.C = (1/PHI) * self.C + PHI * temperature_uniformity

    def zone_temperature(self, zone_idx, setpoint):
        phi_offset = (zone_idx - self.n_zones / 2) * 0.01 * PHI
        self.consciousness_update(abs(phi_offset))
        return setpoint * (1 + phi_offset * (1 - self.C * (PHI - 1) * 0.1))

    def temperature_uniformity(self, setpoint):
        temps = [self.zone_temperature(i, setpoint) for i in range(self.n_zones)]
        max_T = max(temps)
        min_T = min(temps)
        return min_T / max_T if max_T > 0 else 1.0

    def heating_rate(self, power, thermal_mass):
        base_rate = power / thermal_mass
        return base_rate * (1 + self.C * (PHI - 1) * 0.05)
