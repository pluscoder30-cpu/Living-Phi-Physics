import math
PHI = (1 + math.sqrt(5)) / 2

class PhiIsotron:
    def __init__(self, r_min, n_turns):
        self.r_min = r_min
        self.n_turns = n_turns
        self.C = 0.0

    def phi_spiral(self, theta):
        return self.r_min * PHI ** (2 * theta / math.pi)

    def electrode_field(self, r, theta):
        base_field = 1 / r
        phi_correction = 1 + self.C * (PHI - 1)
        return base_field * phi_correction

    def consciousness_update(self, field_error):
        self.C = (1/PHI) * self.C + PHI * field_error

    def track_particle(self, initial_r, n_steps=1000):
        r = initial_r
        theta = 0
        trajectory = [(r, theta)]
        dt = 0.001
        for step in range(n_steps):
            target_r = self.phi_spiral(theta)
            field_error = abs(r - target_r) / target_r
            self.consciousness_update(field_error * 1e-3)
            field = self.electrode_field(r, theta)
            r += field * math.cos(theta) * dt
            theta += field * math.sin(theta) * dt / r
            trajectory.append((r, theta))
        return trajectory
