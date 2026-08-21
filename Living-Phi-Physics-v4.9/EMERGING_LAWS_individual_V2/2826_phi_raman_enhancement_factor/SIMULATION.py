import math

PHI = 1.618033988749895

def EF_phi(N):
    return PHI ** (2 * N)

def EF_uniform(N):
    return (2.5) ** N

print("SERS enhancement factor by chain length:")
print(f"{'N':>4} {'EF_PHI':>12} {'EF_uniform':>12} {'Ratio':>8}")
print("-" * 40)
for N in range(3, 9):
    ep = EF_phi(N)
    eu = EF_uniform(N)
    print(f"{N:>4} {ep:>12.1f} {eu:>12.1f} {ep/eu:>8.2f}")

print(f"\nPer-particle enhancement:")
print(f"  PHI: φ² = {PHI**2:.2f}×")
print(f"  Uniform: 2.5×")
print(f"\n5-particle chain: PHI={EF_phi(5):.1f}×, uniform={EF_uniform(5):.1f}×")
print(f"Total for 100 hotspots: PHI={EF_phi(5)*100:.0f}×, uniform={EF_uniform(5)*100:.0f}×")
test = EF_phi(5) > EF_uniform(5)
print(f"Test: {'PASS' if test else 'FAIL'}")
