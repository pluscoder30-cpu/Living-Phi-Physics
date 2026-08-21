import math
PHI = (1 + math.sqrt(5)) / 2

class PhiSemiconductorLaser:
    def __init__(self, n_wells, well_width):
        self.n_wells = n_wells
        self.w0 = well_width
        self.C = 0.0

    def phi_well_width(self, well_idx):
        return self.w0 * PHI ** (well_idx / self.n_wells)

    def consciousness_update(self, threshold_current):
        self.C = (1/PHI) * self.C + PHI * threshold_current

    def gain(self, current, wavelength):
        base_gain = current * 1e-3
        return base_gain * (1 + self.C * (PHI - 1) * 0.1)

    def threshold_current(self):
        base_threshold = 10.0
        phi_threshold = base_threshold * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_threshold
        return max(phi_threshold, base_threshold * 0.3)

    def output_power(self, current):
        if current > self.threshold_current():
            return (current - self.threshold_current()) * 0.5
        return 0

    def wall_plug_efficiency(self, current, voltage):
        optical_power = self.output_power(current)
        electrical_power = current * voltage
        return optical_power / electrical_power if electrical_power > 0 else 0
