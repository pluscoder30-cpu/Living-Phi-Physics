import math

PHI = 1.618033988749895
C0 = 100.0
V_rated = 2.7
V_phi = V_rated / math.log(PHI)

def E_phi(V):
    return 0.5 * C0 * V ** 2 * PHI ** (V / V_phi)

def E_std(V):
    return 0.5 * C0 * V ** 2

voltages = [0.5, 1.0, 1.5, 2.0, 2.5, 2.7]
print("Supercapacitor energy density:")
print(f"{'V(V)':>6} {'E_PHI(J)':>10} {'E_std(J)':>10} {'Improvement':>12}")
print("-" * 42)
for V in voltages:
    ep = E_phi(V)
    es = E_std(V)
    imp = (ep / es - 1) * 100
    print(f"{V:>6.1f} {ep:>10.1f} {es:>10.1f} {imp:>11.1f}%")

print(f"\nAt rated voltage ({V_rated}V):")
print(f"  PHI: {E_phi(V_rated):.1f} J")
print(f"  Standard: {E_std(V_rated):.1f} J")
print(f"  Improvement: {(E_phi(V_rated)/E_std(V_rated)-1)*100:.1f}%")
test = E_phi(V_rated) > E_std(V_rated)
print(f"Test: {'PASS' if test else 'FAIL'}")
