#!/usr/bin/env python3
import math
PHI=1.618033988749895
def phi_SER(s,snr): return s*PHI**(-snr/PHI)
if __name__=="__main__":
    for db in [5,10,15,20,25,30]:
        sl=10**(db/10); s=4*(1-0.25)*math.erfc(math.sqrt(3*sl/30))/2
        sp=phi_SER(s,sl); print(f"SNR={db:2d}dB SER_std={s:.2e} SER_phi={sp:.2e} imp={s/sp:.1f}x")
