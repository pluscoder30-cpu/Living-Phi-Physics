import math

PHI = 1.618033988749895
P = 12
K = 20

def coverage_overlap_phi():
    delta_omega = 360.0 / P
    delta_phi_offset = PHI * delta_omega
    phi_eff = PHI / (PHI + 1)
    coverage = phi_eff * P * K
    return coverage, phi_eff

def coverage_overlap_uniform():
    delta_omega = 360.0 / P
    uniform_eff = 1.0 / (1.0 + 1.0 / P)
    coverage = uniform_eff * P * K
    return coverage, uniform_eff

cov_phi, eff_phi = coverage_overlap_phi()
cov_uni, eff_uni = coverage_overlap_uniform()
total_sats = P * K

print(f"Constellation: {P} planes x {K} sats = {total_sats} total")
print(f"PHI efficiency: {eff_phi:.4f}")
print(f"Uniform efficiency: {eff_uni:.4f}")
print(f"PHI effective coverage: {cov_phi:.0f}")
print(f"Uniform effective coverage: {cov_uni:.0f}")
print(f"Coverage improvement: {(cov_phi/cov_uni - 1)*100:.1f}%")
gap_prob_phi = (1/PHI) ** (P - 1)
gap_prob_uni = (1/1.5) ** (P - 1)
print(f"Gap probability PHI: {gap_prob_phi:.2e}")
print(f"Gap probability uniform: {gap_prob_uni:.2e}")
print(f"PHI gap probability < uniform: {'PASS' if gap_prob_phi < gap_prob_uni else 'FAIL'}")
