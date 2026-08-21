import math

PHI = 1.618033988749895
k = 8.617e-5
Ea = 0.3
D0 = 1e-10

def D_std(T):
    return D0 * math.exp(-Ea / (k * T))

def D_phi(T):
    return D0 * math.exp(-Ea / (PHI * k * T))

print("Diffusion coefficient comparison:")
print(f"{'T(K)':>6} {'D_std':>12} {'D_phi':>12} {'Ratio':>8}")
print("-" * 42)
for T in [200, 250, 300, 350, 400, 500]:
    ds = D_std(T)
    dp = D_phi(T)
    print(f"{T:>6} {ds:>12.2e} {dp:>12.2e} {dp/ds:>8.2f}")

T = 300
ratio = D_phi(T) / D_std(T)
print(f"\nRatio at 300K: {ratio:.4f}")

c_range = [i * 0.1 for i in range(11)]
D_c = [D_phi(300) * PHI ** c for c in c_range]

print(f"\nConcentration dependence at 300K:")
print(f"{'c/c0':>6} {'D(c)':>12} {'Ratio':>8}")
for c, dc in zip(c_range, D_c):
    print(f"{c:>6.1f} {dc:>12.2e} {dc/D_c[0]:>8.2f}")

test = ratio > 1.0
print(f"\nPHI diffusion > standard: {'PASS' if test else 'FAIL'}")
