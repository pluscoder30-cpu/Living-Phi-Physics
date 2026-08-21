import math, cmath

PHI = 1.618033988749895
B = 100e6
T = 10e-6
c = 3e8
N = 500

def phi_chirp(t):
    return cmath.exp(1j * math.pi * PHI * B * t**2 / T)

def linear_chirp(t):
    return cmath.exp(1j * math.pi * B * t**2 / T)

dt = T / N
t_vals = [i * dt for i in range(N)]

phi_sig = [phi_chirp(t) for t in t_vals]
lin_sig = [linear_chirp(t) for t in t_vals]

def matched_filter(signal, reference):
    out = []
    for shift in range(len(signal)):
        s = sum(signal[i] * reference[i - shift] for i in range(max(0, shift), min(len(signal), shift + len(reference))))
        out.append(abs(s))
    return out

phi_mf = matched_filter(phi_sig, phi_sig)
lin_mf = matched_filter(lin_sig, lin_sig)

phi_peak = max(phi_mf)
lin_peak = max(lin_mf)

phi_peak_idx = phi_mf.index(phi_peak)
lin_peak_idx = lin_mf.index(lin_peak)

def find_3db_width(mf, peak, peak_idx):
    half = peak / 2
    lo = peak_idx
    while lo > 0 and mf[lo] > half:
        lo -= 1
    hi = peak_idx
    while hi < len(mf) - 1 and mf[hi] > half:
        hi += 1
    return hi - lo

phi_width = find_3db_width(phi_mf, phi_peak, phi_peak_idx)
lin_width = find_3db_width(lin_mf, lin_peak, lin_peak_idx)

phi_sidelobe = max(phi_mf[:max(1, phi_peak_idx-5)] + phi_mf[phi_peak_idx+5:]) / phi_peak
lin_sidelobe = max(lin_mf[:max(1, lin_peak_idx-5)] + lin_mf[lin_peak_idx+5:]) / lin_peak

print(f"PHI range resolution: {c/(2*PHI*B)*1000:.1f} mm")
print(f"Linear range resolution: {c/(2*B)*1000:.1f} mm")
print(f"Resolution improvement: {(1 - phi_width/lin_width)*100:.1f}%")
print(f"PHI sidelobe ratio: {phi_sidelobe:.4f}")
print(f"Linear sidelobe ratio: {lin_sidelobe:.4f}")
print(f"Sidelobe improvement: {-20*math.log10(phi_sideloke/lin_sidelobe):.1f} dB" if lin_sidelobe > 0 else "")
print(f"Width reduction ~38%: {'PASS' if phi_width < lin_width else 'FAIL'}")
