import math

PHI = 1.618033988749895
Ymax = 1.0 / PHI

def Y_phi(n):
    return Ymax * (1 - PHI ** (-n))

def Y_std(n):
    return (1 - (1/2)**n)

print("Syngas yield by gasification stage:")
print(f"{'Stages':>7} {'Y_PHI':>8} {'Y_std':>8} {'Diff(%)':>8}")
print("-" * 35)
for n in range(1, 7):
    yp = Y_phi(n)
    ys = Y_std(n)
    print(f"{n:>7} {yp:>8.4f} {ys:>8.4f} {(yp-ys)*100:>8.2f}")

print(f"\nMaximum yield: Y_max = 1/φ = {Ymax:.4f}")
print(f"3-stage: PHI={Y_phi(3):.4f}, std={Y_std(3):.4f}")
test = Y_phi(3) > Y_std(3)
print(f"Test: {'PASS' if test else 'FAIL'}")
