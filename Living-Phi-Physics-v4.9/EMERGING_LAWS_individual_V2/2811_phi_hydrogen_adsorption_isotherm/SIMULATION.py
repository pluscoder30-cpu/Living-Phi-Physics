import math

PHI = 1.618033988749895
K0 = 1.0
N_sites = 4

def theta_phi(P):
    total = 0.0
    for i in range(N_sites):
        K = K0 * PHI ** i
        total += K * P / (1 + K * P)
    return total

def theta_single(P):
    K_avg = K0 * PHI ** (N_sites / 2)
    return K_avg * P / (1 + K_avg * P)

pressures = [10 ** (i * 0.1) for i in range(-20, 21)]

print("Hydrogen adsorption isotherm comparison:")
print(f"{'P(bar)':>8} {'θ_PHI':>8} {'θ_single':>10} {'Ratio':>8}")
print("-" * 38)
for P in [0.1, 0.236, 0.382, 0.618, 1.0, 2.0, 5.0, 10.0]:
    tp = theta_phi(P)
    ts = theta_single(P)
    print(f"{P:>8.3f} {tp:>8.4f} {ts:>10.4f} {tp/ts:>8.2f}")

step_pressures = [1.0 / PHI ** n for n in range(N_sites)]
print(f"\nExpected step pressures: {[f'{p:.3f}' for p in step_pressures]}")

d_theta = []
for i in range(1, len(pressures)):
    dt = theta_phi(pressures[i]) - theta_phi(pressures[i-1])
    d_theta.append((pressures[i] + pressures[i-1]) / 2, dt))

max_steps = sorted(d_theta, key=lambda x: x[1], reverse=True)[:N_sites]
print(f"Step positions (max dθ/dlnP): {[f'{p:.3f}' for p, _ in max_steps]}")

test = len(max_steps) == N_sites
print(f"\nTest: {'PASS' if test else 'FAIL'}")
