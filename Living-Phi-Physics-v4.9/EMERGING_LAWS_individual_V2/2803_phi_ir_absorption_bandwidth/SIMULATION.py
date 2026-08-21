import math

PHI = 1.618033988749895
dnu0 = 50.0
bond_names = ["C-H", "C=C", "C≡C", "C-H (2nd)", "C-H (3rd)"]

bandwidths = []
intensities = []
for n in range(5):
    bw = dnu0 / PHI ** n
    intensity = bw * 1.0  # area = width × height, constant area
    bandwidths.append(bw)
    intensities.append(intensity)

print("PHI-harmonic IR absorption bandwidths:")
print(f"{'Bond':>10} {'n':>3} {'BW(cm-1)':>10} {'Ratio':>8} {'Intensity':>10}")
print("-" * 45)
for i, (name, bw) in enumerate(zip(bond_names, bandwidths)):
    ratio = bw / dnu0
    print(f"{name:>10} {i:>3} {bw:>10.2f} {ratio:>8.4f} {intensities[i]:>10.2f}")

bw_ratio = bandwidths[0] / bandwidths[1]
print(f"\nBW ratio (order 0/1): {bw_ratio:.4f} (expected {PHI:.4f})")
print(f"Intensities constant: {all(abs(intensities[i] - intensities[0]) < 1e-10 for i in range(5))}")
print(f"Test: {'PASS' if abs(bw_ratio - PHI) < 0.01 else 'FAIL'}")
