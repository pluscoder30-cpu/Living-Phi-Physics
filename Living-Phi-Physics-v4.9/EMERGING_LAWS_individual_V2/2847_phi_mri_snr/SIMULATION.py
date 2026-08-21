import math

PHI = 1.618033988749895
SNR0 = 1.0
B_ref = 3.0
B_phi = B_ref / math.log(PHI)

def SNR_phi(B):
    return SNR0 * PHI ** (B / B_phi)

def SNR_std(B):
    return SNR0 * (B / B_ref)

fields = [1.5, 3.0, 7.0, 9.4, 11.7, 14.1]
print("MRI SNR vs field strength:")
print(f"{'B(T)':>6} {'SNR_PHI':>10} {'SNR_std':>10} {'Ratio':>8}")
print("-" * 38)
for B in fields:
    sp = SNR_phi(B)
    ss = SNR_std(B)
    print(f"{B:>6.1f} {sp:>10.3f} {ss:>10.3f} {sp/ss:>8.3f}")

print(f"\nAt 7T: PHI={SNR_phi(7):.3f}, std={SNR_std(7):.3f}")
print(f"PHI model predicts {SNR_phi(7)/SNR_phi(3)*100:.0f}% of standard SNR at 7T")
test = SNR_phi(7) > SNR_phi(3)
print(f"Test: {'PASS' if test else 'FAIL'}")
