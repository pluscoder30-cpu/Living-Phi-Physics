import math
PHI = (1 + 5**0.5) / 2; PHI_INV = 1 / PHI
def phi_cop(classical_cop, kappa=0.8):
    return classical_cop * (1 + kappa * (PHI - 1)) + kappa * PHI_INV * 0.5
cop_classical = 2.5; cop_phi = phi_cop(cop_classical, kappa=1.0)
print(f"COP: {cop_classical} -> {cop_phi:.2f} (gain: {cop_phi/cop_classical:.2f}x)")
print(f"Compressor freq: {528*PHI**5:.1f} Hz (retrocausal constant)")
