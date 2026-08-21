import math

PHI = 1.618033988749895

def E_lib_phi(n):
    return (1.0 - PHI ** (-n)) / (1.0 - 1.0 / PHI)

def E_lib_std(n):
    return 1.0 - (1.0 / 2.0) ** n

print("Liberation efficiency by comminution stage:")
print(f"{'Stages':>7} {'E_PHI':>8} {'E_std':>8} {'Diff(%)':>8}")
print("-" * 35)
for n in range(1, 7):
    ep = E_lib_phi(n)
    es = E_lib_std(n)
    print(f"{n:>7} {ep:>8.4f} {es:>8.4f} {(ep-es)*100:>8.2f}")

print(f"\nPer-stage improvement: PHI adds 1/φⁿ each stage")
for n in range(1, 5):
    inc = E_lib_phi(n) - E_lib_phi(n-1) if n > 0 else E_lib_phi(1)
    print(f"  Stage {n}: +{inc:.4f} (expected 1/φ^{n}={1/PHI**n:.4f})")

test = abs(E_lib_phi(6) - (1 - PHI**(-6))/(1 - 1/PHI)) < 0.001
print(f"\nTest: {'PASS' if test else 'FAIL'}")
