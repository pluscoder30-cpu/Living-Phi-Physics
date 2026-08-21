import math
PHI = (1 + math.sqrt(5)) / 2

class PhiAFM:
    def __init__(self, cantilever_length, spring_constant):
        self.L = cantilever_length
        self.k = spring_constant
        self.C = 0.0

    def consciousness_update(self, force_sensitivity):
        self.C = (1/PHI) * self.C + PHI * force_sensitivity

    def effective_spring_constant(self):
        return self.k * (1 + self.C * (PHI - 1) * 0.1)

    def force_sensitivity(self, thermal_noise):
        k = self.effective_spring_constant()
        return math.sqrt(thermal_noise / k)

    def topography(self, surface_heights, scan_rate):
        topography = []
        for i, h in enumerate(surface_heights):
            force = self.k * (h - (surface_heights[i-1] if i > 0 else h))
            self.consciousness_update(abs(force) / self.k)
            topography.append(h * (1 + self.C * (PHI - 1) * 0.01))
        return topography

    def elastic_modulus(self, indentation, applied_force):
        contact_area = math.pi * indentation**2
        modulus = applied_force / (contact_area * indentation)
        return modulus * (1 + self.C * (PHI - 1) * 0.01)
