import math

PHI = 1.618033988749895
T1_0 = 260.0
tissue_names = ["Fat", "Muscle", "GM", "WM", "CSF"]
T1_values = [T1_0 * PHI ** n for n in range(5)]

print("PHI-clustered T1 values at 3T:")
for name, t1 in zip(tissue_names, T1_values):
    print(f"  {name}: {t1:.0f} ms")

S0 = 1.0
ti_range = [i * 10 for i in range(1, 150)]

def inversion_recovery(ti, t1):
    return S0 * abs(1 - 2 * math.exp(-ti / t1))

best_ti = 0
max_contrast = 0
for ti in ti_range:
    s_gm = inversion_recovery(ti, T1_values[2])
    s_wm = inversion_recovery(ti, T1_values[3])
    contrast = abs(s_gm - s_wm)
    if contrast > max_contrast:
        max_contrast = contrast
        best_ti = ti

optimal_theoretical = T1_0 * math.log(2) * PHI
print(f"\nOptimal TI (computed): {best_ti} ms")
print(f"Optimal TI (formula T1_0*ln(2)*phi): {optimal_theoretical:.0f} ms")
print(f"GM T1: {T1_values[2]:.0f} ms, WM T1: {T1_values[3]:.0f} ms")
print(f"Max contrast at optimal TI: {max_contrast:.4f}")
test = abs(best_ti - optimal_theoretical) < 15
print(f"Test: {'PASS' if test else 'FAIL'}")
