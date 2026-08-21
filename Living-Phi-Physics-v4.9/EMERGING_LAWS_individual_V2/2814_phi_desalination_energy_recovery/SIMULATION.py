import math

PHI = 1.618033988749895

def eta_phi(n):
    return 1.0 - 1.0 / PHI ** n

def eta_std(n):
    return 1.0 - 1.0 / (n + 1)

print("Energy recovery efficiency by stage count:")
print(f"{'Stages':>7} {'η_PHI':>8} {'η_std':>8} {'Diff(%)':>8}")
print("-" * 35)
for n in range(1, 7):
    ep = eta_phi(n)
    es = eta_std(n)
    print(f"{n:>7} {ep:>8.4f} {es:>8.4f} {(ep-es)*100:>8.2f}")

print(f"\nTheoretical max (n→∞): PHI={eta_phi(20):.4f}, std={eta_std(20):.4f}")
print(f"Expected max: 1/φ = {1/PHI:.4f}")
print(f"3-stage: PHI={eta_phi(3):.4f}, std={eta_std(3):.4f}")
print(f"5-stage: PHI={eta_phi(5):.4f}, std={eta_std(5):.4f}")

test = abs(eta_phi(20) - 1/PHI) < 0.01
print(f"Converges to 1/φ: {'PASS' if test else 'FAIL'}")
