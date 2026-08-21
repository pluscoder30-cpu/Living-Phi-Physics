import math
PHI = (1 + math.sqrt(5)) / 2

class PhiTandetron:
    def __init__(self, terminal_voltage, n_strippers=3):
        self.V_terminal = terminal_voltage
        self.n_strippers = n_strippers
        self.foil_thicknesses = [1e-5 * PHI**i for i in range(n_strippers)]
        self.C = 0.0

    def charge_state(self, energy_per_amu, foil_thickness):
        return min(int(energy_per_amu / 0.5), 6)

    def consciousness_update(self, charge_efficiency):
        self.C = (1/PHI) * self.C + PHI * charge_efficiency

    def accelerate(self, mass, initial_energy):
        energy = initial_energy
        charge_states = []
        for i in range(self.n_strippers):
            thickness = self.foil_thicknesses[i]
            energy_per_amu = energy / mass
            q = self.charge_state(energy_per_amu, thickness)
            charge_states.append(q)
            energy += q * self.V_terminal * 1.6e-19 * 1e6
            efficiency = q / 6
            self.consciousness_update(efficiency * (1 + self.C * (PHI - 1)))
        return energy, charge_states
