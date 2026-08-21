import math
PHI = (1 + math.sqrt(5)) / 2

class PhiXrayMicroscope:
    def __init__(self, zone_plate_diameter, outermost_zone):
        self.D = zone_plate_diameter
        self.dr = outermost_zone
        self.C = 0.0

    def phi_zone_radius(self, zone_idx):
        return self.dr * math.sqrt(zone_idx) * PHI ** (zone_idx % 5)

    def consciousness_update(self, resolution_error):
        self.C = (1/PHI) * self.C + PHI * resolution_error

    def spatial_resolution(self):
        base_res = 1.22 * self.dr
        phi_res = base_res * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_res
        return phi_res

    def depth_of_field(self):
        return self.dr**2 / self.C if self.C > 0 else float('inf')

    def magnification(self, image_distance, object_distance):
        return image_distance / object_distance * (1 + self.C * (PHI - 1) * 0.01)
