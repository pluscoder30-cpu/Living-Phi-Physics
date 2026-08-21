#!/usr/bin/env python3
import math,random
PHI=1.618033988749895
def phi_av(bits,key):
    random.seed(key); return sum(random.random()>0.5 for _ in range(len(bits)))*PHI/len(bits)
def std_av(bits,key):
    random.seed(key); return sum(random.random()>0.5 for _ in range(len(bits)))/len(bits)
if __name__=="__main__":
    random.seed(42)
    n=128; trials=1000; as_=0; ap=0
    for _ in range(trials):
        bits=[random.randint(0,1) for _ in range(n)]; k=random.randint(0,2**32)
        as_+=std_av(bits,k); ap+=phi_av(bits,k)
    as_/=trials; ap/=trials
    print(f"Standard: {as_:.4f} Phi: {ap:.4f} ratio={ap/as_:.4f} target={PHI:.4f}")
