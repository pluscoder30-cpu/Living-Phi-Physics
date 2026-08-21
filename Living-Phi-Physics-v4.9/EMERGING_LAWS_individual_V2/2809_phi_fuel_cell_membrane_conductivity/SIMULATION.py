import math

PHI = 1.618033988749895
sigma0 = 0.01
lambda0 = 3.0

def sigma_phi(lam):
    return sigma0 * PHI ** (lam / lambda0)

def sigma_std(lam):
    return sigma0 * math.exp(lam / lambda0 * 0.5)

lambdas = list(range(1, 26))
sigma_phi_vals = [sigma_phi(l) for l in lambdas]
sigma_std_vals = [sigma_std(l) for l in lambdas]

max_phi = max(sigma_phi_vals)
max_std = max(sigma_std_vals)

phi_90 = next(l for l, s in zip(lambdas, sigma_phi_vals) if s >= 0.9 * max_phi)
std_90 = next(l for l, s in zip(lambdas, sigma_std_vals) if s >= 0.9 * max_std)

print("Proton conductivity vs water content:")
print(f"{'λ':>4} {'σ_PHI(S/cm)':>14} {'σ_std(S/cm)':>14} {'Ratio':>8}")
print("-" * 45)
for l in [1, 5, 10, 15, 20, 25]:
    sp = sigma_phi(l)
    ss = sigma_std(l)
    print(f"{l:>4} {sp:>14.4f} {ss:>14.4f} {sp/ss:>8.2f}")

print(f"\nσ_PHI at λ=14: {sigma_phi(14):.4f} S/cm")
print(f"σ_std at λ=14: {sigma_std(14):.4f} S/cm")
print(f"90% max reached at λ={phi_90} (PHI) vs λ={std_90} (std)")
print(f"PHI reaches 90% at {std_90/phi_90:.1f}× lower humidity")
test = phi_90 < std_90
print(f"Test: {'PASS' if test else 'FAIL'}")
