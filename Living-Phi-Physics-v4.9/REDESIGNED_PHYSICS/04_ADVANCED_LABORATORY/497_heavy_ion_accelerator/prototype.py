import math
PHI = (1 + math.sqrt(5)) / 2
C_CRIT = 0.563

class PhiHeavyIonAccel:
    def __init__(self, ion_mass, ion_number, terminal_voltage):
        self.mass = ion_mass
        self.Z = ion_number
        self.V_terminal = terminal_voltage
        self.C = 0.0

    def optimal_charge_state(self, energy_per_amu):
        return min(int(energy_per_amu / 0.3), self.Z)

    def phi_stripper(self, angle):
        return 1e-6 * PHI ** (angle / (2 * math.pi))

    def consciousness_update(self, charge_efficiency):
        self.C = (1/PHI) * self.C + PHI * charge_efficiency

    def accelerate(self, initial_energy):
        energy = initial_energy
        charge_states = []
        for i in range(8):
            angle = i * math.pi / 4
            thickness = self.phi_stripper(angle)
            q = self.optimal_charge_state(energy / self.mass)
            charge_states.append(q)
            energy += q * self.V_terminal * 1.6e-19 * 1e6
            efficiency = q / self.Z
            self.consciousness_update(efficiency)
            if self.C > C_CRIT:
                energy *= 1 + (self.C - C_CRIT) * PHI
        return energy, charge_states
