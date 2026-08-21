import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI; C_CRIT = 0.563263
def phi_lock(inp, correct, kappa=0.8):
    m = sum(1 for a,b in zip(inp,correct) if a==b)/len(correct)
    C = m*(1+kappa*(PHI-1))
    return C > C_CRIT, round(C, 4)
c = [1,0,1,1,0,1]
for n,s in [("Match",c),("1w",[1,0,1,0,0,1]),("2w",[1,0,0,0,0,1])]:
    g,C = phi_lock(s,c,1.0); print(f"  {n}: C={C} Access={g}")
