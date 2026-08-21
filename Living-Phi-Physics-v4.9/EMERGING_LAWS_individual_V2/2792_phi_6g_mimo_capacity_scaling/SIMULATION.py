import math

PHI = 1.618033988749895
B = 1e9
Nt, Nr = 64, 64

def mimo_capacity_ideal(rho, nt, nr):
    cap = 0.0
    for i in range(min(nt, nr)):
        snr_branch = rho * max(nt, nr) / min(nt, nr)
        cap += math.log2(1 + snr_branch)
    return B * cap

def mimo_capacity_phi(rho, nt, nr):
    cap = 0.0
    for i in range(min(nt, nr)):
        snr_branch = rho * max(nt, nr) / (PHI**2 * min(nt, nr))
        cap += math.log2(1 + snr_branch)
    return B * cap

print(f"{'SNR(dB)':>8} {'Ideal(bps)':>14} {'PHI(bps)':>14} {'Ratio':>8}")
print("-" * 50)
for snr_db in [0, 5, 10, 15, 20]:
    rho = 10 ** (snr_db / 10)
    ci = mimo_capacity_ideal(rho, Nt, Nr)
    cp = mimo_capacity_phi(rho, Nt, Nr)
    ratio = cp / ci
    print(f"{snr_db:>8} {ci:>14.0f} {cp:>14.0f} {ratio:>8.4f}")

rho_10 = 10
ratio_10 = mimo_capacity_phi(rho_10, Nt, Nr) / mimo_capacity_ideal(rho_10, Nt, Nr)
print(f"\nRatio at 10dB: {ratio_10:.4f}")
print(f"Expected ~0.78: {'PASS' if 0.75 < ratio_10 < 0.82 else 'FAIL'}")
