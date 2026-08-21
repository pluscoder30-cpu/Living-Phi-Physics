import math

PHI = 1.618033988749895
V_OC = 1.0
j0 = 0.1
a = 0.05

def V_phi(j):
    return V_OC - a * math.log(j / j0) / PHI

def V_std(j):
    return V_OC - a * math.log(j / j0)

j_range = [j0 * math.exp((V_OC - 0.3) * i / (a * 10)) for i in range(1, 21)]

P_phi = [V_phi(j) * j for j in j_range]
P_std = [V_std(j) * j for j in j_range]

V_peak_phi = j_range[P_phi.index(max(P_phi))]
V_peak_std = j_range[P_std.index(max(P_std))]

print("Fuel cell power density:")
print(f"{'j(A/cm²)':>10} {'V_PHI':>8} {'V_std':>8} {'P_PHI':>10} {'P_std':>10}")
print("-" * 50)
for j, vp, vs in zip(j_range[::2], P_phi[::2], P_std[::2]):
    vphi = V_phi(j)
    vstd = V_std(j)
    print(f"{j:>10.3f} {vphi:>8.4f} {vstd:>8.4f} {vp:>10.4f} {vs:>10.4f}")

print(f"\nPeak power voltage: PHI={V_peak_phi:.3f}V, std={V_peak_std:.3f}V")
print(f"Expected V_OC/φ = {V_OC/PHI:.3f}V")
print(f"Expected V_OC/2 = {V_OC/2:.3f}V")
test = abs(V_peak_phi - V_OC/PHI) < 0.05
print(f"Test: {'PASS' if test else 'FAIL'}")
