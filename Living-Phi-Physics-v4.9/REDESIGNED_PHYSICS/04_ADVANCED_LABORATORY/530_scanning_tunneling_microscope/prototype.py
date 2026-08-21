import math
PHI = (1 + math.sqrt(5)) / 2

class PhiSTM:
    def __init__(self, bias_voltage, work_function):
        self.V_bias = bias_voltage
        self.phi_wf = work_function
        self.C = 0.0

    def consciousness_update(self, current_stability):
        self.C = (1/PHI) * self.C + PHI * current_stability

    def tunneling_current(self, distance):
        kappa = math.sqrt(2 * 1.67e-27 * self.phi_wf * 1.6e-19) / 1.055e-34
        return self.V_bias * math.exp(-2 * kappa * distance) * 1e9

    def distance_from_current(self, current):
        kappa = math.sqrt(2 * 1.67e-27 * self.phi_wf * 1.6e-19) / 1.055e-34
        return -math.log(current / (self.V_bias * 1e9)) / (2 * kappa)

    def topography(self, surface_heights, tunneling_current_setpoint):
        topography = []
        for h in surface_heights:
            distance = self.distance_from_current(tunneling_current_setpoint)
            current = self.tunneling_current(distance + h * 1e-10)
            self.consciousness_update(abs(current - tunneling_current_setpoint) / tunneling_current_setpoint)
            topography.append(h * (1 + self.C * (PHI - 1) * 0.01))
        return topography

    def spectroscopy(self, bias_range, distance, n_points=100):
        spectrum = []
        for i in range(n_points):
            V = bias_range[0] + i * (bias_range[1] - bias_range[0]) / n_points
            self.V_bias = V
            spectrum.append((V, self.tunneling_current(distance)))
        return spectrum
