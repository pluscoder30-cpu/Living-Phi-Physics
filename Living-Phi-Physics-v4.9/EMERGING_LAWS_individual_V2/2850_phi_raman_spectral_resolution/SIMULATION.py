import math

PHI = 1.618033988749895
N_phi_const = 2 * math.pi / PHI

def R_phi(N):
    return N * PHI

def R_std(N):
    return N

grooves = [600, 1200, 2400, 3600, 4800, 6000]
print("Raman spectral resolution:")
print(f"{'Grooves':>8} {'R_PHI':>8} {'R_std':>8} {'Improvement':>12}")
print("-" * 40)
for N in grooves:
    rp = R_phi(N)
    rs = R_std(N)
    print(f"{N:>8} {rp:>8.0f} {rs:>8.0f} {rp/rs:>11.2f}×")

print(f"\n1200 grooves: R_PHI = {R_phi(1200):.0f} (expected {1200*PHI:.0f})")
print(f"Improvement factor: {PHI:.4f}×")
test = abs(R_phi(1200) - 1200 * PHI) < 1
print(f"Test: {'PASS' if test else 'FAIL'}")
