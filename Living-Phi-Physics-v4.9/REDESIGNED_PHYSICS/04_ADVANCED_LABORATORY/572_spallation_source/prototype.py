import math
PHI = (1 + math.sqrt(5)) / 2

class PhiSpallationSource:
    def __init__(self, proton_energy, beam_current):
        self.E_p = proton_energy
        self.I_p = beam_current
        self.C = 0.0

    def phi_target_structure(self, position):
        return 1e-2 * PHI ** (position % 4)

    def consciousness_update(self, target_stress):
        self.C = (1/PHI) * self.C + PHI * target_stress

    def neutron_yield(self):
        base_yield = self.E_p * self.I_p * 1e-3
        phi_yield = base_yield * (1 + self.C * (PHI - 1) * 0.1)
        return phi_yield

    def pulse_brightness(self, pulse_width):
        return self.neutron_yield() / pulse_width

    def target_lifetime(self, beam_power):
        base_lifetime = 1e8 / beam_power
        return base_lifetime * (1 + self.C * (PHI - 1) * 0.1)
