import cmath, math

PHI = 1.618033988749895
N = 16
d_lambda = 0.5
k = 2 * math.pi

def array_factor(theta, phases):
    af = 0+0j
    for n in range(N):
        af += cmath.exp(1j * (k * d_lambda * math.sin(theta) + phases[n]))
    return abs(af) ** 2

def phi_phases():
    return [n * PHI * math.pi for n in range(N)]

def uniform_phases():
    return [0.0] * N

angles = [i * math.pi / 180 for i in range(-90, 91)]
phi_af = [array_factor(a, phi_phases()) for a in angles]
uni_af = [array_factor(a, uniform_phases()) for a in angles]

phi_max = max(phi_af)
uni_max = max(uni_af)

phi_3db = sum(1 for p in phi_af if p > phi_max / 2)
uni_3db = sum(1 for p in uni_af if p > uni_max / 2)

phi_sidelobe = max(p for p in phi_af[5:-5]) / phi_max
uni_sidelobe = max(p for p in uni_af[5:-5]) / uni_max

print(f"PHI beam width (3dB bins): {phi_3db}")
print(f"Uniform beam width (3dB bins): {uni_3db}")
print(f"Beamwidth ratio (phi/uni): {phi_3db/uni_3db:.4f}")
print(f"PHI sidelobe ratio: {phi_sidelobe:.4f}")
print(f"Uniform sidelobe ratio: {uni_sidelobe:.4f}")
print(f"Width reduction: {(1 - phi_3db/uni_3db)*100:.1f}%")
pass_test = phi_3db < uni_3db
print(f"Test: PHI narrower beam = {'PASS' if pass_test else 'FAIL'}")
