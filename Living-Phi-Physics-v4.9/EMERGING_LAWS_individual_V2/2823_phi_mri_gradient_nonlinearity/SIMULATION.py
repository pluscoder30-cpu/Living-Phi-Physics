import math

PHI = 1.618033988749895
N_harmonics = 5
c0 = 1.0
r0 = 1.0

def legendre(n, x):
    if n == 0:
        return 1.0
    elif n == 1:
        return x
    else:
        return ((2*n-1)*x*legendre(n-1, x) - (n-1)*legendre(n-2, x)) / n

def G_phi(r, theta):
    total = 0.0
    for n in range(N_harmonics):
        c_n = c0 / PHI ** n
        total += c_n * (r / r0) ** n * legendre(n, math.cos(theta))
    return total

def G_std(r, theta):
    total = 0.0
    for n in range(N_harmonics):
        c_n = c0 / (n + 1)
        total += c_n * (r / r0) ** n * legendre(n, math.cos(theta))
    return total

FOV = 100
N_points = 10
rms_phi = 0
rms_std = 0

for i in range(N_points):
    for j in range(N_points):
        x = (i - N_points/2) / N_points * 2
        y = (j - N_points/2) / N_points * 2
        r = math.sqrt(x**2 + y**2) * r0
        theta = math.atan2(y, x)
        g_phi = G_phi(r, theta)
        g_std = G_std(r, theta)
        deviation_phi = abs(g_phi - c0) / c0
        deviation_std = abs(g_std - c0) / c0
        rms_phi += deviation_phi ** 2
        rms_std += deviation_std ** 2

rms_phi = math.sqrt(rms_phi / (N_points ** 2))
rms_std = math.sqrt(rms_std / (N_points ** 2))

print("Gradient nonlinearity comparison:")
print(f"RMS deviation PHI: {rms_phi:.4f}")
print(f"RMS deviation standard: {rms_std:.4f}")
print(f"Improvement: {(1 - rms_phi/rms_std)*100:.1f}%")
print(f"\nPHI coefficients: {[1/PHI**n for n in range(N_harmonics)]}")
print(f"Std coefficients: {[1/(n+1) for n in range(N_harmonics)]}")
test = rms_phi < rms_std
print(f"Test: {'PASS' if test else 'FAIL'}")
