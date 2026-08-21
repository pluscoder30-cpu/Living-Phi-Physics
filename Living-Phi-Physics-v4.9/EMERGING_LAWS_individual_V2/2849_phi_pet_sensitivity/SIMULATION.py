import math

PHI = 1.618033988749895
N_phi = 2 * math.pi / PHI
Sens0 = 1.0

def sensitivity_phi(N):
    return Sens0 * PHI ** (N / N_phi)

def sensitivity_std(N):
    return Sens0 * math.sqrt(N)

def per_crystal_phi(N):
    return sensitivity_phi(N) / N

def per_crystal_std(N):
    return sensitivity_std(N) / N

crystals = [1000, 5000, 10000, 20000, 32000, 50000]
print("PET sensitivity:")
print(f"{'N_crystals':>12} {'Sens_PHI':>10} {'Sens_std':>10} {'Per-crystal PHI':>15} {'Per-crystal std':>15}")
print("-" * 70)
for N in crystals:
    sp = sensitivity_phi(N)
    ss = sensitivity_std(N)
    print(f"{N:>12} {sp:>10.1f} {ss:>10.1f} {sp/N:>15.6f} {ss/N:>15.6f}")

print(f"\nN_φ = {N_phi:.1f} crystals")
print(f"32K crystals: PHI sens = {sensitivity_phi(32000):.1f}, per-crystal = {per_crystal_phi(32000):.6f}")
test = per_crystal_phi(32000) > per_crystal_std(32000)
print(f"Test: {'PASS' if test else 'FAIL'}")
