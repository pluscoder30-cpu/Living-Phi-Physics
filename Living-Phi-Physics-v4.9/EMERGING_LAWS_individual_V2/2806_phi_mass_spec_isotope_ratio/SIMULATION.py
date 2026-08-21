import math

PHI = 1.618033988749895

def phi_isotope_abundances(n_isotopes):
    abundances = [PHI ** (-n * (n + 1) / 2) for n in range(n_isotopes)]
    total = sum(abundances)
    return [a / total * 100 for a in abundances]

carbon_abundances = phi_isotope_abundances(3)
observed_carbon = [98.93, 1.07, 1e-10]

print("Carbon isotopes (PHI-harmonic):")
print(f"  12C: {carbon_abundances[0]:.2f}%")
print(f"  13C: {carbon_abundances[1]:.4f}%")
print(f"  14C: {carbon_abundances[2]:.6f}%")

ratio_12_13 = carbon_abundances[0] / carbon_abundances[1]
ratio_12_13_obs = observed_carbon[0] / observed_carbon[1]
print(f"\n12C/13C ratio PHI: {ratio_12_13:.2f}")
print(f"12C/13C ratio observed: {ratio_12_13_obs:.2f}")
print(f"Ratio: {ratio_12_13 / ratio_12_13_obs:.2f}x")

elements = {"C": 3, "O": 3, "S": 4}
for elem, n_iso in elements.items():
    abund = phi_isotope_abundances(n_iso)
    print(f"\n{elem} isotopes: {[f'{a:.2f}%' for a in abund]}")

test = ratio_12_13 > 50
print(f"\n12C/13C > 50: {'PASS' if test else 'FAIL'}")
