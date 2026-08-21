import math

PHI = 1.618033988749895
tR0 = 1.0

def retention_index_phi(n, tR_prime):
    if tR_prime <= 0 or tR0 <= 0:
        return 0
    return 100 * (n + math.log(tR_prime / tR0) / math.log(PHI))

def retention_time_phi(n):
    return tR0 * PHI ** (n / PHI)

print("PHI-harmonic retention indices:")
print(f"{'n':>4} {'t_R(min)':>10} {'I_PHI':>10} {'Expected':>10}")
print("-" * 38)
for n in range(1, 6):
    tR = retention_time_phi(n)
    I = retention_index_phi(n, tR)
    expected = 100 * n * PHI
    print(f"{n:>4} {tR:>10.3f} {I:>10.1f} {expected:>10.1f}")

I_spacing = retention_index_phi(2, retention_time_phi(2)) - retention_index_phi(1, retention_time_phi(1))
print(f"\nIndex spacing: {I_spacing:.1f} (expected {100*PHI:.1f})")
print(f"Standard spacing: 100.0")
test = abs(I_spacing - 100 * PHI) < 1
print(f"Test: {'PASS' if test else 'FAIL'}")
