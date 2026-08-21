import math

PHI = 1.618033988749895
eta_max = 1.0
materials = {"Al": 14.3, "Cu": 6.7, "Pb": 0.45}

def eta_phi(n, sigma_rho):
    m = sigma_rho / 5.0
    return eta_max * (1 - PHI ** (-n / max(m, 0.1)))

def eta_std(n, sigma_rho):
    return eta_max * (1 - 0.5 ** n)

print("Eddy current separation efficiency:")
print(f"{'Material':>8} {'σ/ρ':>6} {'η_PHI(3)':>10} {'η_std(3)':>10} {'Improvement':>12}")
print("-" * 50)
for mat, sr in materials.items():
    ep = eta_phi(3, sr)
    es = eta_std(3, sr)
    imp = (ep - es) / es * 100 if es > 0 else 0
    print(f"{mat:>8} {sr:>6.1f} {ep:>10.4f} {es:>10.4f} {imp:>11.1f}%")

print(f"\nAl (σ/ρ=14.3) at 3 stages: PHI={eta_phi(3, 14.3):.4f}, std={eta_std(3, 14.3):.4f}")
test = eta_phi(3, 14.3) > eta_std(3, 14.3)
print(f"Test: {'PASS' if test else 'FAIL'}")
