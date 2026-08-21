import math
PHI = (1 + math.sqrt(5)) / 2

class PhiNeutronSpectrometer:
    def __init__(self, flight_path_length, detector_distance):
        self.L = flight_path_length
        self.d = detector_distance
        self.C = 0.0

    def phi_crystal_rotation(self, position):
        golden_angle = 2 * math.pi * (1 - 1/PHI)
        return golden_angle * position

    def consciousness_update(self, energy_error):
        self.C = (1/PHI) * self.C + PHI * energy_error

    def energy_resolution(self, wavelength):
        base_res = wavelength / self.L * 1e-6
        phi_res = base_res * (1 - self.C * (PHI - 1) * 0.1) if self.C > 0 else base_res
        return phi_res

    def wavelength_from_tof(self, time_of_flight):
        return 3.956e-7 * self.L / time_of_flight

    def energy_from_wavelength(self, wavelength):
        return 81.81 / wavelength**2  # meV from Angstroms
