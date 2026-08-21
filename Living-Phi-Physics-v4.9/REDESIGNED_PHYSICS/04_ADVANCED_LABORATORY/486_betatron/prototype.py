import math
PHI = (1 + math.sqrt(5)) / 2

class PhiBetatron:
    def __init__(self, orbit_radius, B_max):
        self.radius = orbit_radius
        self.B_max = B_max
        self.phi_ratio = PHI / 2
        self.C = 0.0

    def acceleration(self, dB_dt, orbit_area):
        return orbit_area * dB_dt / (2 * math.pi * self.radius)

    def radiation_loss(self, energy):
        return 4.4e-9 * energy**4 / self.radius

    def consciousness_compensation(self, loss):
        self.C = (1/PHI) * self.C + PHI * loss
        if self.C > 0.563:
            return loss * (1 - (self.C - 0.563) * PHI)
        return loss

    def accelerate(self, initial_energy, dB_dt, n_turns=10000):
        energy = initial_energy
        energies = [energy]
        for turn in range(n_turns):
            gain = self.acceleration(dB_dt, math.pi * self.radius**2)
            loss = self.radiation_loss(energy)
            compensated_loss = self.consciousness_compensation(loss)
            energy = energy + gain - compensated_loss
            energies.append(energy)
            if energy <= 0:
                break
        return energies
