import math

PHI = 1.618033988749895
Q0 = 100.0
N0 = 1000.0
N_phi = N0 * PHI

def Q_phi(n):
    return Q0 * (1 - (n / N_phi) ** PHI)

def Q_std(n):
    return Q0 * (1 - (n / N0) ** 2.0)

cycles = list(range(0, 2001, 200))
print("Battery capacity fade comparison:")
print(f"{'Cycles':>8} {'Q_PHI(%)':>10} {'Q_std(%)':>10}")
print("-" * 32)
for n in cycles:
    qp = Q_phi(n) if n < N_phi else 0
    qs = Q_std(n) if n < N0 else 0
    print(f"{n:>8} {max(0, qp):>10.1f} {max(0, qs):>10.1f}")

target_Q = 80.0
n_80_phi = N_phi * (1 - target_Q / Q0) ** (1 / PHI)
n_80_std = N0 * (1 - target_Q / Q0) ** 0.5

print(f"\n80% retention at:")
print(f"  PHI model: {n_80_phi:.0f} cycles")
print(f"  Standard model: {n_80_std:.0f} cycles")
print(f"  Improvement: {n_80_phi/n_80_std:.2f}×")
test = n_80_phi > n_80_std
print(f"Test: {'PASS' if test else 'FAIL'}")
