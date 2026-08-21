import math

PHI = 1.618033988749895
T0 = 300.0
T_target = 800.0
tau = 1.0
Ea = 50.0
R = 8.314

def T_phi(t):
    return T0 * PHI ** (t / tau)

def k_rate(T, phi_modified):
    if phi_modified:
        return math.exp(-Ea / (PHI * R * T))
    return math.exp(-Ea / (R * T))

t_peak = tau * math.log(T_target / T0) / math.log(PHI)
T_at_peak = T_phi(t_peak)

print(f"PHI pyrolysis temperature program:")
print(f"  T₀ = {T0:.0f} K")
print(f"  T_target = {T_target:.0f} K")
print(f"  Peak time: {t_peak:.2f} τ")
print(f"  T at peak: {T_at_peak:.0f} K")

print(f"\nRate constants at {T_at_peak:.0f}K:")
k_phi = k_rate(T_at_peak, True)
k_std = k_rate(T_at_peak, False)
print(f"  PHI-modified: {k_phi:.2e}")
print(f"  Standard: {k_std:.2e}")
print(f"  Ratio: {k_phi/k_std:.2f}")

print(f"\nActivation energy reduction: E_a/φ = {Ea/PHI:.1f} kJ/mol (vs {Ea:.1f})")
print(f"Effective barrier: {Ea/PHI/Ea*100:.1f}% of standard")
test = k_phi > k_std
print(f"Test: {'PASS' if test else 'FAIL'}")
