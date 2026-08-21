import math

PHI = 1.618033988749895
df0 = 1.0
theta0 = 18.5

def doppler_spread(theta):
    return df0 * PHI ** (abs(math.sin(math.radians(theta))) * 5 - 2.5)

angles = [i for i in range(0, 91)]
spreads = [doppler_spread(a) for a in angles]

min_spread = min(spreads)
min_angles = [a for a, s in zip(angles, spreads) if abs(s - min_spread) < 0.05]

print(f"Minimum Doppler spread: {min_spread:.3f} Hz")
print(f"Angles of minimum spread: {min_angles}°")

phi_resonant = [theta0 * PHI ** n for n in range(1, 5)]
phi_resonant = [a for a in phi_resonant if a < 90]
print(f"\nPHI-resonant angles: {[f'{a:.1f}' for a in phi_resonant]}°")

print(f"\nDoppler spread at key angles:")
for a in [0, 18, 30, 45, 60, 75, 90]:
    print(f"  θ={a}°: {doppler_spread(a):.3f} Hz")

print(f"\nReference: {df0/PHI:.3f} Hz at first PHI resonance")
test = min_spread < df0
print(f"Test: {'PASS' if test else 'FAIL'}")
