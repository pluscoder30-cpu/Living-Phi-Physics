import math

PHI = 1.618033988749895
R0 = 1000.0

def R_phi(n):
    return R0 * PHI ** n

def R_std(n):
    return R0 * 2.0 ** n

def T_phi(n):
    return 1.0 / PHI ** n

def T_std(n):
    return 1.0 / 2.0 ** n

print("Resolving power and transmission by stage count:")
print(f"{'Stages':>7} {'R_PHI':>10} {'R_std':>10} {'T_PHI':>8} {'T_std':>8} {'R·T PHI':>10} {'R·T std':>10}")
print("-" * 75)
for n in range(1, 6):
    rp = R_phi(n)
    rs = R_std(n)
    tp = T_phi(n)
    ts = T_std(n)
    print(f"{n:>7} {rp:>10.0f} {rs:>10.0f} {tp:>8.4f} {ts:>8.4f} {rp*tp:>10.0f} {rs*ts:>10.0f}")

print(f"\n3-stage comparison:")
print(f"  PHI: R={R_phi(3):.0f}, T={T_phi(3):.4f}, R·T={R_phi(3)*T_phi(3):.0f}")
print(f"  Std: R={R_std(3):.0f}, T={T_std(3):.4f}, R·T={R_std(3)*T_std(3):.0f}")
print(f"  Resolution advantage std: {R_std(3)/R_phi(3):.2f}×")
print(f"  Transmission advantage PHI: {T_phi(3)/T_std(3):.2f}×")
test = T_phi(3) > T_std(3)
print(f"Test: {'PASS' if test else 'FAIL'}")
