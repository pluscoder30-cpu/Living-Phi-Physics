import math

PHI = 1.618033988749895
PDE_max = 50.0
lambda_peak = 600.0
lambda_phi = 100.0
sigma = 80.0

def PDE_phi(lam):
    return PDE_max * PHI ** (-abs(lam - lambda_peak) / lambda_phi)

def PDE_gauss(lam):
    return PDE_max * math.exp(-(lam - lambda_peak) ** 2 / (2 * sigma ** 2))

wavelengths = [400, 500, 600, 700, 800, 900, 1000]
print("SiPM detection efficiency vs wavelength:")
print(f"{'λ(nm)':>8} {'PDE_PHI(%)':>12} {'PDE_Gauss(%)':>14} {'Ratio':>8}")
print("-" * 46)
for lam in wavelengths:
    pp = PDE_phi(lam)
    pg = PDE_gauss(lam)
    ratio = pp / pg if pg > 0.1 else float('inf')
    print(f"{lam:>8} {pp:>12.2f} {pg:>14.2f} {ratio:>8.2f}")

phi_width = 2 * lambda_phi * math.log(PHI)
gauss_width = 2.355 * sigma
print(f"\nPHI spectral width (1/e): {phi_width:.1f} nm")
print(f"Gaussian FWHM: {gauss_width:.1f} nm")
print(f"Width ratio: {phi_width/gauss_width:.2f}")
test = PDE_phi(800) > PDE_gauss(800)
print(f"Test: {'PASS' if test else 'FAIL'}")
