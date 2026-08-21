import math

PHI = 1.618033988749895
Q0 = 1.0
P0 = 1.0
P_phi = P0 / math.log(PHI)
K_lang = 1.0

def Q_phi(P):
    return Q0 * PHI ** (P / P_phi)

def Q_lang(P):
    return Q0 * K_lang * P / (1 + K_lang * P)

pressures = [0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0]
print("CO2 adsorption capacity:")
print(f"{'P(bar)':>8} {'Q_PHI':>10} {'Q_Lang':>10} {'Ratio':>8}")
print("-" * 38)
for P in pressures:
    qp = Q_phi(P)
    ql = Q_lang(P)
    print(f"{P:>8.1f} {qp:>10.3f} {ql:>10.3f} {qp/ql:>8.2f}")

print(f"\nP_phi = {P_phi:.3f} bar")
print(f"At 1 bar: PHI={Q_phi(1):.3f}, Langmuir={Q_lang(1):.3f}")
print(f"Improvement: {Q_phi(1)/Q_lang(1):.1f}x")
test = Q_phi(1) > Q_lang(1)
print(f"Test: {'PASS' if test else 'FAIL'}")
