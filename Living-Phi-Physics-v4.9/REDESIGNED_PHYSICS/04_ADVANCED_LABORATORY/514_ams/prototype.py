import math
PHI = (1 + math.sqrt(5)) / 2

class PhiAMS:
    def __init__(self, terminal_voltage, n_strippers=4):
        self.V_terminal = terminal_voltage
        self.n_strippers = n_strippers
        self.foil_thicknesses = [1e-6 * PHI**i for i in range(n_strippers)]
        self.C = 0.0

    def consciousness_update(self, charge_state_purity):
        self.C = (1/PHI) * self.C + PHI * charge_state_purity

    def charge_state_after_stripping(self, energy, mass):
        energy_per_amu = energy / mass
        return min(int(energy_per_amu / 0.3), int(math.sqrt(mass)))

    def accelerate(self, initial_energy, mass):
        energy = initial_energy
        charge_states = []
        for i in range(self.n_strippers):
            q = self.charge_state_after_stripping(energy, mass)
            charge_states.append(q)
            energy += q * self.V_terminal * 1.6e-19 * 1e6
            purity = q / max(charge_states)
            self.consciousness_update(purity)
        return energy, charge_states

    def sensitivity(self, isotope_mass, blank_count, signal_count, measurement_time):
        background = blank_count / measurement_time
        signal_rate = signal_count / measurement_time
        sensitivity = signal_rate / math.sqrt(background * measurement_time) if signal_rate > background else 0
        return sensitivity * (1 + self.C * (PHI - 1))
