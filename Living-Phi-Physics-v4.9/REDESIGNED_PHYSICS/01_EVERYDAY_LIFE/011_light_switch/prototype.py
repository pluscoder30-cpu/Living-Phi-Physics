import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI; C_CRIT = 0.563263
def phi_switch_state(pos):
    return 1/(1+math.exp(-10*(pos-C_CRIT)))
for p in [0.0,0.25,0.5,0.75,1.0]:
    print(f"  Pos {p:.2f} -> {phi_switch_state(p)*100:.0f}%")
