import math

PHI = 1.618033988749895

def gain_phi(N):
    return N * PHI

def gain_std(N):
    return N

def SNR_gain(N):
    signal = sum(PHI ** (-n / N) for n in range(N))
    noise = sum(PHI ** (-2 * n / N) for n in range(N))
    return signal ** 2 / noise

print("Sonar processing gain:")
print(f"{'N':>4} {'G_PHI':>8} {'G_std':>8} {'Ratio':>8} {'SNR_meas':>10} {'Expected':>10}")
print("-" * 52)
for N in [8, 16, 32, 64, 128]:
    gp = gain_phi(N)
    gs = gain_std(N)
    snr = SNR_gain(N)
    print(f"{N:>4} {gp:>8.1f} {gs:>8.1f} {gp/gs:>8.2f} {snr:>10.1f} {gp:>10.1f}")

print(f"\n64-element: PHI gain = {gain_phi(64):.1f}, SNR improvement = {10*math.log10(PHI):.1f} dB")
test = abs(SNR_gain(64) - gain_phi(64)) < 5
print(f"Test: {'PASS' if test else 'FAIL'}")
