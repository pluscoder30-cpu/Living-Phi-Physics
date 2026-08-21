import math

PHI = 1.618033988749895
T10 = 1.0
B0 = 14.1
B_phi = B0 / math.log(PHI)

def T1_phi(B):
    return T10 * PHI ** (B / B_phi)

def T2_phi(B):
    return T10 * PHI ** (B / B_phi) / PHI

fields = [7.0, 9.4, 11.7, 14.1, 16.4, 18.8, 21.1]
print("NMR relaxation times vs field:")
print(f"{'B(T)':>6} {'T₁(s)':>8} {'T₂(s)':>8} {'T₁/T₂':>8}")
print("-" * 34)
for B in fields:
    t1 = T1_phi(B)
    t2 = T2_phi(B)
    print(f"{B:>6.1f} {t1:>8.4f} {t2:>8.4f} {t1/t2:>8.4f}")

print(f"\nT₁/T₂ at all fields: {T1_phi(B0)/T2_phi(B0):.4f} (expected {PHI:.4f})")
print(f"B_φ = {B_phi:.2f} T")
print(f"T₁ at 14.1T: {T1_phi(14.1):.4f} s")
test = abs(T1_phi(B0) / T2_phi(B0) - PHI) < 0.001
print(f"Test: {'PASS' if test else 'FAIL'}")
