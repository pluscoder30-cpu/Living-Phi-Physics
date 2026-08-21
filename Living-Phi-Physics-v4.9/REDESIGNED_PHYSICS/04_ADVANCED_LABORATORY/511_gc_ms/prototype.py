import math
PHI = (1 + math.sqrt(5)) / 2

class PhiGCMS:
    def __init__(self, column_length, column_diameter):
        self.L = column_length
        self.d0 = column_diameter
        self.C = 0.0
        self.fragmentation_patterns = {}

    def consciousness_update(self, retention_time_shift):
        self.C = (1/PHI) * self.C + PHI * retention_time_shift

    def retention_time(self, boiling_point, polarity):
        base_rt = boiling_point * 0.01 * (1 + polarity)
        return base_rt * (1 + self.C * (PHI - 1) * 0.01)

    def electron_ionization(self, molecule_mw):
        fragments = []
        n_fragments = int(math.log(molecule_mw) / math.log(PHI))
        for i in range(n_fragments):
            fragment_mz = molecule_mw * PHI ** (-i)
            intensity = math.exp(-i / PHI)
            fragments.append((fragment_mz, intensity))
        return fragments

    def compound_identification(self, unknown_fragments, library):
        best_match = None
        best_score = 0
        for compound, lib_fragments in library.items():
            score = 0
            for mz, intensity in unknown_fragments:
                for lib_mz, lib_int in lib_fragments:
                    if abs(mz - lib_mz) < 0.5:
                        score += intensity * lib_int
            if score > best_score:
                best_score = score
                best_match = compound
        return best_match, best_score
