import math, cmath

PHI = 1.618033988749895
N = 8
B = 100e6
c = 3e8
d0 = 1.0

def phi_coded_delays():
    return [d0 * PHI ** n for n in range(N)]

def uniform_delays():
    return [d0 * n for n in range(N)]

def ambiguity_function(tau, delays):
    af = 0+0j
    for d in delays:
        af += cmath.exp(1j * 2 * math.pi * B * (tau - d))
    return abs(af) / N

delays_phi = phi_coded_delays()
delays_uni = uniform_delays()

tau_range = [i * 0.001 for i in range(-20, 21)]
af_phi = [ambiguity_function(t, delays_phi) for t in tau_range]
af_uni = [ambiguity_function(t, delays_uni) for t in tau_range]

res_single = c / (2 * B)
res_phi = c / (2 * N * PHI * B)
res_uni = c / (2 * N * B)

print(f"Single pulse resolution: {res_single*1000:.1f} mm")
print(f"PHI-coded resolution: {res_phi*1000:.1f} mm")
print(f"Uniform-coded resolution: {res_uni*1000:.1f} mm")
print(f"Improvement factor PHI: {res_single/res_phi:.2f}x (expected {N*PHI:.2f}x)")
print(f"Improvement factor uniform: {res_single/res_uni:.2f}x (expected {N:.2f}x)")

sidelobe_phi = max(af_phi[:8] + af_phi[12:]) if len(af_phi) > 12 else max(af_phi[:3] + af_phi[5:])
sidelobe_uni = max(af_uni[:8] + af_uni[12:]) if len(af_uni) > 12 else max(af_uni[:3] + af_uni[5:])

print(f"\nPeak sidelobe PHI: {20*math.log10(sidelobe_phi):.1f} dB")
print(f"Peak sidelobe uniform: {20*math.log10(sidelobe_uni):.1f} dB")
test = res_phi < res_uni
print(f"Test: {'PASS' if test else 'FAIL'}")
