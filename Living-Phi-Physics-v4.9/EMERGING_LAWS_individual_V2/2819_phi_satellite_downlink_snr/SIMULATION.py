import math, random

PHI = 1.618033988749895
SNR0 = 15.0
A_phi = 6.18
N = 1000
random.seed(42)

def snr_phi(A):
    return SNR0 + A_phi * math.log(PHI) * random.gauss(0, 1)

def snr_std(A):
    return SNR0 + 8.0 * random.gauss(0, 1)

snr_phi_vals = sorted([snr_phi(0) for _ in range(N)])
snr_std_vals = sorted([snr_std(0) for _ in range(N)])

idx_618 = int(0.618 * N)
idx_99 = int(0.99 * N)

phi_reliable = snr_phi_vals[idx_618]
std_reliable = snr_std_vals[idx_99]

print(f"PHI model 61.8% reliable SNR: {phi_reliable:.1f} dB")
print(f"Standard model 99% reliable SNR: {std_reliable:.1f} dB")
print(f"Improvement: {phi_reliable - std_reliable:.1f} dB")

phi_threshold = SNR0 - 10 * math.log10(PHI)
print(f"\nTheoretical PHI threshold: {phi_threshold:.1f} dB")
print(f"Computed PHI 61.8%: {phi_reliable:.1f} dB")

print(f"\nSNR statistics:")
print(f"  PHI mean: {sum(snr_phi_vals)/N:.1f} dB")
print(f"  PHI std: {(sum((s-sum(snr_phi_vals)/N)**2 for s in snr_phi_vals)/N)**0.5:.2f}")
print(f"  Std mean: {sum(snr_std_vals)/N:.1f} dB")
print(f"  Std std: {(sum((s-sum(snr_std_vals)/N)**2 for s in snr_std_vals)/N)**0.5:.2f}")

test = phi_reliable > std_reliable
print(f"\nTest: {'PASS' if test else 'FAIL'}")
