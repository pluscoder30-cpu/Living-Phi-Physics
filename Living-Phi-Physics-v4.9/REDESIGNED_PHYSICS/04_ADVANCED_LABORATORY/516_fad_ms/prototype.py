import math
PHI = (1 + math.sqrt(5)) / 2

class PhiFADMS:
    def __init__(self, tip_radius, applied_voltage):
        self.r_tip = tip_radius
        self.V = applied_voltage
        self.C = 0.0

    def phi_tip_array(self, n_tips):
        positions = []
        for i in range(n_tips):
            x = i * PHI
            y = math.sin(2 * math.pi * i / PHI)
            positions.append((x, y))
        return positions

    def consciousness_update(self, field_enhancement):
        self.C = (1/PHI) * self.C + PHI * field_enhancement

    def field_enhancement(self):
        base_enhancement = self.V / self.r_tip
        return base_enhancement * (1 + self.C * (PHI - 1))

    def ion_signal(self, binding_energy, ionization_efficiency):
        field = self.field_enhancement()
        energy = binding_energy - 1e-19 * field * self.r_tip
        signal = ionization_efficiency * math.exp(-energy / (8.6e-5 * 300)) if energy > 0 else ionization_efficiency
        self.consciousness_update(signal)
        return signal * (1 + self.C * (PHI - 1) * 0.1)
