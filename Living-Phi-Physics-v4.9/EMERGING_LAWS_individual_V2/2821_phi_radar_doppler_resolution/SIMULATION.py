import math, cmath

PHI = 1.618033988749895
N = 256

def phi_window(n):
    return PHI ** (-n / N)

def rect_window(n):
    return 1.0

def spectrum(window_func):
    spectrum = []
    for k in range(N):
        s = sum(window_func(n) * cmath.exp(-2j * math.pi * k * n / N) for n in range(N))
        spectrum.append(abs(s))
    return spectrum

spec_phi = spectrum(phi_window)
spec_rect = spectrum(rect_window)

peak_phi = max(spec_phi)
peak_rect = max(spec_rect)

def find_3db_width(spec, peak):
    half = peak / math.sqrt(2)
    indices = [i for i, s in enumerate(spec) if s > half]
    if not indices:
        return len(spec)
    return max(indices) - min(indices) + 1

width_phi = find_3db_width(spec_phi, peak_phi)
width_rect = find_3db_width(spec_rect, peak_rect)

non_zero_phi = [s for s in spec_phi if s > peak_phi * 0.001]
non_zero_rect = [s for s in spec_rect if s > peak_rect * 0.001]

sidelobe_phi = max(non_zero_phi[5:]) / peak_phi if len(non_zero_phi) > 5 else 0
sidelobe_rect = max(non_zero_rect[5:]) / peak_rect if len(non_zero_rect) > 5 else 0

print(f"PHI window 3dB width: {width_phi} bins")
print(f"Rect window 3dB width: {width_rect} bins")
print(f"Width ratio: {width_phi/width_rect:.4f}")
print(f"PHI peak sidelobe: {20*math.log10(sidelobe_phi):.1f} dB")
print(f"Rect peak sidelobe: {20*math.log10(sidelobe_rect):.1f} dB")
test = width_phi <= width_rect
print(f"Test: {'PASS' if test else 'FAIL'}")
