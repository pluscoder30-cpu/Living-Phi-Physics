import math
PHI = (1 + math.sqrt(5)) / 2

class PhiFunctionGenerator:
    def __init__(self, base_frequency, amplitude):
        self.f0 = base_frequency
        self.A = amplitude
        self.C = 0.0

    def phi_phase_accumulation(self, time, phase_idx):
        return 2 * math.pi * self.f0 * time * PHI ** (phase_idx % 3)

    def consciousness_update(self, harmonic_distortion):
        self.C = (1/PHI) * self.C + PHI * harmonic_distortion

    def sine_wave(self, time, n_harmonics=10):
        signal = 0
        for n in range(1, n_harmonics + 1):
            harmonic_amp = self.A / n * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else self.A / n
            signal += harmonic_amp * math.sin(self.phi_phase_accumulation(time, n))
        return signal

    def total_harmonic_distortion(self):
        base_thd = 0.01
        phi_thd = base_thd * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_thd
        return phi_thd

    def frequency_stability(self, time_interval):
        base_drift = 1e-6 * time_interval
        return base_drift * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_drift
