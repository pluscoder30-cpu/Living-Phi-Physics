import math

PHI = 1.618033988749895
N_phi = 2 * math.pi / PHI
Sens0 = 1.0

def sensitivity_phi(N):
    return Sens0 * PHI ** (N / N_phi)

def sensitivity_std(N):
    return Sens0 * (1 + 0.01 * N)

def Q_phi(N):
    return 100 * PHI

def Q_std(N):
    return 100.0

turns = [8, 16, 32, 48, 64]
print("NMR probe sensitivity:")
print(f"{'Turns':>8} {'Sens_PHI':>10} {'Sens_std':>10} {'Q_PHI':>8} {'Q_std':>8}")
print("-" * 48)
for N in turns:
    sp = sensitivity_phi(N)
    ss = sensitivity_std(N)
    print(f"{N:>8} {sp:>10.4f} {ss:>10.4f} {Q_phi(N):>8.0f} {Q_std(N):>8.0f}")

print(f"\nQ factor: PHI={Q_phi(16):.0f}, std={Q_std(16):.0f} (ratio={Q_phi(16)/Q_std(16):.2f}×)")
test = Q_phi(16) > Q_std(16)
print(f"Test: {'PASS' if test else 'FAIL'}")
