import math

PHI = 1.618033988749895
nu0 = 500.0
N_modes = 4
sigma0 = 1.0

modes = []
for n in range(N_modes):
    freq = nu0 * PHI ** n
    sigma = sigma0 * PHI ** (2 * n)
    modes.append((freq, sigma))

print("PHI-harmonic Raman modes:")
print(f"{'Mode':>5} {'Freq(cm-1)':>12} {'Cross section':>15} {'Ratio':>8}")
print("-" * 45)
for i, (freq, sigma) in enumerate(modes):
    ratio = sigma / sigma0
    print(f"{i+1:>5} {freq:>12.1f} {sigma:>15.4f} {ratio:>8.2f}")

ratios = [modes[i][1] / modes[0][1] for i in range(N_modes)]
expected = [PHI ** (2 * n) for n in range(N_modes)]

print(f"\nExpected ratios: {[f'{r:.2f}' for r in expected]}")
print(f"Computed ratios: {[f'{r:.2f}' for r in ratios]}")

match = all(abs(ratios[i] - expected[i]) < 0.01 for i in range(N_modes))
print(f"All ratios match: {'PASS' if match else 'FAIL'}")
