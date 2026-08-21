import math
PHI = (1 + math.sqrt(5)) / 2

class PhiCryoEM:
    def __init__(self, accelerating_voltage, defocus_range):
        self.V_accel = accelerating_voltage
        self.defocus_range = defocus_range
        self.C = 0.0

    def consciousness_update(self, motion_amplitude):
        self.C = (1/PHI) * self.C + PHI * motion_amplitude

    def beam_induced_motion(self, dose, frame_idx):
        base_motion = dose * 1e-3 * (frame_idx + 1)**0.5
        return base_motion * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_motion

    def resolution_limit(self, dose, n_frames):
        total_motion = sum(self.beam_induced_motion(dose / n_frames, i) for i in range(n_frames))
        self.consciousness_update(total_motion / n_frames)
        base_resolution = 1e-10 * (1 + total_motion)
        return base_resolution * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_resolution

    def single_particle_resolution(self, n_particles, particle_size, dose):
        base_res = particle_size / math.sqrt(n_particles) * math.exp(-dose * 1e-4)
        return base_res * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_res

    def motion_correction(self, image_stack):
        corrected = []
        for i, frame in enumerate(image_stack):
            motion = self.beam_induced_motion(1.0, i)
            corrected.append(frame * math.exp(-motion))
        return corrected
