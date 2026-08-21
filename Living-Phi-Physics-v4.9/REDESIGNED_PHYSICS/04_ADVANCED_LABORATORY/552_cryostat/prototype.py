import math
PHI = (1 + math.sqrt(5)) / 2

class PhiCryostat:
    def __init__(self, n_shields, base_temperature):
        self.n_shields = n_shields
        self.T_base = base_temperature
        self.C = 0.0

    def phi_shield_spacing(self, shield_idx):
        return 1e-2 * PHI ** (shield_idx % 4)

    def consciousness_update(self, heat_load):
        self.C = (1/PHI) * self.C + PHI * heat_load

    def shield_temperature(self, shield_idx):
        T_outer = 300
        T_inner = self.T_base
        ratio = (T_outer - T_inner) * PHI ** (-shield_idx) / PHI ** self.n_shields
        return T_inner + ratio

    def total_heat_load(self, view_factor=0.01):
        sigma = 5.67e-8
        total = 0
        for i in range(self.n_shields):
            T = self.shield_temperature(i)
            T_next = self.shield_temperature(i + 1) if i < self.n_shields - 1 else self.T_base
            heat = sigma * view_factor * (T**4 - T_next**4)
            total += heat
        self.consciousness_update(total / 1e-6)
        return total * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else total

    def hold_time(self, cryogen_volume, latent_heat):
        return cryogen_volume * latent_heat / max(self.total_heat_load(), 1e-12)
