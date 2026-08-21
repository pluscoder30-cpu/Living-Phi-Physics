import math
PHI = (1 + math.sqrt(5)) / 2

class PhiSeismicIsolation:
    def __init__(self, platform_mass, n_isolation_stages):
        self.m = platform_mass
        self.N = n_isolation_stages
        self.C = 0.0

    def phi_spring_constant(self, stage_idx):
        base_k = 1e4
        return base_k * PHI ** (stage_idx % 3)

    def consciousness_update(self, residual_vibration):
        self.C = (1/PHI) * self.C + PHI * residual_vibration

    def transfer_function(self, frequency):
        base_TF = 1
        for i in range(self.N):
            k = self.phi_spring_constant(i)
            omega_n = math.sqrt(k / self.m)
            base_TF *= (frequency / omega_n)**2 / (1 + (frequency / omega_n)**2)
        phi_TF = base_TF * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_TF
        return phi_TF

    def residual_motion(self, ground_motion, frequency):
        return ground_motion * self.transfer_function(frequency)

    def active_damping_efficiency(self):
        base_eff = 0.9
        return base_eff * (1 + self.C * (PHI - 1) * 0.05)
