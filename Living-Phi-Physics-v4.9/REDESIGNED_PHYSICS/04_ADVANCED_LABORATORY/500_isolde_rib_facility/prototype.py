import math
PHI = (1 + math.sqrt(5)) / 2

class PhiISOLDE:
    def __init__(self, proton_energy, target_thickness):
        self.proton_E = proton_energy
        self.target_thickness = target_thickness
        self.C = 0.0

    def consciousness_update(self, release_efficiency):
        self.C = (1/PHI) * self.C + PHI * release_efficiency

    def release_time(self, isotope_mass, pore_size):
        classical_release = isotope_mass * 1e-9 / pore_size
        phi_release = classical_release / PHI
        self.consciousness_update(phi_release / classical_release)
        return phi_release

    def ionization_efficiency(self, ionization_potential):
        return math.exp(-ionization_potential / (self.proton_E * 1e-6))

    def production_rate(self, isotope_mass, ionization_potential, pore_size):
        production = self.proton_E * self.target_thickness * 1e-30
        ionization = self.ionization_efficiency(ionization_potential)
        release = 1 / self.release_time(isotope_mass, pore_size)
        self.consciousness_update(ionization * release)
        if self.C > 0.563:
            phi_boost = 1 + (self.C - 0.563) * PHI**2
        else:
            phi_boost = 1.0
        return production * ionization * release * phi_boost
