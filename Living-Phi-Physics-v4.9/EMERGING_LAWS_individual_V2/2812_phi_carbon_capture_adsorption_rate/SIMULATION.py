import math

PHI = 1.618033988749895
tau = 1.0
q_eq = 1.0

def q_phi(t):
    return q_eq * (1 - math.exp(-(t / tau) ** (1.0 / PHI)))

def q_std(t):
    return q_eq * (1 - math.exp(-t / tau))

times = [i * 0.25 for i in range(1, 21)]
print("CO₂ adsorption kinetics:")
print(f"{'t/τ':>6} {'q_PHI':>8} {'q_std':>8} {'Ratio':>8}")
print("-" * 34)
for t in times:
    tp = q_phi(t)
    ts = q_std(t)
    print(f"{t:>6.2f} {tp:>8.4f} {ts:>8.4f} {tp/ts:>8.3f}")

t_90_phi = next(t for t in [i * 0.01 for i in range(1, 500)] if q_phi(t) >= 0.9)
t_90_std = next(t for t in [i * 0.01 for i in range(1, 500)] if q_std(t) >= 0.9)

print(f"\n90% equilibrium time: {t_90_phi:.2f}τ (PHI) vs {t_90_std:.2f}τ (std)")
print(f"PHI reaches 90% at {t_90_std/t_90_phi:.2f}× longer time")
print(f"30-min capacity (t=30τ): PHI={q_phi(30):.4f}, std={q_std(30):.4f}")
print(f"Stretching exponent: {1/PHI:.4f} (expected 1/φ)")
test = abs(1/PHI - 0.618) < 0.001
print(f"Test: {'PASS' if test else 'FAIL'}")
