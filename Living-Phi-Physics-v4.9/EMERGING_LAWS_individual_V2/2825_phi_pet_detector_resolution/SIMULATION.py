import math

PHI = 1.618033988749895
w0 = 4.0
N_levels = 3

def phi_segmentation(w0, n_levels):
    widths = [w0 / PHI ** i for i in range(n_levels)]
    return widths

def effective_resolution(widths):
    return widths[-1]

def doi_precision(widths):
    if len(widths) < 2:
        return widths[0]
    return widths[0] / PHI ** (len(widths) - 1)

widths = phi_segmentation(w0, N_levels)
R_eff = effective_resolution(widths)
DOI = doi_precision(widths)

print(f"PHI crystal segmentation:")
for i, w in enumerate(widths):
    print(f"  Level {i}: {w:.2f} mm")

print(f"\nEffective resolution: {R_eff:.2f} mm (expected {w0/PHI:.2f} mm)")
print(f"DOI precision: {DOI:.2f} mm (expected {w0/PHI**2:.2f} mm)")
print(f"Resolution improvement: {(1-R_eff/w0)*100:.1f}%")
print(f"Standard resolution: {w0:.2f} mm")
test = abs(R_eff - w0/PHI) < 0.01
print(f"Test: {'PASS' if test else 'FAIL'}")
