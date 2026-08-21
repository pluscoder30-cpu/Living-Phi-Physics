import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
print(f"Latency: {round(15*(1-1.0*PHI_INV*0.12),1)} ns, Throughput: {round(50*(1+1.0*(PHI-1))+1.0*PHI_INV*5,1)} GB/s")
