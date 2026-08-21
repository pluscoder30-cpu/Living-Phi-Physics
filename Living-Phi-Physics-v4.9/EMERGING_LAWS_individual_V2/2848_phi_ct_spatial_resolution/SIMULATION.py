import math

PHI = 1.618033988749895
N_phi = 2 * math.pi / PHI
dx0 = 1.0

def resolution_phi(n_proj):
    return dx0 / PHI ** (n_proj / N_phi)

def resolution_std(n_proj):
    return dx0 / math.sqrt(n_proj)

projections = [100, 200, 300, 400, 600, 800, 1000]
print("CT spatial resolution vs projections:")
print(f"{'Projections':>12} {'Δx_PHI':>10} {'Δx_std':>10} {'Ratio':>8}")
print("-" * 44)
for n in projections:
    dp = resolution_phi(n)
    ds = resolution_std(n)
    print(f"{n:>12} {dp:>10.4f} {ds:>10.4f} {dp/ds:>8.3f}")

print(f"\nN_φ = {N_phi:.1f} projections")
print(f"At 600 projections: PHI={resolution_phi(600):.4f}, std={resolution_std(600):.4f}")
test = resolution_phi(600) < resolution_std(600)
print(f"Test: {'PASS' if test else 'FAIL'}")
