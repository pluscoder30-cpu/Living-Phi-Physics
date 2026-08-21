import math
PHI = (1 + math.sqrt(5)) / 2

class PhiVacuumGauge:
    def __init__(self, gauge_type, measurement_range):
        self.type = gauge_type
        self.range = measurement_range
        self.C = 0.0

    def phi_grid_structure(self, grid_idx):
        return 1e-3 * PHI ** (grid_idx % 6)

    def consciousness_update(self, calibration_drift):
        self.C = (1/PHI) * self.C + PHI * calibration_drift

    def sensitivity(self, gas_type):
        base_sensitivity = {'N2': 1.0, 'Ar': 1.3, 'H2': 0.4, 'He': 0.15}
        S = base_sensitivity.get(gas_type, 1.0)
        return S * (1 + self.C * (PHI - 1) * 0.01)

    def pressure_reading(self, raw_signal, gas_type='N2'):
        sensitivity = self.sensitivity(gas_type)
        base_pressure = raw_signal / sensitivity
        self.consciousness_update(abs(raw_signal - 1.0) / 1.0 if raw_signal > 0 else 0)
        return base_pressure * (1 + self.C * (PHI - 1) * 0.005)

    def calibration_stability(self, time_hours):
        drift = 0.01 * time_hours
        return drift * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else drift
