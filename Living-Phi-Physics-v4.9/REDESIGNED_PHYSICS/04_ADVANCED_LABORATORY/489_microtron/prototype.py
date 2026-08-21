import math
PHI = (1 + math.sqrt(5)) / 2
C_CRIT = 0.563

class PhiMicrotron:
    def __init__(self, cavity_voltage, n_recirculations):
        self.V = cavity_voltage
        self.n_recirc = n_recirculations
        self.C = 0.0

    def energy_gain(self, turn):
        return self.V * PHI ** (turn % 10)

    def consciousness_update(self, orbit_deviation):
        self.C = (1/PHI) * self.C + PHI * orbit_deviation

    def track(self, initial_energy):
        energy = initial_energy
        orbits = []
        for turn in range(self.n_recirc):
            gain = self.energy_gain(turn)
            energy += gain
            target_len = 2 * math.pi * (initial_energy + turn * self.V) / (1.6e-19 * 1.0)
            orbit_len = 2 * math.pi * energy / (1.6e-19 * 1.0)
            deviation = abs(orbit_len - target_len) / target_len
            self.consciousness_update(deviation)
            if self.C > C_CRIT:
                correction = 1 - (self.C - C_CRIT) * (PHI - 1) * 0.1
                energy *= correction
            orbits.append((turn, energy))
        return orbits
