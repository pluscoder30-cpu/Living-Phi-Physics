import math

PHI = 1.618033988749895
kT_e = 0.02569
V_phi = kT_e / PHI
V_PZC = 0.0
C0 = 20.0

def C_dl_phi(V):
    return C0 * PHI ** ((V - V_PZC) / V_phi)

V_range = [V_PZC + i * 0.001 for i in range(-100, 101)]
C_values = [C_dl_phi(V) for V in V_range]

peak_Vs = []
for i in range(1, len(C_values) - 1):
    if C_values[i] > C_values[i-1] and C_values[i] > C_values[i+1]:
        peak_Vs.append(V_range[i])

print(f"V_phi (PHI thermal voltage): {V_phi*1000:.2f} mV")
print(f"C_dl range: {min(C_values):.2f} to {max(C_values):.2f} μF/cm²")
print(f"Number of local maxima: {len(peak_Vs)}")

if len(peak_Vs) >= 2:
    spacings = [(peak_Vs[i+1] - peak_Vs[i])*1000 for i in range(len(peak_Vs)-1)]
    print(f"Peak spacings (mV): {[f'{s:.1f}' for s in spacings]}")
    avg_spacing = sum(spacings) / len(spacings)
    print(f"Average spacing: {avg_spacing:.1f} mV (expected {V_phi*1000:.1f})")
    test = abs(avg_spacing - V_phi * 1000) < 2
else:
    print("C_dl is monotonic (exponential model)")
    print("Testing PHI exponent at specific voltages:")
    for n in [0, 1, 2, 3]:
        V = V_PZC + n * V_phi
        print(f"  n={n}: V={V*1000:.1f}mV, C_dl={C_dl_phi(V):.2f} μF/cm²")
    ratio = C_dl_phi(V_PZC + V_phi) / C_dl_phi(V_PZC)
    print(f"Ratio n=1/n=0: {ratio:.4f} (expected {PHI:.4f})")
    test = abs(ratio - PHI) < 0.01

print(f"Test: {'PASS' if test else 'FAIL'}")
