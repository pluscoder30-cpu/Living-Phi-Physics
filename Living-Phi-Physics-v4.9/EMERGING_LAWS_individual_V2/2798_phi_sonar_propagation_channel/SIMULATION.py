import math

PHI = 1.618033988749895
c = 1500.0
depth = 100.0
N_paths = 10
A0 = 1.0
tau0 = 2 * depth / c

def phi_channel_ir():
    taps = []
    for n in range(N_paths):
        delay = n * PHI * tau0
        amp = A0 / PHI ** n
        taps.append((delay, amp))
    return taps

def uniform_channel_ir():
    taps = []
    for n in range(N_paths):
        delay = n * tau0
        amp = A0 / (n + 1)
        taps.append((delay, amp))
    return taps

phi_taps = phi_channel_ir()
uni_taps = uniform_channel_ir()

tau_max_phi = phi_taps[-1][0]
tau_max_uni = uni_taps[-1][0]

bc_phi = 1.0 / (PHI * tau_max_phi)
bc_uni = 1.0 / tau_max_uni

print("PHI channel arrivals:")
for d, a in phi_taps:
    print(f"  delay={d*1000:.1f}ms, amp={a:.4f}")
print(f"tau_max PHI: {tau_max_phi*1000:.1f} ms")
print(f"tau_max uniform: {tau_max_uni*1000:.1f} ms")
print(f"Coherence BW PHI: {bc_phi:.1f} Hz")
print(f"Coherence BW uniform: {bc_uni:.1f} Hz")
print(f"B_c = 1/(phi*tau_max) = {1/(PHI*tau_max_phi):.1f} Hz")
test = abs(bc_phi - 1/(PHI*tau_max_phi)) < 0.01
print(f"Test B_c formula: {'PASS' if test else 'FAIL'}")
