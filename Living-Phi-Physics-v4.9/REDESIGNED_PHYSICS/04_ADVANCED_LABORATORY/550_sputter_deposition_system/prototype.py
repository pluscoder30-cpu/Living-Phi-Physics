import math
PHI = (1 + math.sqrt(5)) / 2

class PhiSputterDeposition:
    def __init__(self, target_power, target_substrate_distance):
        self.P = target_power
        self.d = target_substrate_distance
        self.C = 0.0

    def phi_rotation_angle(self, time):
        golden_angle = 2 * math.pi * (1 - 1/PHI)
        return golden_angle * time

    def consciousness_update(self, uniformity_error):
        self.C = (1/PHI) * self.C + PHI * uniformity_error

    def deposition_rate(self, material, pressure):
        base_rates = {'Ti': 5, 'Al': 8, 'Cu': 10, 'Au': 12}
        base_rate = base_rates.get(material, 5)
        pressure_factor = math.exp(-pressure / 1e-2)
        return base_rate * pressure_factor * (1 + self.C * (PHI - 1) * 0.1)

    def film_uniformity(self, substrate_positions):
        thicknesses = []
        for pos in substrate_positions:
            angle = math.atan2(pos[1], pos[0])
            r = math.sqrt(pos[0]**2 + pos[1]**2)
            thickness = self.deposition_rate('Ti', 1e-2) * math.exp(-r / self.d)
            thicknesses.append(thickness)
        max_t = max(thicknesses)
        min_t = min(thicknesses)
        uniformity = min_t / max_t if max_t > 0 else 1.0
        self.consciousness_update(1 - uniformity)
        return uniformity * (1 + self.C * (PHI - 1) * 0.05)
