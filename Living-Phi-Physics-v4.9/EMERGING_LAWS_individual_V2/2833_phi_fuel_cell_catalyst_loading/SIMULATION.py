import math

PHI = 1.618033988749895
m0 = 0.1
i_phi = 0.3

def m_cat_phi(i):
    return m0 * PHI ** (i / i_phi)

def m_cat_std(i):
    return m0 * (i / i_phi) ** 2.0

currents = [0.1, 0.2, 0.3, 0.5, 0.7, 1.0]
print("Optimal catalyst loading vs current density:")
print(f"{'i(A/cm²)':>10} {'m_PHI(mg/cm²)':>15} {'m_std(mg/cm²)':>15} {'Saving(%)':>10}")
print("-" * 55)
for i in currents:
    mp = m_cat_phi(i)
    ms = m_cat_std(i)
    saving = (1 - mp / ms) * 100 if ms > 0 else 0
    print(f"{i:>10.2f} {mp:>15.4f} {ms:>15.4f} {saving:>10.1f}")

i_target = 0.5
mp = m_cat_phi(i_target)
ms = m_cat_std(i_target)
print(f"\nAt i={i_target} A/cm²:")
print(f"  PHI loading: {mp:.4f} mg/cm²")
print(f"  Standard loading: {ms:.4f} mg/cm²")
print(f"  Catalyst saving: {(1-mp/ms)*100:.1f}%")
test = mp < ms
print(f"Test: {'PASS' if test else 'FAIL'}")
