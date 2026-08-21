import math
PHI = (1 + math.sqrt(5)) / 2

class PhiXrayCT:
    def __init__(self, n_projections, reconstruction_radius):
        self.n_proj = n_projections
        self.R = reconstruction_radius
        self.C = 0.0

    def phi_projection_angle(self, proj_idx):
        golden_angle = math.pi * (3 - math.sqrt(5))
        return golden_angle * proj_idx

    def consciousness_update(self, artifact_level):
        self.C = (1/PHI) * self.C + PHI * artifact_level

    def spatial_resolution(self, focal_spot, detector_pitch):
        base_res = max(focal_spot, detector_pitch)
        phi_res = base_res * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_res
        return phi_res

    def contrast_resolution(self, material_difference):
        base_contrast = material_difference * 0.1
        return base_contrast * (1 + self.C * (PHI - 1) * 0.1)

    def reconstruction_quality(self, n_projections):
        base_quality = min(1.0, n_projections / 360)
        return base_quality * (1 + self.C * (PHI - 1) * 0.05)
